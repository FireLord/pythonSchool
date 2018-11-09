i=1
wordCount=0
alphaNumCount=0
charCount=0
while i>0:
    word=input("Enter a sentence(press q to quit):")
    if word == "q":
        break
    for a in word:
        if a.isspace():
            wordCount+=1
        if a.isalnum():
            alphaNumCount+=1
        charCount+=len(a)
percentage = (alphaNumCount/charCount)*100
print("Number of words:",wordCount+1) # adding 1 as user might not give space after ending sentence.
print("Number of char:",charCount)
print("Percentage of char that are alpha numeric:",percentage)
