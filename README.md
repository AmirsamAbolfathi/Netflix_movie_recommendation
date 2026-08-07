# 🎬 Netflix Movie & Show Recommender

A content-based recommendation web app that suggests Netflix movies and TV shows based on a natural-language description of what you're in the mood for. Built with **TF-IDF** vectorization and **cosine similarity**, wrapped in a polished **Streamlit** UI with glassmorphism styling.

![Cyber Fenix](https://img.shields.io/badge/Cyber%20Fenix-Lab-red?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square)

---

## ✨ Features

- 🔎 **Natural language search** — describe what you want to watch (e.g. *"an exciting war movie"*) and get relevant matches
- 🎯 **Content-based filtering** — combines title, type, release year, and age certification into a TF-IDF vector space
- 🎛️ **Adjustable results** — slider to control how many recommendations are shown (1–10)
- 🎥 **Filter by type** — narrow results to Movies, Shows, or both
- 🖼️ **Custom UI** — glassmorphism cards, background image, and custom favicon/logo
- ⚡ **Fast & cached** — model and data loaded once via Streamlit for smooth interaction

---

## 🌐 Live App

🔗 **[Try it on Streamlit Cloud](https://netflix-movie-recommendation-cyber-fenix.streamlit.app/)**

## 🧠 How It Works

1. Each title in the dataset is turned into a text string combining its **title, type, release year, and age certification**.
2. A pre-trained **TF-IDF vectorizer** (`model.pkl`) transforms both the dataset and the user's query into numeric vectors.
3. **Cosine similarity** is computed between the user's query vector and every title in the dataset.
4. Results are sorted by similarity score and filtered by content type before being displayed.

---

## 📁 Project Structure

```
├── netflix_movie_recommendation.py     # Main Streamlit app
├── model.pkl                           # Trained TF-IDF vectorizer
├── Netflix_TV_Shows_and_Movies.pkl     # Preprocessed Netflix dataset
├── icon.webp                           # App favicon / logo
├── background.webp                     # App background image
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/AmirsamAbolfathi/netflix-movie-recommender.git
cd netflix-movie-recommender
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run netflix_movie_recommendation.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — web app framework
- **scikit-learn** — TF-IDF vectorization & cosine similarity
- **pandas** — data handling
- **Pillow (PIL)** — image handling for favicon

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Amirsam Abolfathi**
🔗 GitHub: [@AmirsamAbolfathi](https://github.com/AmirsamAbolfathi)
📺 Channel: **Cyber Fenix Lab** — Code. Create. Conquer.
