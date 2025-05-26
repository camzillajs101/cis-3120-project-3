# cis-3120-project-3
Project #3 for CIS 3120, spring 2025. Idea: Virtual Book Club — Pull book data from an API like Open Library; based on selected genre, have AI generate a book summary and discussion questions.

## Project Requirements
* External data collection (OpenLibraryAPI)
* Generative AI imagination (Ollama)
* Gradio App
* Version control

## Our Project
#### Completed by Camilo Mason and Robert Emicente

[GitHub Repository](https://github.com/camzillajs101/cis-3120-project-3/)

### Setup & Use

To launch the Gradio project, please run the `virtual_book_club.py` file:
```
$ python virtual_book_club.py
```
Or visit the [public link](https://1dcda3a26e09d02844.gradio.live/).

Once in the Gradio interface, select a genre from the dropdown and hit "Submit" to get a random book from that genre, a summary, and a list of potential discussion questions.

The Python program will first pick a book at random through a genre listing, and then use the book's title, author, and list of related topics to generate the summary and questions using Ollama's tinyllama LLM.