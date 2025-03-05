import streamlit as st
from openai import OpenAI
import json
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set up OpenAI API key
openai_client = OpenAI()


# App Title
st.title("Email Generator for Customer Success Managers")
st.subheader("Generate professional, helpful replies in seconds!")

# Input Fields
sender_email = st.text_area("Sender's Email", placeholder="Paste the sender's email here...")
user_draft = st.text_area("Your Draft or Notes", placeholder="Write your ideas or key points here...")
keywords = st.text_input("Additional Keywords or Phrases", placeholder="Add specific words you'd like to include...")

# Tone Selection (Optional)
tone = st.selectbox("Tone of the Response", ["Helpful", "Professional", "Friendly", "Sender's"], index=1)
if tone == "Sender's":
    tone = "match the tone of the senders"
else:
    tone = f"be {tone.lower()}"

generated_email = None

# Generate Email Button
if st.button("Generate Email"):
    if sender_email.strip() and user_draft.strip():
        with st.spinner("Generating your email..."):
            # Call OpenAI GPT model using the OpenAI class
            messages = [
                {"role": "developer", "content": f"You are a helpful and professional email assistant."},
                {"role": "user", "content": f"assist me with creating an email draft. i will provide the senders email and a current draft that i have. please review my draft and make changes where necessary. The tone should {tone.lower()}."},
                {"role": "user", "content": f"Sender's Email: {sender_email}"},
                {"role": "user", "content": f"My Email Draft: {user_draft}"},
            ]
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7
            )
            generated_email = response.choices[0].message.content.strip()
            st.text_area("Generated Email", value=generated_email, height=300)
    else:
        st.warning("Please fill in both the sender's email and your draft notes.")

# Save Draft
if "drafts" not in st.session_state:
    st.session_state.drafts = []

if st.button("Save Draft"):
    if sender_email and user_draft:
        draft = {
            "sender_email": sender_email,
            "user_draft": user_draft,
            "keywords": keywords,
            "tone": tone,
            "generated_email": generated_email,
        }
        st.session_state.drafts.append(draft)
        with open("drafts.json", "w") as file:
            json.dump(st.session_state.drafts, file)
        st.success("Draft saved!")
    else:
        st.warning("Generate an email before saving the draft.")

# Load Drafts
if st.button("Load Previous Drafts"):
    try:
        with open("drafts.json", "r") as file:
            drafts = json.load(file)
        st.session_state.drafts = drafts
        st.write("Loaded drafts:")
        for i, draft in enumerate(drafts):
            st.write(f"Draft {i + 1}")
            st.json(draft)
    except FileNotFoundError:
        st.error("No drafts found!")
