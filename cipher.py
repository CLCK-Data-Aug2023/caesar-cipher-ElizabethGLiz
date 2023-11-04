sentence = input("Please enter a sentence")
print(sentence)
sentence = sentence.lower()
print(sentence)
substitution_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}
secret_sentence = []
i = 0
for i in range(len(sentence)):
    print(f" Each letter of the sentence {sentence[i]}")
    if sentence[i] in substitution_dict:
        print("yes")
        secret_sentence.append(substitution_dict[sentence[i]])
        i += 1
    else:
        print("no")
        secret_sentence.append(sentence[i])
        i += 1
secret_sentence = ''.join(secret_sentence).split()
print(*secret_sentence)
        