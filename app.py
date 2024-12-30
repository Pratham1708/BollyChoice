import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Load the Bollywood movie dataset
@st.cache_data  # Updated caching method
def load_data():
    try:
        file_path = 'datasets/IMDB-Movie-Dataset(2023-1951).csv'  # Update with the correct file path
        movies_df = pd.read_csv(file_path)
        movies_df = movies_df[~movies_df['movie_name'].str.startswith('Untitled')]  # Remove movies starting with "Untitled"
        movies_df['combined_features'] = movies_df['genre'] + ' ' + movies_df['director'] + ' ' + movies_df['cast']
        return movies_df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

movies_df = load_data()

# Content-Based Filtering: Cosine Similarity on combined features
@st.cache_data
def calculate_cosine_similarity(df):
    try:
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['combined_features'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return cosine_sim
    except Exception as e:
        st.error(f"Error calculating cosine similarity: {e}")
        return None

cosine_sim = calculate_cosine_similarity(movies_df)

# Cosine Similarity based on the cast (actors only)
@st.cache_data
def calculate_actor_similarity(df):
    try:
        actor_tfidf = TfidfVectorizer(stop_words='english')
        actor_tfidf_matrix = actor_tfidf.fit_transform(df['cast'])
        actor_cosine_sim = cosine_similarity(actor_tfidf_matrix, actor_tfidf_matrix)
        return actor_cosine_sim
    except Exception as e:
        st.error(f"Error calculating actor similarity: {e}")
        return None

actor_cosine_sim = calculate_actor_similarity(movies_df)

# Get recommendations based on content similarity
def get_content_based_recommendations(title, top_n=5):
    try:
        idx = movies_df[movies_df['movie_name'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]
        return movies_df['movie_name'].iloc[movie_indices].tolist()
    except Exception as e:
        st.error(f"Error fetching content-based recommendations: {e}")
        return []

# Get recommendations based on actor similarity
def get_actor_based_recommendations(title, top_n=5):
    try:
        idx = movies_df[movies_df['movie_name'] == title].index[0]
        actor_sim_scores = list(enumerate(actor_cosine_sim[idx]))
        actor_sim_scores = sorted(actor_sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        movie_indices = [i[0] for i in actor_sim_scores]
        return movies_df['movie_name'].iloc[movie_indices].tolist()
    except Exception as e:
        st.error(f"Error fetching actor-based recommendations: {e}")
        return []

# Filter movies by genre
def filter_movies_by_genre(df, genre):
    genre_filtered_df = df[df['genre'].str.contains(genre, case=False, na=False)]
    return genre_filtered_df

# Streamlit frontend layout with enhanced UI
def app_layout():
    st.markdown(
        """
        <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .stButton button {
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🎬 BollyChoice - Bollywood Movie Recommender")
    st.write(
        """
        Welcome to BollyChoice, your personalized Bollywood movie recommender!
        Whether you're looking for films similar to your favorites or discovering new ones based on the same actors or content,
        BollyChoice has you covered. Select a genre, choose a movie, and get tailored recommendations based on actor similarity or content features.
        With an easy-to-use interface and fast recommendations, explore the best of Bollywood like never before!
        """
    )

    # Genre-based filtering section
    st.subheader("📂 Explore Movies by Genre")
    unique_genres = set(genre.strip() for sublist in movies_df['genre'].dropna().str.split(',').tolist() for genre in sublist)
    selected_genre = st.selectbox("Select a genre to explore movies", sorted(unique_genres))

    # Initialize session_state for genre and movie selection
    if 'filtered_movie_list' not in st.session_state:
        st.session_state['filtered_movie_list'] = movies_df['movie_name'].tolist()

    # Filter movies by genre and update the movie list
    if st.button("Filter by Genre"):
        with st.spinner(f"Filtering movies in '{selected_genre}' genre..."):
            time.sleep(1)  # Simulate delay
            genre_filtered_df = filter_movies_by_genre(movies_df, selected_genre)

        if not genre_filtered_df.empty:
            st.session_state['filtered_movie_list'] = genre_filtered_df['movie_name'].tolist()

        else:
            st.warning("No movies found for the selected genre.")

    # Show the movie dropdown with filtered movies
    selected_movie = st.selectbox("Choose a movie", st.session_state['filtered_movie_list'])

    # Show recommendations based on the selected movie
    if st.button("Get Recommendations"):
        with st.spinner("Loading recommendations..."):  # Add a loading spinner
            time.sleep(2)  # Simulate a 2-second delay
            actor_recommendations = get_actor_based_recommendations(selected_movie, top_n=5)
            content_recommendations = get_content_based_recommendations(selected_movie, top_n=5)

        # Display selected movie description and actors
        selected_movie_info = movies_df[movies_df['movie_name'] == selected_movie].iloc[0]
        st.subheader(f"**Selected Movie: {selected_movie_info['movie_name']}**")
        st.write(f"**Genre:** {selected_movie_info['genre']}")
        st.write(f"**Director:** {selected_movie_info['director']}")
        st.write(f"**Cast:** {selected_movie_info['cast']}")
        st.write(f"**Description:** {selected_movie_info.get('overview', 'No description available.')}")

        if not actor_recommendations and not content_recommendations:
            st.warning("No recommendations available for this movie.")
        else:
            col1, col2 = st.columns(2)  # Create two columns

            # Actor-based recommendations
            with col1:
                st.subheader(f"Top 5 Actor-based Recommendations for {selected_movie}:")
                for movie in actor_recommendations:
                    st.write(f"**{movie}**")

            # Content-based recommendations
            with col2:
                st.subheader(f"Top 5 Content-based Recommendations for {selected_movie}:")
                for movie in content_recommendations:
                    st.write(f"**{movie}**")

if __name__ == '__main__':
    app_layout()
