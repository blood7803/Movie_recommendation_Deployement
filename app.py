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
import gdown
import os

st.write("Starting app...")

def download_file(file_id, filename):
    if not os.path.exists(filename):
        st.write(f"Downloading {filename}...")
        gdown.download(id=file_id, output=filename, quiet=False)

movie_id = "1aLBRrw6IrniFXVZ11UOx92DYcbuqiIql"
similarity_id = "1XNYtGIDlIsodfOk0CgV40T-KrDDygodA"

download_file(movie_id, "movie.pkl")
download_file(similarity_id, "similarity.pkl")

# Check file size
st.write("Movie file size:", os.path.getsize("movie.pkl"))
st.write("Similarity file size:", os.path.getsize("similarity.pkl"))

# Try loading
st.write("Loading pickle files...")

movies_dict = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.write("Files loaded successfully!")

movies = pd.DataFrame(movies_dict)

st.title('🎬 Movie Recommender System')