import requests
import json
import gradio as gr
import random

"""
GENRE LISTING:
- Fantasy 			 	-> fiction_fantasy_general
- Science fiction    	-> fiction_science_fiction_general
- Mystery 			 	-> fiction_mystery_&_detective_general
- Thriller 			 	-> fiction_thrillers_general
- Romance 			 	-> fiction_romance_general
- Biography 		 	-> biography
- Historical fiction 	-> fiction_historical_general
- Horror 			 	-> fiction_horror
- Adventure 		 	-> fiction_action_&_adventure
- Dystopian 		 	-> fiction_dystopian
"""

genres = {
	"fantasy": "fiction_fantasy_general",
	"science fiction": "fiction_science_fiction_general",
	"mystery": "fiction_mystery_&_detective_general",
	"thriller": "fiction_thrillers_general",
	"romance": "fiction_romance_general",
	"biography": "biography",
	"historical fiction": "fiction_historical_general",
	"horror": "fiction_horror",
	"adventure": "fiction_action_&_adventure",
	"dystopian": "fiction_dystopian"
}

url = "https://www.openlibrary.org/subjects/"
genre = "historical fiction"

response = requests.get(url + genres[genre] + ".json")
json_data = response.json()

index = random.randint(0,10) # don't select the first book every time; random choice of top ten results

work = json_data["works"][index]

# print(json.dumps(work,indent=4))

"""
Prompt construction:

You are an assistant that generates brief, thoughtful summaries of books based on their title and a list of subjects.
Do not make up plot details or specific events. Use the title and subject tags to infer the general themes, tone, and likely type of story.
Your goal is to write a 2–3 sentence summary that captures what someone might expect from reading this book, based on those elements alone.

Generate a 2-3 sentence summary of a book and 2-3 relevant discussion questions for a book club using the following information:

Title: [book title]
Subjects: [list of book subjects, comma-delimited]
"""

title = work["title"]
subjects = ', '.join(work["subject"][:20]) # limit to first 20 listed subjects

print(f"Title: {title}\nSubjects: {subjects}")