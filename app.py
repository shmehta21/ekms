import streamlit as st
import os
from ekms.generative import llm_adapter, prompts, storage

st.set_page_config(page_title="Generative EKMS", layout="wide")

st.title("Generative EKMS")
st.caption("Stage 1 - Generate summaries, explanations, and checklists from documents.")

#Upload or paste content
uploaded_file = st.file_uploader("Upload a document", type=["txt", "md"])
text_input = st.text_area("...or paste text here", height=200)

#Prompt preset
preset = st.selectbox("Choose a preset",
                      ["Executive Summary", "New-hire explanation", "Compliance Checklist"]
                      )
temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7)
max_tokens = st.slider("Max Tokens", 100, 2000, 500)

if st.button("Generate"):
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
    else:
        content = text_input


    if not content.strip():
        st.error("Please provide content")
    else:
        st.info("Generating...")
        prompt_text = prompts.build_prompt(preset, content)
        output = llm_adapter.generate(prompt_text, temperature, max_tokens)

        st.subheader("Generated Output")
        st.write(output)

        storage.save_generated(preset, content, output)
        st.success("Saved to local storage.")

# Show saved history
st.subheader("History")        
for item in storage.get_history():
    with st.expander(f"{item['preset']} – {item['timestamp']}"):
        st.markdown(f"**Input:**\n```\n{item['input']}\n```")
        st.markdown(f"**Output:**\n```\n{item['output']}\n```")




