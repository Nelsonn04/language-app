# Find the cards due today and quiz you one at a time: show the Spanish word, 
# let you think, reveal the answer, then ask "Did you know it? (y/n)".
# Update each card: if right, move it up a box; if wrong, back to Box 1. Update the timestamp and save.
# Persist everything so that closing and reopening the app keeps your progress.
# Keep BOX_INTERVALS as a constant at the top of the file.
import json

# Opens the JSON file with all the flashcard information and loads it
with open("flashcards.json", "r", encoding="utf-8") as file:
    flashcards = json.load(file)
study_set = []
for card in flashcards:
    if card["last_reviewed"] is None:
        study_set.append(card)


def cards_due():
    print(study_set)

cards_due()