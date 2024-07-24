import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # Start a camera
    camera_image = st.camera_input("Camera")

if camera_image: 
    # Check the image file
    print(camera_image)

    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert to grayscale
    gray_image = img.convert("L")

    # Render the grayscale
    st.image(gray_image)