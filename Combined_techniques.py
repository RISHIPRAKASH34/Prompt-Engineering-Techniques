import streamlit as st
import requests
import time

OLLAMA_API = "http://localhost:11434/api/chat"

# Techniques list
techniques = [
    "Zero-shot",
    "One-shot",
    "Few-shot",
    "Chain-of-thought",
    "ReAct",
    "AI Skills"
]

def run_ollama(prompt):
    payload = {
        "model": "llama3.2",  # change if you installed another model
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    start_time = time.time()
    response = requests.post(OLLAMA_API, json=payload)
    end_time = time.time()

    if response.status_code == 200:
        data = response.json()
        output = data["message"]["content"]
        tokens = data.get("eval_count", "N/A")
        elapsed = round(end_time - start_time, 2)
        return output, tokens, elapsed
    else:
        return f"Error: {response.status_code}, {response.text}", "N/A", 0

# Streamlit UI
st.title("🤖 Apex Insight")
st.write("Compare different prompt engineering techniques")

technique = st.selectbox("Select a technique:", techniques)

problem = st.text_area("Enter your problem/prompt:")

if st.button("Run"):
    if technique == "Zero-shot":
        prompt = f"Answer directly without examples:\n{problem}"

    elif technique == "One-shot":
        prompt = f"Example: 'Translate Hola -> Hello'\nNow: {problem}"

    elif technique == "Few-shot":
        prompt = (
            "Here are several examples across different domains:\n"
            "Math: '12 × 8' -> 96\n"
            "Translation: 'Hola' -> Hello\n"
            "Sentiment: 'I hate traffic' -> Negative\n"
            "Reasoning: 'If a car travels 100 km in 2 hours, speed?' -> 50 km/h\n"
            "Now solve:\n"
            f"{problem}"
        )

    elif technique == "Chain-of-thought":
        prompt = f"Think step by step before answering. Show reasoning clearly, then final answer:\nProblem: {problem}"

    elif technique == "ReAct":
        prompt = (
            f"You are an agent that uses ReAct (Reason + Act). "
            f"First reason about the problem, then decide an action (like search, calculate, lookup), "
            f"then provide the final answer.\nProblem: {problem}\n"
            f"Format:\nReasoning: ...\nAction: ...\nObservation: ...\nAnswer: ..."
        )

    elif technique == "AI Skills":
        prompt = (
            "You are an AI with multiple professional skills. "
            "Depending on the problem, decide the most suitable role to adopt "
            "(Math Tutor, Coding Assistant, Travel Planner, Language Teacher, Motivational Coach). "
            "Clearly state which role you are using, then solve or explain:\n"
            f"{problem}"
        )

    else:
        prompt = problem

    status = st.empty()
    status.info("🚀 Generating...")

    output, tokens, elapsed = run_ollama(prompt)

    status.empty()

    st.subheader("📌 Response")
    st.write(output)

    st.subheader("📊 Performance Metrics")
    st.write(f"⏱ Time taken: {elapsed} seconds")
    st.write(f"🔢 Tokens used: {tokens}")