# ekms

Enterprise Knowledge Management System is a platform where employees can query company policies, technical documentation, and best practices.

# Generative EKMS – Stage 1

A lightweight Enterprise Knowledge Management System (EKMS) for generating summaries, explanations, and compliance checklists from documents.

## Quickstart

```bash
# Install deps
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY=""

# Run app
streamlit run app.py

# Docker commands
docker build -t ekms-generative .
docker run -p 8501:8501 --env OPENAI_API_KEY=sk-your-secret-key ekms-generative
```
