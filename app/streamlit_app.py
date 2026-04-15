import streamlit as st
import requests

st.title("AI Resume Analyzer")

resume = st.text_area("Paste Resume")
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={"resume": resume, "jd": jd}
    )

    result = response.json()

    st.write("Match Score:", result["match_score"])
    st.write("Level:", result["match_level"])
    st.write("Missing Skills:", result["missing_skills"])
    st.write("Suggestion:", result["suggestion"])