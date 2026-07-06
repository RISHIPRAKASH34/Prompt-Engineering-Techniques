# AI Resume Organizer

import streamlit as st
from ollama import chat

st.set_page_config(page_title="One-shot")
st.markdown("<h2 style='text-align:left;'>Resume Organizer</h2>", unsafe_allow_html=True)

resume = st.text_area("📄 Paste an unstructured resume:")
if st.button("🚀 Organize"):
    with st.spinner("Organizing resume..."):
        prompt = f"""You are an AI Resume Organizer.

        Your task is to extract important information from an unstructured resume and present it in the exact format shown in the example.

        Example:

        Resume:
        John Smith
        Software Engineer

        Email: johnsmith@gmail.com
        Phone: +1-555-123-4567

        Skills:
        Python, Java, SQL, Docker

        Education:
        B.Tech in Computer Science
        University of California
        2020

        Experience:
        Software Engineer at ABC Technologies
        2020 - Present

        Output:

        Name: John Smith
        Job Title: Software Engineer
        Email: johnsmith@gmail.com
        Phone: +1-555-123-4567

        Skills:
        - Python
        - Java
        - SQL
        - Docker

        Education:
        - B.Tech in Computer Science
        - University of California
        - 2020

        Experience:
        - Software Engineer at ABC Technologies
        - 2020 - Present

        --------------------------------------------------

        Now organize the following resume in the same format.

        Resume: {resume}

        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.success(response["message"]["content"])
