import streamlit as st
from PIL import Image

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention


st.set_page_config(
    page_title="AI Text Insight Visualizer",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Text Insight Visualizer")

st.write(
    "Convert image text into words and visualize "
    "word-level attention using an attention mechanism."
)

st.divider()

uploaded_file = st.file_uploader(
    "📷 Upload an Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Image")
    st.image(image, use_container_width=True)

    st.divider()

    # OCR
    extracted_text = extract_text(image)

    st.subheader("📄 Extracted Text")

    if extracted_text.strip():

        st.text_area(
            "OCR Output",
            extracted_text,
            height=200
        )

        st.divider()

        # Word Processing
        words = extracted_text.split()

        st.subheader("🔤 Processed Words")

        st.write(", ".join(words))

        st.success(
            f"Processed {len(words)} words."
        )

        st.divider()

        # Embeddings
        embeddings = create_embeddings(words)

        st.subheader("🔢 Word Embeddings")

        st.write(
            f"Embedding generated for {len(embeddings)} words."
        )

        st.divider()

        # Attention
        attention_scores = calculate_attention(
            embeddings
        )

        st.subheader("🧠 Word Attention")

        # Normalize scores only for visualization
        max_score = max(attention_scores)

        for word, score in zip(
            words,
            attention_scores
        ):

            normalized_score = score / max_score

            st.write(
                f"**{word}** — {score:.3f}"
            )

            st.progress(
                float(normalized_score)
            )

        st.divider()

        # Highest Attention Word
        highest_index = attention_scores.index(
            max(attention_scores)
        )

        highest_word = words[highest_index]

        st.success(
            f"⭐ Highest Attention Word: **{highest_word}**"
        )

    else:

        st.warning(
            "⚠️ No text detected in the image."
        )
