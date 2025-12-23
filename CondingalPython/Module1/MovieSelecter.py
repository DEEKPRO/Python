import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import *
from colorama import init, Fore
import time
import sys
import kagglehub

# Download latest version
path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")

print("Path to dataset files:", path)
init(autoreset=True)

def load_data(file_path=path):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))
genres = list_genres(movies_df)

def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case= False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]
    
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0) and polarity > 0)) or not mood:
            recommendations.append(())
        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive😁" if polarity > 0 else "Negative😔" if polarity < 0 else "Neutral😐"
        print(f"{Fore.CYAN}{idx}.🎥 {title} (Polarity: {polarity:.2f}, {sentiment})")

def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")

    print(Fore.GREEN + "Available Genres: ", end="")
    for idx,  genre in enumerate(genres, 1):
        print()