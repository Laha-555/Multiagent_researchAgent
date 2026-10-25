🤖 Multi-Agent AI Research Assistant

An AI-powered research application built with Streamlit, LangChain, NVIDIA Nemotron, and DuckDuckGo Search. The application uses a multi-agent architecture in which specialized AI agents collaborate to research a topic, analyze information, and generate a comprehensive final response.

✨ Features
Research Agent: Searches the web using DuckDuckGo and gathers relevant information.
Analysis Agent: Analyzes supplied information, identifies insights, and evaluates benefits, risks, and limitations.
Supervisor Agent: Coordinates specialist agents and combines their findings into a final answer.
Interactive User Interface: Enter any research topic or question through a Streamlit web interface.
Real-Time Processing: Displays a loading indicator while the agents process your request.
Download Results: Download generated responses as Markdown files.
Error Handling: Displays errors related to agent initialization and execution.
🏗️ Architecture

The application follows a supervisor-based multi-agent architecture.

text
                  User Input
                      |
                      v
              Supervisor Agent
                      |
             +--------+--------+
             |                 |
             v                 v
        Research Agent    Analysis Agent
             |                 |
             v                 |
       DuckDuckGo Search        |
             |                 |
             +--------+--------+
                      |
                      v
               Final Response
                      |
                      v
                Streamlit UI

Agent Responsibilities
Agent	Responsibility
Research Agent	Searches the web and summarizes relevant findings.
Analysis Agent	Evaluates information and identifies important insights.
Supervisor Agent	Coordinates the specialist tools and produces the final response.

The supervisor decides which tools to invoke based on the user's question and its instructions.

🛠️ Technologies Used
Python — Application programming language.
Streamlit — Interactive web application interface.
LangChain — Agent creation and tool integration.
NVIDIA Nemotron — Large language model accessed through NVIDIA AI Endpoints.
DuckDuckGo Search — Web search integration.
python-dotenv — Loads environment variables from a .env file.
📁 Project Structure
text
multi-agent-ai-research-assistant/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

app.py — Main Streamlit application containing the agents and user interface.
.env — Stores the NVIDIA API key.
.gitignore — Prevents sensitive files and unnecessary files from being committed.
requirements.txt — Lists the Python dependencies.
README.md — Project documentation.
⚙️ Prerequisites

Before running the application, make sure you have:

Python 3.10 or a compatible version supported by your installed dependencies.
An NVIDIA API key.
An internet connection for model access and web searches.
pip installed.
🚀 Installation and Setup
1. Clone the repository

If your project is hosted on GitHub:

bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY


Replace the repository URL with your actual GitHub repository.

Alternatively, create a project folder and place app.py inside it.

2. Create a virtual environment

Windows:

bash
python -m venv venv
venv\Scripts\activate


macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

Create a requirements.txt file with the following contents:

text
streamlit
python-dotenv
langchain
langchain-community
langchain-nvidia-ai-endpoints
duckduckgo-search


Install the packages:

bash
pip install -r requirements.txt

4. Configure the NVIDIA API key

Obtain an API key from the NVIDIA API Catalog.

Create a .env file in the project root:

env
NVIDIA_API_KEY=your_nvidia_api_key_here


Replace the placeholder with your actual API key.

Security: Never publish your API key or commit your .env file to a public repository.

5. Create a .gitignore file

Add the following entries:

gitignore
.env
venv/
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml

6. Run the application

Start the Streamlit server:

bash
streamlit run app.py


Open the local URL displayed in your terminal, usually:

text
http://localhost:8501

💡 How to Use
Launch the application.
Enter a research topic or question in the input field.
Click Run AI Agents.
Wait while the supervisor coordinates the available specialist tools.
Review the generated research and analysis.
Click Download Results to save the response as a Markdown file.
Example Questions
What are the benefits and risks of AI agents?
How is generative AI transforming healthcare?
What are the advantages and limitations of renewable energy?
Analyze the applications of blockchain technology in supply chain management.
What are the opportunities and challenges of autonomous vehicles?
🔄 Workflow
User input: The user submits a research question through Streamlit.
Task coordination: The supervisor determines how to approach the question.
Research: The research tool invokes the research agent, which can use DuckDuckGo Search.
Analysis: The supervisor can send relevant information to the analysis tool for further evaluation.
Response generation: The supervisor combines the available findings into a final answer.
Presentation: Streamlit displays the response and provides an option to download it.
🔐 Environment Variables
Variable	Description
NVIDIA_API_KEY	API key used to authenticate with NVIDIA AI Endpoints.

The python-dotenv package loads the environment variables from the .env file.

⚠️ Limitations
Research quality depends on search results and their availability.
AI-generated responses can contain incorrect or incomplete information.
Search results should be verified against reliable primary sources.
The supervisor may not invoke every specialist tool for every question.
API usage may be subject to NVIDIA service limits, availability, and applicable pricing.
Response time depends on model latency, search performance, and the number of agent calls.
The application does not guarantee that every generated claim includes a verifiable source citation.
🧰 Troubleshooting
NVIDIA API key error
Verify that .env is in the project root.
Confirm that the variable is named NVIDIA_API_KEY.
Ensure the API key is valid and has access to the selected model.
Restart Streamlit after changing environment variables.
Module not found

Install the dependencies again:

bash
pip install -r requirements.txt

Search or connection errors
Check your internet connection.
Verify that the search dependency is installed.
Retry if the search provider or model endpoint is temporarily unavailable.
Streamlit command not found

Try running:

bash
python -m streamlit run app.py

🔮 Future Improvements

Potential enhancements include:

Display separate research and analysis outputs.
Add conversation history and follow-up questions.
Provide source URLs and citations for research findings.
Add configurable model selection.
Implement streaming responses.
Add PDF and DOCX export.
Add caching and request limits to control API usage.
Deploy the application using Streamlit Community Cloud or another hosting platform.
🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

Fork the repository.
Create a feature branch.
Make your changes.
Submit a pull request with a description of the improvements.
📄 License

Choose a license appropriate for your project before distributing it publicly. For example, you can use the MIT License by adding a LICENSE file containing the applicable license text.

🙌 Acknowledgements
Streamlit
LangChain
NVIDIA AI
DuckDuckGo

Built with Python, LangChain, NVIDIA Nemotron, and Streamlit.
