# import streamlit as st
# import pickle
# import pandas as pd

# st.title('Movie Recommender System')

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

#     recommended_movies = []
#     for i in movie_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
# similarity = pickle.load(open('similarity.pkl','rb'))

# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)


# option = st.selectbox(
#     "SELECT MOVIE", movies['title'].values)

# if st.button('Recommend'):
#     recommendations = recommend(option)
#     for i in recommendations:
#         st.write(i)


import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ---------------- DOWNLOAD FILES ---------------- #

def download_file(url, filename):
    if not os.path.exists(filename):
        response = requests.get(url, stream=True)
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

# Google Drive direct links
movie_url = "https://drive.google.com/uc?id=1aLBRrw6IrniFXVZ11UOx92DYcbuqiIql"
similarity_url = "https://drive.google.com/uc?id=1XNYtGIDlIsodfOk0CgV40T-KrDDygodA"

# Download files
download_file(movie_url, "movie.pkl")
download_file(similarity_url, "similarity.pkl")

# ---------------- LOAD DATA ---------------- #

movies_dict = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

# ---------------- UI ---------------- #

st.title('🎬 Movie Recommender System')

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

selected_movie = st.selectbox(
    "SELECT MOVIE",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)