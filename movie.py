import pandas as pd
import spacy
nlp = spacy.load('en_core_web_md')

# Opening the txt file and separating the lines (each movie is on a new line)
with open('movies.txt', 'r') as file:
     lines = file.readlines()

# Empty dictionary to store the movie titles and descriptions.
     
film_dict = {}
# Loops through the lines and splits the movie title and description as keys and items.
for line in lines: 
    key, value = line.split(':') 
    film_dict[key.strip()] = value.strip() # Stores them in the empty dictionary.

# print(film_dict)


query = """Will he save their world or destroy it? When the Hulk becomes too danergous for Earth, the
Illuminati trick Hulk into a shuttle and launch him into space to a planet where the hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
# The description of the movie that has been watched by the user.
query_doc = nlp(query)

scores = {} # Creating an empty dictionary to store the similarity scores.

# print(movies)

# Tokenising each description and find similarity
for movies, description in film_dict.items():
    movie_doc = nlp(description)
    similarity = query_doc.similarity(movie_doc)
    scores[movies] = round(similarity, 4)
        
recommendation = max(scores,key=scores.get)
# Highest similarity score is the next recommended movie for the user to watch.
        
print(f"Recommended Movie: {recommendation}")