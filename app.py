import streamlit as st
import pickle
import pandas as pd

# Set up the web page title
st.title('Movie Recommender System')

# 1. Load the exported pickle files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Define the recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Get top 5 matches
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# 3. Create the UI Dropdown selector
selected_movie_name = st.selectbox(
    'Type or select a movie to get recommendations:',
    movies['title'].values
)

# 4. Trigger recommendations when button is clicked
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("### You might also like:")
    for movie in recommendations:
        st.write(f"- {movie}")