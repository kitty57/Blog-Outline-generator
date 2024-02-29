import streamlit as st
import streamlit as st
import google.generativeai as genai
import textwrap
import random
import streamlit.components.v1 as components

genai.configure(api_key="AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc")
model = genai.GenerativeModel(model_name="gemini-pro")
def generate_blog_outline(topic):
    human_prompt = f"'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'"
    response = model.generate_content(human_prompt)
    return response.text

def create_collapsible_section(title, content):
    return """
    <details>
        <summary>{}</summary>
        <p>{}</p>
    </details>
    """.format(title, content)
    
st.title("Generate Blog Outline")
topic = st.text_input("Enter the topic you want to generate a blog outline about:")
if st.button("Generate Outline"):
    if topic:
        outline = generate_blog_outline(topic)
        st.markdown("**Generated Outline:**")
        st.write(outline)

        random_topics = ["Artificial Intelligence", "Space Exploration", "Healthy Eating", "Cryptocurrency", "Climate Change"]
        random_topic = random.choice(random_topics)
        st.markdown(f"**Random Topic Suggestion:** {random_topic}")

        st.markdown("**Collapsible Sections:**")
        for i, paragraph in enumerate(outline.split("\n\n")):
            st.markdown(create_collapsible_section(f"Paragraph {i+1}", paragraph), unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic.")

