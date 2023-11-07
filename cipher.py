#This Caesar cipher program replaces
#a letter in the sentence with a letter that is a five  down in the alphabet
sentence = input("Please enter a sentence ")
#print(sentence)
sentence = sentence.lower()
#print(sentence)
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
secret_sentence = ""
for char in sentence:
    if char in substitution_dict:
        char = substitution_dict[char]
    secret_sentence += char
print(secret_sentence)