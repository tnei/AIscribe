import streamlit as st
import openai

# Authenticate with OpenAI
openai.api_key = "YOUR_API_KEY_HERE"

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
            full_prompt += f" *{body}*"
        else:
            full_prompt += f" {body}"
        full_prompt += f"\n\nConclusion:"
        if bullets_conclusion:
            full_prompt += f"\n- {conclusion}"
        else:
            full_prompt += f" {conclusion}"

        # Generate the blog post
        response = openai.Completion.create(
            engine="davinci",
            prompt=full_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )

        # Display the blog post
        st.write(response.choices[0].text)

if __name__ == "__main__":
    app()
