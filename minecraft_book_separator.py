# This code takes an input and divides it into parts that have 256 characters or less. 
# It is usefull to paste a long text into a Minecraft Bedrock book, that can only accept 256 characters per page and doesn't accept pasting longer texts. 
text = input("Insert your text here: ")
pages = []
while len(text) > 256:
    pages.append(text[0:256])
    text = text[256:]
pages.append(text)
for page in pages:
    print("Page ", pages.index(page)+1, ":", sep="")
    print(page)
    print("-"*10)
