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

print(json.dumps(json_data,indent=4))