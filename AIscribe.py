import streamlit as st
import openai

# Authenticate with OpenAI
openai.api_key = "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"

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

    # Generate the blog post
    if st.button("Generate"):
        # Construct the prompt
        full_prompt = f"{prompt} {option}\n\nTitle: {title}\n\nIntroduction: {intro}\n\nBody: {body}\n\nConclusion: {conclusion}"

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
