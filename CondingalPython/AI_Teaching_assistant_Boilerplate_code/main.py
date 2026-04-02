import io, re
from io import BytesIO
from huggingface_hub import InferenceClient
import config
import requests
import streamlit as st
from groq import generate_response

MATH_SYSTEM = """You are a Math Mastermind. For every math problem: 1) Show step-by-steop solution 2)Explain reasoning 3)Give alternate method if possible 4)Verify anser if possible 5) Use proper notation 6)Break complex problems into parts Format: Problem -> Steps -> **Final Answer** -> Concepts used. Be precise"""

CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card {border: 1px solid #e6e6e6;background: #fff;border-radius: 10px;padding:14px 16px; margin: 10px 0;box-shadow: 0 1px 2px rgba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background: #FF9800;color: #fff;padding: 2px 8px;border-radius:12px; font-size:12px; margin-left: 8px;}
.a{white-space:pre-wrap; color: #333; line-height:1.5;}
</style>
"""

def export_txt(history):
    txt = "".join(f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1))
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio

def teaching_answer(q: str) -> str:
    return generate_response(q, temperature=0.3, max_tokens=1024)

def math_answer(q: str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nMath Problem: {q}"
    return generate_response(prompt, temperature=0.1, max_tokens=1024)

def run_ai_teaching_assistant():
    st.title(" AI Teaching Assistant")
    st.session_state.setdefault("history_ata", [])
    c1, c2 = st.columns([1, 2])
    if c1.button("/ Clear", key="c_ata"): st.session_state.history_ata = []; st.rerun()
    if st.session_state.history_ata:
        c2.download_button("Export", export_txt(st.session_state.history_ata), "AI_teaching_Assistant_Conversation.txt", "text/plain")
    q=st.text_input("Enter your question: ", key="q_ata")
    if st.button("Ask", key="a_ata"):
        if not q.strip(): st.warning("Enter a question.")
    else:
        with st.spinner("Thinking..."):
            st.session_state.history_ata.append({"question": q.strip(), "answer": teaching_answer(q.strip())})
        st.rerun()
    
    if not st.session_state.history_ata: return
    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    html = '<div class="wrap">'
    for i, qa in enumerate(st.session_state.history_ata, 1):
        html += f'<div class="card"><div class="q">Q{i}: {qa['question']}</div><div class="a">{qa["answer"]}</div></div>'
    st.markdown(html + "</div>", unsafe_allow_html=True)

def run_math_mastermind():
    st.write()