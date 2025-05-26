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
OLLAMA = "http://localhost:11434/api/generate" # Ollama API endpoint

def recommend_books(genre_preference=None):
	if genre_preference.lower() not in genres:
		return "Sorry, we currently don't have any recommendations for that genre."

	response = requests.get(url + genres[genre_preference.lower()] + ".json") # Search OpenLibraryAPI for genre

	if response.status_code != 200:
		return "API error"

	json_data = response.json()

	work = random.choice(json_data["works"]) # don't select the first book every time; random choice of top results

	title = work["title"]
	subjects = ', '.join(work["subject"][:20]) # limit to first 20 listed subjects for relevancy
	author = work["authors"][0]["name"]

	aftprompt = f"Title: {title}\nAuthor: {author}\nSubjects: {subjects}"

	s_prompt = f"Generate a short summary of a book using the following information about the book:\n\n{aftprompt}"
	q_prompt = f"Generate 2-3 discussion questions using the following information about a book:\n\n{aftprompt}"

	payload = {
		"model": "tinyllama",
		"prompt": s_prompt,
		"stream": False
	}

	try:
		s_response = requests.post(OLLAMA,json=payload)
		payload["prompt"] = q_prompt
		q_response = requests.post(OLLAMA,json=payload)

		if s_response.status_code == 200 and q_response.status_code == 200:
			return f"📚 Recommended book for genre {genre_preference}:\n\n{title} by {author}.\n\nSummary: {s_response.json()["response"]}\n\nDiscussion questions:\n{q_response.json()["response"]}"
		else:
			return "Error"
	except Exception as e:
		return e

# Create the interface
demo = gr.Interface(
    fn=recommend_books,
    inputs=[
        gr.Dropdown(["Fantasy","Science fiction","Mystery","Thriller","Romance","Biography","Historical fiction","Horror","Adventure","Dystopian"])
    ],
    outputs=[
        gr.Textbox(label="📚 Book Recommendations")
    ],
    title="Recommended Books by Genre",
    description="Get book recommendations based on the genre you like"
)

if __name__ == "__main__":
	demo.launch(share=True)