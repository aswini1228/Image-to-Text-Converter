import streamlit as st
from PIL import Image
from preprocessing import preprocess_image
from ocr import extract_text

st.set_page_config(
    page_title="Image to Text Converter",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Image to Text Converter")
st.write("Upload a PNG image and extract the text using OCR.")

uploaded_file = st.file_uploader(
    "Upload your PNG image",
    type=["png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Image")
    st.image(image, use_container_width=True)

    if st.button("🔍 Extract Text"):

        processed_image = preprocess_image(image)

        extracted_text = extract_text(processed_image)

        st.subheader("📝 Extracted Text")

        if extracted_text.strip():

            st.text_area(
                "Recognized Text",
                extracted_text,
                height=300
            )

            st.download_button(
                label="📥 Download Text",
                data=extracted_text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )

        else:
            st.warning("No text found in the image.")
