import streamlit as st
import google.generativeai as genai
import os
import textwrap
from PIL import Image
import pathlib
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initiate the Model using a Function
def get_response(input, image):
    # Flash can read Images and Extract Information
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!= "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Design the Page
st.header(":blue[Gemini Image to Text] Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Upload an Image...", 
                                 type = ["jpg", "png", "jpeg"])

# Display the Image
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded File", use_container_width=True)
    
# Create the Submit Button
submit = st.button("Magic")

if submit:
    response = get_response(input, image)
    st.subheader("The Response is: ")
    st.write(response)