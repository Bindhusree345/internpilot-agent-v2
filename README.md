# 🚀 InternPilot – AI Internship Assistant

InternPilot is an AI-powered multi-agent internship assistant that helps students and freshers streamline their internship preparation workflow.

It can:

✅ Analyze resumes  
✅ Suggest internship portals and opportunities  
✅ Generate professional cover letters  
✅ Create interview preparation questions  

This project is designed as a complete end-to-end internship assistant web app built with **Streamlit**.

---

## 🌟 Features

### 📄 Resume Analyzer Agent
- Upload your resume PDF  
- Extracts key skills, projects, and strengths  
- Provides a summarized profile for recruiters

### 🔍 Internship Finder Agent
- Suggests real internship portals and links  
- Helps users discover opportunities based on their goals

### ✉️ Cover Letter Generator Agent
- Automatically drafts a short professional internship cover letter  
- Personalized using resume highlights

### 🧠 Interview Preparation Agent
- Generates role-specific interview questions  
- Helps students practice before interviews

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit** (Frontend Web App)
- **DuckDuckGo Search API** (Internship search)
- **PyPDF** (Resume text extraction)
- **LLM Integration (Groq / HF API / Lightweight Models)**

---

## 📂 Project Structure

```bash
internpilot-agent-v2/
│── src/
│   ├── streamlit_app.py     # Main Streamlit UI
│   ├── agents.py            # Multi-agent workflow logic
│
│── requirements.txt         # Dependencies
│── Dockerfile               # Container deployment
│── README.md                # Project documentation
