# osu! Private Server Chatbot

A Streamlit-based chatbot powered by Google's Gemini AI, designed to assist users with osu! gameplay, technical issues, and specifically focused on the `osuwin21.my.id` private server.

**As right now osuwin21.my.id server is inaccessible due hosting server issue, and developer still trying to fix it, any respon for osuwin21.my.id will return downtime server as an answer.**

## Features

*   **osu! Expertise**: Answers questions about gameplay mechanics, scoring, difficulty, and client settings.
*   **Technical Support**: Provides help with game installation, performance issues, and hardware requirements.
*   **Private Server Helper**: Offers specific guidance for the `osuwin21.my.id` server, including connection instructions and common setup issues.
*   **Status Awareness**: Informs users about the server's current downtime and suggests checking official communication channels.
*   **Community Links**: References the server website and community Discord for updates and discussions.
*   **Streaming Responses**: Provides a natural, chat-like conversation experience.

## Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **LLM**: [Gemini 2.5 Flash](https://ai.google.dev/)
*   **LangChain**: For LLM integration and prompt management
*   **Python**: Core application logic

## Requirements

*   Python 3.8+
*   Google Gemini API Key

## Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ImOyZo/osuwin21-chatbot
    cd osuwin21-chatbot
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Google API Key**
    *   Obtain a Google AI API Key from [Google AI Studio](https://aistudio.google.com/).
    *   **For Local Development**: Create a file `.streamlit/secrets.toml` in the project root:
        ```toml
        GOOGLE_API_KEY = "gemini-api-key"
        ```
    *   **For Streamlit Cloud Deployment**: Go to your app's settings, navigate to "Secrets", and paste:
        ```
        GOOGLE_API_KEY = "gemini-api-key"
        ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

## Configuration

The chatbot's behavior is primarily controlled by the `system_prompt` in `app.py`. You can customize this prompt to include more specific information about your private server, such as:

*   Detailed connection instructions
*   Server rules and guidelines
*   Specific beatmap or gameplay features
*   Correct community links (replace the placeholder Discord link)

