from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_respone(image):
    response=model.generate_content(["Caption this image",image], 
                                    generation_config=genai.types.GenerationConfig(
                    temperature=1.1
                )) # input -> describe what you want to do with the image
    return response.text

st.set_page_config(page_title="Image Caption Generator")

st.header("Generate a caption for your Image")

# input=st.text_input("What do you want to do with the image?", key="input")

uploaded_file=st.file_uploader("Upload an image..", type=['jpg','jpeg','png'])

image=""

if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit=st.button("Generate")

if submit:
    response=get_gemini_respone(image)
    # st.subheader("Here's what I think...")
    st.write(response)
