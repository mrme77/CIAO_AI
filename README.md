# CIAO-AI

CIAO-AI is a locally hosted AI-powered application designed to help children answer questions about Italian history, geography, and language translations. It uses a combination of open-source tools to provide a private, efficient, and interactive experience.

## Features
- **Gradio Front-End**: A user-friendly interface for interacting with the AI.
- **Ollama LLM**: Runs the Gemma3 model locally on a Raspberry Pi.
- **LangChain**: Manages prompts and chains for better contextual understanding.
- **ChromaDB**: Provides long-term memory for storing and retrieving past interactions.
- **Firebase Integration**: Adds contextual memory about individual users to personalize conversations.

## Requirements
- Raspberry Pi 4 or newer (with at least 4GB RAM).
- Python 3.9 or higher.
- Docker (for running Ollama).

## Installation
1. Clone the repository:

2. Install dependencies:
uv pip install -r requirements.txt


3. Set up Ollama and download the Gemma3 model:
   Follow the instructions in `models/ollama_setup.md`.

4. Configure Firebase:
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/).
   - Download the `firebase_config.json` file and place it in the `firebase/` directory.

5. Run the application:


## Usage
- Open the Gradio interface in your browser (default: `http://localhost:7860`).
- Ask questions about Italian history, geography, or translations.
- The application will remember user preferences and past interactions using Firebase.

## Configuration
Edit `config.yaml` to customize model settings, memory paths, and other parameters.

## License
This project is open-source and licensed under the MIT License.


