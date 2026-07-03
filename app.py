import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AQ.Ab8RN6LTyH29Gs9Noqt9t4lfN9elwxkJSLB8mpfCPvWfQpDeaQ"])


model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎓 AI Learning Buddy Shreya")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    (
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    )
)

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} simply."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic}."

        else:
            prompt = topic

        response = model.generate_content(prompt)

        st.write(response.text)
