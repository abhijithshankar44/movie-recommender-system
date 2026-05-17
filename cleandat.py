import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your dataset
df = pd.read_csv(r'C:\Users\abhij\Downloads\final_dataset.zip')
df['tags'] = df['tags'].fillna('')

# NO stop_words parameter needed here!
# Just limit your max_features to keep the matrix size optimal.
cv = CountVectorizer(max_features=5000)
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)
# 5. Create the recommendation function


def recommend(movie):
    try:
        # Find the index of the movie in the dataframe
        movie_index = df[df['title'] == movie].index[0]
        
        # Get the similarity scores for that movie
        distances = similarity[movie_index]
        
        # Sort the scores in descending order (ignoring the first one which is the movie itself)
        # enumerate helps us keep track of the original index while sorting
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        print(f"Movies similar to '{movie}':\n")
        for i in movies_list:
            # i[0] is the index of the similar movie
            print(df.iloc[i[0]].title)
            
    except IndexError:
        print("Movie not found in the dataset. Please check the spelling.")

# Let's test it!
recommend('Toy Story')

# Save the movies dataframe as a dictionary (easier to load as a dataframe later)
pickle.dump(df.to_dict(), open('movie_dict.pkl', 'wb'))

# Save the similarity matrix 
pickle.dump(similarity, open('similarity.pkl', 'wb'))