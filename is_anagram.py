texts = [input("Let's check for anagrams:\nWord 1: ").lower(), input("Word 2: ").lower()]

for text in texts:
    text_aux = []
    for ch in text: # Remove whitespaces and puts the characters in the auxiliary string
        if ch.isalpha():
            ch.lower()
            text_aux.append(ch)
    text_aux.sort() # Sorts the characters for further comparison
    texts[texts.index(text)] = text_aux[:] # Copies the contents of the auxiliary list into the main list

if texts[0] == texts[1] and texts[0] != []: # If the two lists are equal and one of them are not empty:
    print("Anagrams")
else:
    print("Not anagrams")