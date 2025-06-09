# streamlit_app.py
import streamlit as st
from story_generator import generate_story

st.set_page_config(page_title="AI Dungeon Story Generator", layout="centered")

st.title("🧙‍♂️ AI Dungeon Story Generator")

# Prompt input
prompt = st.text_input("Enter a story prompt:", "")

# Genre selection
genre = st.selectbox("Select a genre:", ["Fantasy", "Mystery", "Sci-Fi", "Horror", "Adventure"])

# Number of outputs
num_outputs = st.slider("How many story continuations?", 1, 5, 1)

# Button to generate
if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        full_prompt = f"{genre} Story: {prompt}"
        with st.spinner("Generating story..."):
            try:
                stories = generate_story(full_prompt, num_return_sequences=num_outputs)
                for i, story in enumerate(stories, 1):
                    st.markdown(f"### Story {i}")
                    st.write(story)
                # Save last story to file
                with open("generated_story.txt", "w", encoding="utf-8") as f:
                    f.write(stories[-1])
            except Exception as e:
                st.error(f"Error: {e}")
