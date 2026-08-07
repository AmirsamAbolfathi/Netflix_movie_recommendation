import base64
import pandas as pd
import pickle as pk
import streamlit as st
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

######################################   import model   ############################################################

with open("model.pkl", "rb") as file:
    model = pk.load(file)

data = pd.read_pickle("Netflix_TV_Shows_and_Movies.pkl")

data_text = (
    data["title"] + " " + data["type"] + " "
    + data["release_year"].astype(str) + " " + data["age_certification"]
).str.lower()

data_number = model.transform(data_text)

######################################      icon      ############################################################

page_icon = Image.open("icon.webp")
st.set_page_config(page_title="Netflix Movie & Show Recommender", page_icon=page_icon, layout="centered")

######################################   background   ####################################################

with open("background.webp", "rb") as file:
    encoded = base64.b64encode(file.read()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.55);
        z-index: -1;
    }}
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(20, 20, 20, 0.45);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    [data-testid="stMainBlockContainer"] {{
        background: rgba(0, 0, 0, 0.35);
        backdrop-filter: blur(2px);
        -webkit-backdrop-filter: blur(2px);
        border-radius: 14px;
        padding: 2rem;
        min-height: 100vh;
    }}
    [data-testid="stAppViewBlockContainer"] {{
        min-height: 100vh;
    }}
    h1, h3, p, span, label {{
        color: #ffffff !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

######################################    body    #######################################################

logo_col, title_col = st.columns([1, 5])
with logo_col:
    st.image(page_icon, width=80)
with title_col:
    st.title("Netflix Movie & Show Recommender")

col1, col2 = st.columns([3, 1])
with col1:
    user_text_input = st.text_area(
        "Describe what you're in the mood for, and I'll suggest the best matches.",
          value="", height=100,placeholder="e.g. an exciting war movie"
    )
with col2:
    top_n = st.slider("Number of results", min_value=1, max_value=10, value=5)

content_type = st.radio("Content type", ["All", "Movies", "Shows"], horizontal=True)

######################################   button   ########################################################

if st.button("Get Recommendations 🔍", type="primary"):
    if user_text_input.strip() == "":
        st.warning("Please enter a description.")
    else:
        with st.spinner("Searching..."):
            user_data_number = model.transform([user_text_input.lower()])
            similarity = cosine_similarity(user_data_number, data_number).flatten()

            filtered_data = data.copy()
            filtered_data["similarity"] = similarity

            if content_type == "Movies":
                filtered_data = filtered_data[filtered_data["type"] == "MOVIE"]
            elif content_type == "Shows":
                filtered_data = filtered_data[filtered_data["type"] == "SHOW"]

            results = filtered_data.sort_values("similarity", ascending=False).head(top_n)

        if results.empty or results["similarity"].max() == 0:
            st.info("No matches found. Try a different description.")
        else:
            st.subheader("Recommended for you:")
            for _, row in results.iterrows():
                with st.container(border=True):
                    st.markdown(f"### {row['title']}")
                    meta = f"📅 {row['release_year']}  |  🎞️ {row['type']}"
                    score = row.get("imdb_score", None)
                    if pd.notna(score) and str(score).strip() != "":
                        meta += f"  |  ⭐ {score}"
                    st.caption(meta)
                    st.write(row["description"])
