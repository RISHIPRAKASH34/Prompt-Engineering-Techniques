
# AI Math Tutor

import streamlit as st
from ollama import chat

st.set_page_config(page_title="Chain-of-thought")
st.markdown("<h2 style='text-align:left;'>AI Math Tutor</h2>", unsafe_allow_html=True)

equation = st.text_input("🧮 Enter an equation/problem:")
if st.button("🚀 Solve"):
    with st.spinner("Solving step by step..."):
        prompt = f"""You are an expert mathematics tutor.

        Solve the following equation.
        Think step by step before arriving at the final answer.
        Clearly explain each step.

        Equation: {equation}
        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.success(response["message"]["content"])
