# Chat with TXT File

A Python-based NLP project that allows users to chat with a TXT knowledge file using **semantic search** and **sentence embeddings**.

The system retrieves the most relevant information from the text file based on the meaning of the user's question.

---

## Features

- Chat with a TXT file
- Semantic similarity search
- Sentence embeddings using Sentence Transformers
- Meaning-based retrieval
- Confidence threshold for irrelevant questions
- Modular project structure

---

## Project Structure

```txt
chat-with-txt/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
│   └── knowledge.txt
│
└── modules/
    ├── __init__.py
    ├── loader.py
    ├── embedder.py
    ├── similarity.py
    └── retriever.py
```

---

## Technologies Used

- Python
- Sentence Transformers
- Scikit-learn
- NLP Embeddings
- Cosine Similarity

---

## Installation

Clone repository:

```bash
git clone <your-github-link>
```

Go to project folder:

```bash
cd chat-with-txt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run:

```bash
python main.py
```

Ask questions:

Example:

```txt
What is machine learning?
```

Output:

```txt
Machine learning is a subset of artificial intelligence that helps systems learn from data.
```

---

## Example Use Cases

- Document Question Answering
- Knowledge Search
- Chatbots
- Mini RAG Systems
- Information Retrieval

---

## Future Improvements

- PDF support
- Multi-document chat
- Memory/chat history
- Streamlit UI
- RAG with LLM integration

---

## Author

Ananth Jeeth Vuppala