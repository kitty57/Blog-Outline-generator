import streamlit as st
import streamlit as st
import google.generativeai as genai
import textwrap

genai.configure(api_key="AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc")
model = genai.GenerativeModel(model_name="gemini-pro")
def generate_blog_outline(topic):
    human_prompt = f"'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'"
    response = model.generate_content(human_prompt)
    return response.text

# Define Streamlit UI
st.title("Generate Blog Outline")
topic = st.text_input("Enter the topic you want to generate a blog outline about:")
if st.button("Generate Outline"):
    if topic:
        outline = generate_blog_outline(topic)
        st.markdown(outline)
    else:
        st.warning("Please enter a topic.")

