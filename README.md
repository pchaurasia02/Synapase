# ✦ Synapse — Smart Task Planner

> A gentle, intelligent task planner designed to help you organize your day, take small steps, and make meaningful progress without the pressure of perfection.

**Synapse** is a full-stack task management application built with **FastAPI, SQLModel, SQLite, Tailwind CSS, and Vanilla JavaScript**.

The goal is to create more than a basic to-do list — Synapse aims to make productivity feel calm, encouraging, and personal.

---

## ✧ Features

### Task Management

- Create new tasks
- View all tasks
- View individual tasks
- Mark tasks as completed
- Update existing tasks
- Delete tasks
- Clear completed tasks

### Productivity Dashboard

- Total task count
- Pending task count
- Completed task count
- Encouraging productivity messages
- Clean and distraction-free task interface

### UI & Experience

- Responsive design for desktop and mobile
- Ethereal, soft-feminine visual style
- Light and dark/night mode
- Glassmorphism-inspired cards
- Soft pastel gradients
- Encouraging microcopy
- Minimal and distraction-free interface

---

## 🌙 Design Philosophy

Synapse is designed around the idea that productivity doesn't have to feel overwhelming.

Instead of focusing only on how many tasks are left, the interface encourages users to recognize their progress.

> **You don't have to do everything. Just take the next step.**

The design uses:

- Lavender
- Soft pink
- Pearl white
- Deep navy and plum for night mode
- Subtle gradients
- Rounded cards
- Minimal animations
- Generous whitespace

The overall experience is intended to feel **ethereal, calm, intelligent, and encouraging**.

---

## 🛠️ Tech Stack

### Backend

- **Python**
- **FastAPI** — REST API framework
- **SQLModel** — ORM and data validation
- **SQLite** — Database
- **Uvicorn** — ASGI server

### Frontend

- **HTML5**
- **Tailwind CSS**
- **Vanilla JavaScript**

---

## 📁 Project Structure

```text
synapse/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── test.db
├── requirements.txt
└── README.md
