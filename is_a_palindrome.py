text = input("Enter your text to check if it is a palindrome: ")
text = text.lower() # Remove uppercase letters
global text2, text3
text2, text3 = "", ""
for ch in text: # Remove whitespaces and reverse the order of the string
    
    if ch.isalpha():
        text2 += ch
        text3 = ch + text3

if text2 == text3:
    print("It's a palindrome")
else:
    print("It's not a palindrome")