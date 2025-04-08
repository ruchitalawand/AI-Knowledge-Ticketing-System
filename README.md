# AI-Knowledge-Ticketing-System
A service engineer is troubleshooting a part malfunction. They type in “problem with ECU not receiving ignition signal”. The AI classifies the intent, retrieves relevant articles about ECU and ignition issues, and displays them. If not satisfied, the engineer submits a ticket which is routed to the support team.

✅ Key Features:
🔍 Semantic Search using NLP: Users can input queries in natural language to find relevant help articles using zero-shot classification (via Hugging Face Transformers).
📂 AI-Powered Knowledge Base: Articles are categorized by tags and searched based on semantic similarity rather than keyword match.
🧾 Ticket Management System: Users can submit support tickets that are logged with real-time status tracking (open, in progress, closed).
👤 Admin Dashboard: Admins can manage articles, users, and view all submitted tickets.
💬 Simple Web UI: Intuitive interface for both knowledge search and ticket submission using Django templates.
🔐 User Authentication (Extendable): Based on Django’s authentication system for access control.
📦 RESTful APIs (Optional): Built using Django REST Framework for extensibility and integration with other services.

🛠️ Technologies Used:
Backend Framework: Django 3.2+
NLP Model: Hugging Face Transformers (zero-shot-classification)
API Layer: Django REST Framework
Database: SQLite (can be switched to PostgreSQL)
UI: Django Templates (HTML, Bootstrap optional)
Language: Python 3.8+
Dev Tools: Git, GitHub, pip, virtualenv
