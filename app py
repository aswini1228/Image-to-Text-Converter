import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(
    page_title="Image to Text Converter",
    page_icon="📝"
)

st.title("📝 Image to Text Converter")
st.write("Upload an image and extract the text using OCR.")

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")
    st.image(image, use_container_width=True)

    if st.button("Extract Text"):

        text = pytesseract.image_to_string(image)

        st.subheader("Extracted Text")

        if text.strip():
            st.text_area(
                "Text",
                text,
                height=300
            )

            st.download_button(
                "Download Text",
                text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )
        else:
            st.warning("No text found in the image.")
