# AI Comment Moderator

import streamlit as st
from ollama import chat

st.set_page_config(page_title="Zero-shot")
st.markdown("<h2 style='text-align:left;'>Comment Moderator</h2>", unsafe_allow_html=True)

comment = st.text_input("Enter a comment to moderate:")
if st.button("🚀 Moderate"):
    with st.spinner("Moderating your comment..."):
        prompt = f"""You are a comment moderation AI.

        Classify the following comment into one category:
        Safe
        Offensive
        Spam
        Hate Speech
        Needs Human Review

        comment: 
        {comment}
        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.success(response["message"]["content"])
