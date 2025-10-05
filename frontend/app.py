import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.resume_parser import parse_resume
from backend.skill_extraction import extract_skills
from backend.placement_scoring import score_candidate

st.title("Smart Resume Insights & Placement Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    resume_text = parse_resume("temp_resume.pdf")
    skills = extract_skills(resume_text)
    score = score_candidate(skills)
    st.subheader("Extracted Skills:")
    st.write(skills)
    st.subheader("Placement Score:")
    st.write(score)
