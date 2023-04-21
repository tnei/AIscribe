import requests
import streamlit as st
import openai

# Define the prompt
prompt = "Write a blog post on the following topic:"

# Define the options
options = {
    1: "Artificial Intelligence",
    2: "Blockchain Technology",
    3: "Cybersecurity",
    4: "Data Science",
    5: "Internet of Things",
    6: "Quantum Computing"
}

# Define the API endpoint
API_ENDPOINT = "http://localhost:8000/get-api-key"

# Get the API key from the server
response = requests.get(API_ENDPOINT)
if response.status_code == 200:
    api_key = response.json()["api_key"]
else:
    st.error("Failed to retrieve API key.")
    st.stop()

# Authenticate with OpenAI
openai.api_key = api_key

# Define the Streamlit app
def app():
    st.title("Blog Post Generator")

    # Display the options
    option = st.selectbox("Select a topic:", list(options.values()))

    # Get the user input
    title = st.text_input("Title:")
    intro = st.text_area("Introduction:")
    body = st.text_area("Body:")
    conclusion = st.text_area("Conclusion:")

    # Add text formatting options
    bold_intro = st.checkbox("Bold introduction")
    italic_body = st.checkbox("Italic body")
    bullets_conclusion = st.checkbox("Bulleted conclusion")

    # Generate the blog post
    if st.button("Generate"):
        # Construct the prompt
        full_prompt = f"{prompt} {option}\n\nTitle: {title}\n\nIntroduction:"
        if bold_intro:
            full_prompt += f" **{intro}**"
        else:
            full_prompt += f" {intro}"
        full_prompt += f"\n\nBody:"
        if italic_body:
            full_prompt += f" _{body}_"
        else:
            full_prompt += f" {body}"
        full_prompt += f"\n\nConclusion:"
        if bullets_conclusion:
            bullet_points = conclusion.split("\n")
            for bullet_point in bullet_points:
                full_prompt += f"\n- {bullet_point}"
        else:
            full_prompt += f" {conclusion}"

        # Generate the blog post using GPT-3
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=full_prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            post = response.choices[0].text.strip()
            st.success("Blog post generated!")
            st.write(post)
        except Exception as e:
            st.error("Failed to generate blog post.")
            st.error(e)
