# Customer Support Ticket Classifier

import streamlit as st
from ollama import chat

st.set_page_config(page_title="Few-shot")
st.markdown("<h2 style='text-align:left;'>Ticket Classifier</h2>", unsafe_allow_html=True)

ticket = st.text_area("🎫 Enter customer support ticket:")
if st.button("🚀 Classify"):
    with st.spinner("Classifying ticket..."):
        prompt = f"""You are a customer support ticket classifier.

        Classify tickets into one of these categories:
        - Billing
        - Technical Support
        - Delivery
        - Account
        - General Inquiry

        Examples:

        Ticket:
        I was charged twice for my subscription.

        Category:
        Billing

        -----------------------

        Ticket:
        I cannot log into my account.

        Category:
        Account

        -----------------------

        Ticket:
        My package hasn't arrived even after a week.

        Category:
        Delivery

        -----------------------

        Ticket:
        The application crashes whenever I open it.

        Category:
        Technical Support

        -----------------------

        Now classify this ticket.

        Ticket: {ticket}
        """
        response = chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
        st.info(response["message"]["content"])
