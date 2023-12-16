# flashcards.py

# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    total = len(data["cards"])
    score = 0
    print(data)

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess == i["a"]:
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")
    ...

    if guess.lower() == i["a"].lower():