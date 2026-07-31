# AI-Powered Automation: n8n Workflow & Python Integration

This repository showcases a dual approach to building AI-powered automated reporting systems:
1. **Low-Code/No-Code Workflow**: Built in **n8n**, integrating OpenAI LLMs and Gmail.
2. **Scripting & Workflow Automation**: Handled via custom **Python** scripts.

Python Development and Automation Architecture
<img width="854" height="527" alt="Captura de pantalla 2026-07-30 213420" src="https://github.com/user-attachments/assets/6551f8b9-76a2-44f9-9c62-444296de1066" />
<img width="855" height="510" alt="Captura de pantalla 2026-07-30 214201" src="https://github.com/user-attachments/assets/92e44637-9ed3-4c17-9e2a-68f145a1f723" />
<img width="859" height="522" alt="Captura de pantalla 2026-07-30 214106" src="https://github.com/user-attachments/assets/4016225b-8456-407c-ab23-f716688649eb" />


This repository contains robust, production-ready Python solutions focused on process automation, custom scripting, efficient data pipelines, and intelligent integrations.

Each project is designed with a strong emphasis on clean code architecture, maintainability, and modular design, ensuring that scripts do not just run, but scale securely in real-world environments.

Core Capabilities and Technical Stack
Custom Scripting and Task Automation: Development of tailored command-line tools and background workers to eliminate repetitive manual operations and operational bottlenecks.

Workflow and API Integrations: Seamless connection between disparate APIs, third-party services, and event-driven systems using webhooks (including platforms like n8n and Zapier).

Data Processing and ETL Pipelines: Extraction, transformation, validation, and loading of structured and unstructured datasets efficiently.

File and Document Automation: Automated batch processing of complex file structures (JSON, CSV, Excel spreadsheets, and text documents) with robust error-handling mechanisms.

Technology Ecosystem
Plaintext
Languages:    Python 3.x
Automation:   n8n, Zapier, Webhooks, Cron/Task Schedulers
Data and APIs: RESTful APIs, JSON, Pandas, Openpyxl, Requests
Databases:    SQL, SQLite, PostgreSQL (integration-ready)
Tooling:      Git, GitHub Actions, Virtual Environments (venv/poetry)
Architecture and Design Principles
Modular and Scalable: The codebase is structured into decoupled components (services, parsers, handlers), making future feature expansions seamless.

Resilient Error Handling: Implements comprehensive logging, exception management, and validation guards to prevent silent failures during automated execution.

Environment-Driven Configuration: Secure handling of credentials, tokens, and environment variables via .env management to protect sensitive information across deployments.

Why Python for Automation?
Python remains the gold standard for rapid prototyping and reliable backend automation due to its massive ecosystem of libraries and clean readability. These scripts are built to bridge the gap between heavy software development and agile day-to-day business efficiency.

n8n AI-Powered Automated Reporter
<img width="902" height="399" alt="n8n-preview png" src="https://github.com/user-attachments/assets/49887864-8ad5-4924-883a-0455f37b0a7c" />

Project Overview
This repository contains a production-ready, highly efficient workflow built in n8n designed to bridge the gap between Large Language Models and everyday communication tools. By integrating OpenAI's advanced LLMs directly with Gmail, this project automates the process of generating, formatting, and distributing intelligent reports and summaries on demand.

The solution demonstrates practical expertise in modern low-code architecture, seamless API integration, and dynamic variable mapping between disparate micro-services.

Architecture and Workflow Pipeline
The automation pipeline consists of three core sequential nodes meticulously configured to handle data payload transformation:

Manual Trigger (When clicking 'Execute workflow'): Initiates the pipeline on demand, providing a reliable control mechanism for testing, debugging, and batch execution.

AI Processing Node (OpenAI - Message a model): Interfaces directly with OpenAI's language models, evaluates incoming context, performs advanced natural language generation, and structures intelligent responses into clean JSON payloads.

Notification Node (Gmail - Send a message): Dynamically parses and maps output variables from the preceding AI node, constructs a polished HTML or plain-text email, and delivers it directly to the designated recipient's inbox.

Tech Stack and Prerequisites
To successfully deploy and run this workflow, ensure your environment meets the following requirements:

n8n Engine: Self-hosted instance or n8n Cloud environment.

OpenAI API: Active account with valid API credentials and billing credits.

Google Cloud / Gmail Integration: Authorized OAuth2 credentials configured within n8n to permit secure email dispatch.

Installation and Deployment Guide
Follow these steps to import and run the workflow in your own n8n environment:

Clone this repository or download the workflow JSON file (n8n-ai-gmail-workflow.json).

Log in to your n8n dashboard.

Navigate to the top-right options menu (...) and click Import from File.

Select and upload the downloaded JSON configuration file.

Set up and verify your required credentials:

Link your OpenAI API Credential using your private API key.

Complete the Google OAuth2 authentication flow for the Gmail node.

Save the workflow, click Execute workflow to test the pipeline, and verify delivery in your inbox.

Practical Use Cases and Business Value
Automated Executive Summaries: Instantly process lengthy text inputs, meeting notes, or data logs into concise digests sent to stakeholders.

Customer Support Triage: Leverage AI models to categorize inbound inquiries or feedback and automatically draft or send initial responses.

Scheduled and On-Demand Reporting Pipelines: Serve as a flexible backbone for periodic system status updates, data summaries, and automated notification loops.
