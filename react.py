# AI Shopping Assistant

import streamlit as st
from ollama import chat

st.set_page_config(page_title="ReAct")
st.markdown("<h2 style='text-align:left;'>Shopping Assistant</h2>", unsafe_allow_html=True)

product = st.text_input("🛒 Product Category:")
budget = st.text_input("💰 Budget:")
purpose = st.text_input("🎯 Purpose:")
brand = st.text_input("🏷️ Preferred Brand (optional):")

if st.button("🚀 Recommend"):
    with st.spinner("Finding with Reason..."):
        prompt = f"""You are an intelligent AI Shopping Assistant.
        Use the ReAct framework.
        Follow this format:

        Thought:
        Reason about the user's request.

        Action:
        Determine what information should be considered.

        Observation:
        Analyze the provided information.

        Repeat if necessary.

        Finally provide:
        Final Recommendation
        here are details:
        {product}
        {budget}
        {purpose}
        {brand}
        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.info(response["message"]["content"])
