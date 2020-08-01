import json
from difflib import get_close_matches

data = json.load(open("./data.json"))

def translate(word):
    wordLower = word.lower()

    if wordLower in data:
        return data[wordLower]
    elif get_close_matches(wordLower, data.keys(), cutoff=0.8):
        word = get_close_matches(wordLower, data.keys(), cutoff=0.8)[0]
        yn = input(f"Did you mean {word}? Enter Y if yes, or N if no: ")
        if yn.lower() == "y":
            return data[word]
        return "Sorry, try again."
    else:
        return "Word does not exists. Please double check it"

word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)