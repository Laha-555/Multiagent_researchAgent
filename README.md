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




#Agent	Responsibility
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
