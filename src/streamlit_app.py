import streamlit as st
from agents import internpilot_controller

st.set_page_config(page_title="InternPilot v2", page_icon="🚀")

st.title("🚀 InternPilot v2 – Internship Assistant")
st.write("Paste resume → Find internships → Generate cover letter → Prepare interview")

# --------------------------
# Resume Input
# --------------------------
st.header("📄 Paste Your Resume Text")

resume_text = st.text_area(
    "Paste your resume content here:",
    height=250
)

if resume_text:
    st.success("✅ Resume text added successfully!")

# --------------------------
# Internship Goal
# --------------------------
st.header("🎯 Internship Goal")

goal = st.text_input("Enter your goal (example: Agentic AI Internship India)")

# --------------------------
# Run Workflow
# --------------------------
if st.button("Run Full Agentic Workflow"):

    if not resume_text.strip():
        st.error("❌ Please paste your resume first!")
    else:
        with st.spinner("Running InternPilot Agents..."):
            results = internpilot_controller(goal, resume_text)

        st.subheader("✅ Resume Summary")
        st.write(results["resume_summary"])

        st.subheader("🔍 Internship Links")
        st.text(results["internships"])

        st.subheader("✉️ Cover Letter Draft")
        st.write(results["cover_letter"])

        st.subheader("🧠 Interview Questions")
        st.write(results["questions"])
