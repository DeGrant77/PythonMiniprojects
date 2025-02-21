"""
Translates your sentences to pyglatin
"""
pyg = "ay"
sentence = input("please enter a sentence:")
for words in sentence.split():
    firstletter = words[0]
    new_word = words[1:len(words)]
    pyglatin = new_word + firstletter + pyg
    if len(pyglatin)> 0 and pyglatin.isalpha():
        print (pyglatin,end=" ")
    else:
        print("No")
