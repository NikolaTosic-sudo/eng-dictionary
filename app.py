import json
from difflib import get_close_matches
import tkinter as tk

data = json.load(open("./data.json"))

def translate():
    word = word_value1.get()

    translation.delete('1.0', tk.END)

    wordLower = word.lower()

    if wordLower in data:
        if type(data[wordLower]) == list:
            for item in data[wordLower]:
                word1.delete('0', tk.END)
                translation.insert(tk.END, item)
                translation.insert(tk.END, '\n')
        else:
            return data[wordLower]

    elif get_close_matches(wordLower, data.keys(), cutoff=0.8):

        word = get_close_matches(wordLower, data.keys(), cutoff=0.8)[0]

        item = (f"Did you mean {word}? Enter above Y if yes, or N if no: ")

        translation.insert(tk.END, item)

        word_value2 = tk.StringVar()
        word2 = tk.Entry(window, textvariable=word_value2)
        word2.config(width=10)
        word2.grid(row=1, column=4)

        def tryagain():
            yn = word_value2.get()

            if yn.lower() == "y":
                translation.delete('1.0', tk.END)
                if type(data[word]) == list:
                    for item2 in data[word]:
              #          word1.delete('0', tk.END)
                        translation.insert(tk.END, item2)
                        translation.insert(tk.END, '\n')
                        word2.destroy()
                        btn2.destroy()
                else:
                    word2.destroy()
                    btn2.destroy()
                    return data[word]

            elif yn.lower() == "n":
                word1.delete('0', tk.END)
                translation.delete('1.0', tk.END)
                translation.insert(tk.END, "Sorry, try again.")
                word2.destroy()
                btn2.destroy()

        btn2 = tk.Button(window, text="Try Again", command=tryagain)
        btn2.grid(row=1, column=7)

    else:
        translation.insert(tk.END, "Word does not exists. Please double check it")


window = tk.Tk()

window.title("Translator")

word_value1 = tk.StringVar()
word1 = tk.Entry(window, textvariable = word_value1)
word1.grid(row=1, column=4)
word1.config(width=40)
label1 = tk.Label(window, text="Enter a word you want to translate")
label1.grid(row=1, column=3)

btn = tk.Button(window, text="Translate", command=translate)
btn.grid(row=1, column=7)

translation = tk.Text(window)
translation.grid(row=4, columnspan=8)


window.mainloop()