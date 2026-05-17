# Movie Recommender System 🎬

A content-based movie recommendation engine built using Natural Language Processing (NLP) and deployed as an interactive web application.

## 🚀 Project Overview
This system recommends 5 similar movies based on user selection. It analyzes a dataset of 9,000+ movies, combining text attributes like genres, keywords, cast, and crew into a centralized `tags` feature.

## 🛠️ Tech Stack & Concepts
- **Frontend UI:** Streamlit
- **Data Manipulation:** Pandas, NumPy
- **NLP Vectorization:** Scikit-Learn (`CountVectorizer` / Bag of Words)
- **Mathematical Matching:** Cosine Similarity

## 🏃 How to Run Locally

1. Clone this repository or download the files.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt

Follow these steps to set up the project on your machine:

### 1. Clone the Repository
Download or clone this folder to your computer and navigate into it using your terminal:
```bash
cd movie-recommender-system
```
### 2. Install Dependencies
Install all required libraries automatically using pip:
```bash
pip install -r requirements.txt
```
### 3. Add the Dataset
Place your compressed dataset file (final_dataset.zip) inside your computer's Downloads folder, or update the file path inside cleandat.py to point to its location.

### 4. Generate the Model Files (Pickles)
Run the data cleaning script to process the text data and generate your local similarity matrices:
```bash
python cleandat.py
```
### 5. Launch the Web App
Start the Streamlit application server:
```bash
python -m streamlit run app.py

