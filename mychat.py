import google.generativeai as genai
import streamlit as st


GOOGLE_API_KEY = "AIzaSyCWNDbhBTB6p6WxD1Bqvvz93Dxj8EoVJj8"

genai.configure(api_key=GOOGLE_API_KEY)

# Model initiation
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)  # Updated method name
    return response.text

# Streamlit UI
st.title("Simple Chatbot")
st.write("This chatbot uses the Gemini API key from Google Generative AI.")

# Get user input
user_input = st.text_input("Enter Your Prompt:")

# Generate and display output when the user provides input
if user_input:
    output = getResponseFromModel(user_input)
    st.write("Response:")
    st.write(output)

print(output)







    


