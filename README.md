# AI-Powered Automation: n8n Workflow & Python Integration

This repository showcases a dual approach to building AI-powered automated reporting systems:
1. **Low-Code/No-Code Workflow**: Built in **n8n**, integrating OpenAI LLMs and Gmail.
2. **Scripting & Workflow Automation**: Handled via custom **Python** scripts.

<img width="902" height="399" alt="n8n-preview png" src="https://github.com/user-attachments/assets/52f3383e-4d8b-4195-a140-5282da4bba40" />


---

Repository Structure

- `/workflow/n8n-ai-gmail.json` - The exported n8n workflow file.
- `/src/main.py` - The equivalent Python script handling API requests and integrations.

---

Quick Start (Python)

If you prefer running the logic via Python:

```bash
pip install openai
python src/main.py
