# CyberSecurity Consultant

import streamlit as st
from ollama import chat

st.set_page_config(page_title="AI Skills")
st.markdown("<h2 style='text-align:left;'>Cybersecurity Consultant</h2>", unsafe_allow_html=True)

query = st.text_area("🛡️ Describe your cybersecurity issue:")
if st.button("🚀 Consult"):
    with st.spinner("Analyzing security issue..."):
        prompt = f"""Act as as cybersecurity consultant, analyze the query, and provide a detailed response.

        Responsibilities:
        - Analyze security threats.
        - Explain technical concepts simply.
        - Suggest best practices.
        - Recommend mitigation strategies.
        - Give practical advice.

        Client Query: {query}
        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.success(response["message"]["content"])
