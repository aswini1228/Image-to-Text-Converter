#  AI Text Insight Visualizer

An AI-powered application that extracts text from uploaded images using OCR and analyzes word-level importance using an attention mechanism.

##  Live Application

https://ai-text-insight-visualizer.streamlit.app/

## Features

-  Upload an image containing text
-  Extract text using OCR
-  Process extracted words
-  Generate word embeddings
-  Calculate word-level attention scores
-  Visualize attention scores using progress bars
-  Identify the highest-attention word

##  Workflow

Image Upload  
↓  
OCR Text Extraction  
↓  
Word Processing  
↓  
Word Embeddings  
↓  
Attention Mechanism  
↓  
Softmax  
↓  
Attention Score Visualization  
↓  
Highest Attention Word

##  Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- Pillow
- NumPy

##  Attention Mechanism

The application generates numerical representations for extracted words and calculates their similarity with an overall query representation.

The resulting scores are normalized using the **Softmax function** to obtain attention weights.

### Softmax Formula

\[
Attention\ Weight_i =
\frac{e^{score_i}}
{\sum_j e^{score_j}}
\]

##  Objective

The main objective of this project is to demonstrate how OCR, word embeddings, and attention mechanisms can be combined to analyze and visualize important words from text extracted from images.

##  Use Case

This application can be used to analyze text from documents, interview-related content, educational materials, and other image-based text sources.

##  Author

**Aswini S**  
B.Sc Computer Science with Artificial Intelligence

