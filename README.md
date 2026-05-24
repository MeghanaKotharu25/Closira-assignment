# Closira AI Agent Assignment

## Project Overview
This repository contains the intelligence layer for the "Closira" customer communication platform, implemented as a Python-based CLI workflow. The agent is configured for **Bloom Aesthetics Clinic**, capable of handling inbound inquiries, qualifying leads, and ensuring patient safety through strict escalation protocols.

## Features
* **Stage 1 (FAQ):** Responds to clinic-related queries grounded strictly in the provided `sop.json` data.
* **Stage 2 (Lead Qualification):** Executes a multi-step intake flow to collect patient requirements.
* **Stage 3 (Escalation Detection):** A two-tier safety system combining heuristic keyword matching and LLM-based reasoning to flag medical/legal questions or complaints.
* **Stage 4 (Conversation Summary):** Generates structured data at the end of the session, including intent and collected lead details.

## Setup Instructions

### Prerequisites
* Python 3.9+
* An [OpenRouter API Key](https://openrouter.ai/)

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/closira-assignment](https://github.com/your-username/closira-assignment)
   cd closira-assignment
   pip install -r requirements.txt

2. **Configure Environment::**
    **Create a .env file in the root directory and add your key:
    **OPENROUTER_API_KEY=sk-or-v1-your-key-here

3. **Run the agent::**
    ```bash
    python main.py

