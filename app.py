import streamlit as st 
import pickle
import requests

def fetch_poster(movie_id):
    # Construct the URL for fetching the poster
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=aac1bbc151747d8dca06c090c40cb727"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    
    # Construct the full URL for the poster
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"
# Load the movie list and similarity matrix
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract movie titles
movies_list = movies['title'].values

# Streamlit app header
st.header("Movie Recommender System")

# Movie selection dropdown


import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


    
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]
imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue = st.selectbox("Select movie from dropdown", movies_list)
def recommend(movie):
    # Find the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    
    # Compute the distances from the selected movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    # Get the top 5 recommended movies, skipping the first one (itself)
    recommend_movie = []
    recommend_poster = []
    for i in distances[1:6]:  # Skip the first one as it is the movie itself
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
        
    return recommend_movie, recommend_poster

# Show recommendations on button click
if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    
    # Display the recommended movies in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0], use_column_width=True)
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1], use_column_width=True)
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2], use_column_width=True)
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3], use_column_width=True)
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4], use_column_width=True)
