# 🕵️‍♂️ Agentic Honeypot: The Scam Baiter

> *"Goodness gracious! Is that the number on the back of the card? My reading glasses are missing..."*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75B2?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📖 Overview

**Agentic Honeypot** is an intelligent, autonomous API designed to counter cyber scams by wasting scammers' time. Powered by **Google Gemini AI**, it acts as "Rajesh," a confused, elderly, non-tech-savvy persona who keeps scammers engaged in endless loops of fruitless conversation.

While the scammer is busy talking to Rajesh, the system silently operates in the background to:
1.  **Detect** phishing attempts.
2.  **Extract** critical intelligence (UPI IDs, Phone Numbers, Links).
3.  **Report** the data to authorities (or a central database).

---

## 🚀 Features

### 🧠 **Autonomous Persona Engine**
- Uses **Google Gemini 1.5 Flash** to generate context-aware, human-like responses.
- Maintains a consistent persona ("Rajesh") who is polite but "accidentally" incompetent.
- Dynamically adapts to SMS, WhatsApp, or Email contexts.

### 🕵️ **Real-Time Intelligence Extraction**
The system automatically parses incoming messages to capture:
- 🔗 **Phishing Links** (e.g., bit.ly, ngrok.io)
- 💳 **Bank Account Numbers**
- 💰 **UPI IDs / Payment Handles**
- 📞 **Scammer Phone Numbers**

### 📡 **Silent Callback Reporting**
- Intelligence is sent asynchronously to a central server (e.g., Cybercrime DB) without alerting the scammer.
- Calculates a **Risk Score** based on the conversation content.

---

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High-performance Async I/O)
- **AI Model:** [Google Gemini API](https://ai.google.dev/) (Generative responses)
- **Networking:** [Uvicorn](https://www.uvicorn.org/) & [Ngrok](https://ngrok.com/) (Tunneling)
- **Validation:** [Pydantic](https://docs.pydantic.dev/) (Data integrity)
- **Utilities:** Python `re` (Regex for intel extraction)

---


## ⚡ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/agentic-honeypot.git](https://github.com/your-username/agentic-honeypot.git)
cd agentic-honeypot
