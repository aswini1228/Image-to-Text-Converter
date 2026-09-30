#  AI Attention Visualizer

An AI-based application that extracts text from an image using OCR and visualizes word-level attention using an attention mechanism.

##  Features

- Upload an image
- Extract text using OCR
- Process extracted words
- Generate word embeddings
- Calculate attention scores
- Visualize attention using progress bars
- Identify the highest-attention word

##  Workflow

Image
↓
OCR
↓
Extracted Text
↓
Word Processing
↓
Word Embeddings
↓
Attention Mechanism
↓
Softmax
↓
Attention Scores
↓
Visualization

##  Technologies

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- Pillow
- NumPy

##  Attention Mechanism

The application calculates similarity between each word embedding and the overall query representation.

The scores are converted into normalized attention weights using Softmax.

### Softmax Formula

Attention Weight:

e^score / Σ e^score

##  Application

This project demonstrates how attention mechanisms can be used to identify important words from text extracted from images.

##  Author

Aswini S
B.Sc Computer Science with Artificial Intelligence
