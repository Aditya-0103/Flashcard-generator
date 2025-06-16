import streamlit as st
import json
import pandas as pd
from file_parser import extract_text_from_pdf
from flashcard_gen import generate_flashcards
from utils import parse_flashcards

st.title("📚 LLM-Powered Flashcard Generator")

input_method = st.radio("Input Method", ["Paste Text", "Upload PDF"])
subject = st.selectbox("Subject Type (optional)", ["General", "Biology", "History", "CS", "Math", "Custom"])

user_text = ""

if input_method == "Paste Text":
    user_text = st.text_area("Paste your study content here")
else:
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        user_text = extract_text_from_pdf(uploaded_file)

if st.button("Generate Flashcards"):
    if not user_text.strip():
        st.warning("Please enter or upload some content first.")
    else:
        with st.spinner("Generating flashcards..."):
            raw_output = generate_flashcards(user_text, subject)
            flashcards = raw_output

        if flashcards:
            st.success(f"✅ Generated {len(flashcards)} flashcards!")

            for i, card in enumerate(flashcards, 1):
                st.markdown(f"**Q{i}:** {card['question']}")
                st.markdown(f"*A{i}:* {card['answer']}")
                st.markdown("---")

            # Move export code INSIDE the block
            csv_data = pd.DataFrame(flashcards).to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download as CSV", data=csv_data, file_name="flashcards.csv", mime="text/csv")

            json_data = json.dumps(flashcards, indent=2)
            st.download_button("📥 Download as JSON", data=json_data, file_name="flashcards.json", mime="application/json")
        else:
            st.error("❌ No flashcards were generated.")
