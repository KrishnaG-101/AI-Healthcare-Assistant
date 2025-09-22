# 🏥 AI Healthcare Assistant

## 📝 Project Description

**AI Healthcare Assistant** is an advanced LLM + RAG-based chatbot designed to help users (patients) with medical queries. The assistant can answer questions and provide contextually relevant information by leveraging a Retrieval-Augmented Generation (RAG) system. A key feature is the ability for users to upload documents, which are parsed and used to provide the LLM with up-to-date and specific context, preventing hallucinations and ensuring more accurate responses. The system is trained on the knowledge base of the **Gale Medical Encyclopedia**.

---

## 🚀 Getting Started

To set up and run the project locally, follow these steps. This project uses **uv** as the package manager for fast and efficient dependency management.

### Prerequisites

-   **Python 3.10+**
-   **uv** package manager. If you don't have it, install it with `pip`:
    ```bash
    pip install "uv>=0.1.25"
    ```

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KrishnaG-101/AI-Healthcare-Assistant.git
    ```

2.  **Install dependencies using `uv`:**
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys for **Groq**, **Pinecone**, and **Google GenAI**.
    ```
    GOOGLE_API_KEY="your_google_api_key"
    GROQ_API_KEY="your_groq_api_key"
    PINECONE_API_KEY="your_pinecone_api_key"
    PINECONE_INDEX_NAME="your_pinecone_index_name"
    ```

### Running the Application

This project uses a split-architecture with a FastAPI backend for handling logic and a Streamlit frontend for the user interface.

1.  **Start the FastAPI backend:**
    This server will handle the API requests for document parsing and LLM calls.
    ```bash
    cd ./backend/
    uvicorn main:app --reload
    ```

2.  **Start the Streamlit frontend:**
    Open a new terminal window in the project directory and run the Streamlit app.
    ```bash
    cd ./frontend/
    streamlit run app.py
    ```

The application will open automatically in your web browser. If it doesn't, navigate to `http://localhost:8501`.

---

## ✨ Features

-   **Intelligent Chatbot:** Ask general medical questions and get informed, AI-generated responses.
-   **Contextual RAG:** Enhance answers with external knowledge from the **Gale Medical Encyclopedia**.
-   **Document Upload:** Submit medical reports or other documents (PDF format) to provide personalized context for your queries.
-   **Fast Responses:** Leverages **Groq** for high-speed LLM inference, ensuring a smooth user experience.

---

## 🛠️ Technology Stack

-   **Python:** The core programming language.
-   **uv:** A modern, fast Python package manager used for project dependency management.

### Backend & API
-   **FastAPI:** A high-performance web framework for building the backend API.
-   **Uvicorn:** An ASGI server to run the FastAPI application.
-   **Pypdf:** Used to parse and extract text from uploaded PDF documents.
-   **Python-Multipart:** Handles the processing of file uploads in the FastAPI application.

### Frontend & UI
-   **Streamlit:** A user-friendly framework for creating interactive web applications, serving as the chat interface.
-   **Requests:** Used by the frontend to make API calls to the FastAPI backend.

### LLM & RAG Ecosystem
-   **LangChain:** The primary framework for orchestrating the entire RAG pipeline, including document loading, chunking, embedding, and interaction with the LLM and vector store.
-   **LangChain-Groq:** Integrates with the Groq API for lightning-fast LLM inference.
-   **LangChain-Google-GenAI:** Connects to Google's generative AI models for additional LLM capabilities.
-   **Pinecone:** A managed vector database used to store and efficiently retrieve document embeddings for the RAG process.

### Other Modules
-   **Python-dotenv:** Manages environment variables for API keys and configurations.
-   **Pydantic:** Provides data validation and settings management.
-   **Tqdm:** A progress bar library, useful for tracking long-running processes like document parsing or embedding.
-   **Loguru:** A simple yet powerful logging library for debugging and tracking application events.

---

## 🤝 Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request.

---

## 📄 License

This Project is licenses under MIT License.
