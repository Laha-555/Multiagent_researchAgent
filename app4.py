
import streamlit as st
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables
load_dotenv()

# --------------------------------------------------
# Streamlit page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Multi-Agent AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Research Assistant")
st.write(
    "Enter a topic or question. The Research Agent gathers "
    "information, the Analysis Agent reasons about it, and "
    "the Supervisor Agent combines the results."
)

# --------------------------------------------------
# Initialize agents only once
# --------------------------------------------------
@st.cache_resource
def initialize_agents():

    # NVIDIA LLM
    llm = ChatNVIDIA(
        model="nvidia/nemotron-3.5-lightning-30b-a3b"
    )

    # Web search tool
    search = DuckDuckGoSearchRun()

    # Specialist 1: Research Agent
    research_agent = create_agent(
        model=llm,
        tools=[search],
        system_prompt=(
            "You are a research specialist. "
            "Use web search to gather relevant information. "
            "Summarize key facts, evidence, and sources. "
            "Clearly distinguish verified facts from uncertainty."
        )
    )

    # Specialist 2: Analysis Agent
    analysis_agent = create_agent(
        model=llm,
        tools=[],
        system_prompt=(
            "You are an analysis specialist. "
            "Analyze the supplied information logically. "
            "Identify key insights, benefits, risks, "
            "limitations, and practical implications. "
            "Do not invent facts or sources."
        )
    )

    # Tool 1: Research
    @tool
    def research_topic(topic: str) -> str:
        """Research a topic using web search and summarize findings."""
        result = research_agent.invoke({
            "messages": [
                {"role": "user", "content": topic}
            ]
        })
        return str(result["messages"][-1].content)

    # Tool 2: Analysis
    @tool
    def analyze_information(information: str) -> str:
        """Analyze information supplied by the supervisor."""
        result = analysis_agent.invoke({
            "messages": [
                {"role": "user", "content": information}
            ]
        })
        return str(result["messages"][-1].content)

    # Supervisor Agent
    supervisor = create_agent(
        model=llm,
        tools=[
            research_topic,
            analyze_information
        ],
        system_prompt=(
            "You are a supervisor coordinating specialist agents. "
            "For each user question, use research_topic to gather "
            "relevant evidence. Then use analyze_information to "
            "analyze the research when appropriate. Finally, "
            "provide a clear, structured answer combining the "
            "research and analysis. Do not claim to have used a "
            "tool unless you actually used it."
        )
    )

    return research_agent, analysis_agent, supervisor


# --------------------------------------------------
# Load agents
# --------------------------------------------------
try:
    research_agent, analysis_agent, supervisor = initialize_agents()
except Exception as e:
    st.error(f"Could not initialize the AI agents: {e}")
    st.stop()


# --------------------------------------------------
# User input
# --------------------------------------------------
st.subheader("Ask a research question")

with st.form("research_form"):
    user_input = st.text_area(
        "Enter your topic or question:",
        placeholder=(
            "Example: Research the benefits and risks of AI agents."
        ),
        height=120
    )

    submitted = st.form_submit_button(
        "🚀 Run AI Agents",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# Execute supervisor
# --------------------------------------------------
if submitted:

    if not user_input.strip():
        st.warning("Please enter a topic or question first.")

    else:
        st.session_state["last_question"] = user_input.strip()

        with st.spinner(
            "AI agents are researching and analyzing your question..."
        ):
            try:
                result = supervisor.invoke({
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input.strip()
                        }
                    ]
                })

                answer = result["messages"][-1].content

                st.session_state["last_answer"] = answer

            except Exception as e:
                st.error(f"An error occurred while processing: {e}")


# --------------------------------------------------
# Display result
# --------------------------------------------------
if st.session_state.get("last_answer"):

    st.divider()
    st.subheader("📌 Research Results")

    st.markdown(
        st.session_state["last_answer"]
    )

    st.download_button(
        label="⬇️ Download Results",
        data=str(st.session_state["last_answer"]),
        file_name="ai_research_results.md",
        mime="text/markdown",
        use_container_width=True
    )


# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.header("About this application")

    st.markdown(
        """
        **Research Agent**
        - Searches the web
        - Collects relevant findings

        **Analysis Agent**
        - Examines the supplied information
        - Identifies insights and risks

        **Supervisor Agent**
        - Coordinates both specialists
        - Produces the final response
        """
    )

    st.divider()

    st.caption(
        "Powered by LangChain, NVIDIA Nemotron, "
        "DuckDuckGo Search, and Streamlit."
    )
