def cipher(sentence, displacement):
    deciphered = ""
    displacement = int(displacement)
    for ch in sentence:
        if ord(ch) >= 65 and ord(ch) <= 90:
            ch = chr(ord(ch) + displacement)
            if ord(ch) > 90:
                ch = chr(ord(ch)-26)
        elif ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) + displacement)
            if ord(ch) > 122:
                ch = chr(ord(ch)-26)
        deciphered += ch
    return deciphered

def askfornum(message):
    num = input(message)
    if num.isdigit():
        num = int(num)
        if num < 1:
            return askfornum("Displacement is smaller than 1. Try again: ")
        elif num > 25:
            return askfornum("Displacement is bigger than 25. Try again: ")
        else: return num
    else:   return askfornum("Displacement not a number. Try again: ")

sentence, displacement = input("Sentence: "), askfornum("Displacement (1-25): ")

print(cipher(sentence, displacement))
