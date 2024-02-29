import streamlit as st
import random
import google.generativeai as genai
from wordcloud import WordCloud

# Configure GenerativeAI model
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel(model_name="gemini-pro")

# Function to generate blog outline
def generate_blog_outline(topic):
    human_prompt = f"'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'"
    response = model.generate_content(human_prompt)
    return response.text

# Function to create collapsible sections
def create_collapsible_section(title, content):
    return """
    <details>
        <summary style="font-weight:bold">{}</summary>
        <p>{}</p>
    </details>
    """.format(title, content)

st.set_page_config(layout="wide")  
st.title("Blog Outline Generator")
st.sidebar.image("✍🏻", width=200)  
st.sidebar.title("Random Topic Generator")

st.write("")
st.write("")
col1, col2 = st.columns([2, 1])  

with col1:
    topic = st.text_input("Enter the topic you want to generate a blog outline about:")
    if st.button("Generate Outline"):
        if topic:
            outline = generate_blog_outline(topic)
            st.markdown("**Generated Outline:**")
            for i, paragraph in enumerate(outline.split("\n\n")):
                st.markdown(create_collapsible_section(f"Paragraph {i+1}", paragraph), unsafe_allow_html=True)
        else:
            st.warning("Please enter a topic.")

with col2:
    if st.sidebar.button("Generate Random Topic"):
        random_topics = ["Artificial Intelligence", "Space Exploration", "Healthy Eating", "Cryptocurrency", "Climate Change"]
        random_topic = random.choice(random_topics)
        st.sidebar.write(f"Suggested Topic: {random_topic}")

footer = """
<div style="background-color:#f8f9fa;padding:10px;border-radius:5px;text-align:center;">
    <p style="color:#6c757d;">Powered by GenerativeAI and Streamlit</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
