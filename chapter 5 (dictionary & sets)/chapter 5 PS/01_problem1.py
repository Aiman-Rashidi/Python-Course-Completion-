wordMeaningPair = {
    "madad" : "help",
    "kursi" : "chair",
    "billi" : "cat"
}

askWord = input("enter the word you want meaning of: ")

# print(wordMeaningPair[askWord])   # throws an error 
# print(wordMeaningPair.get(askWord))

meaning = wordMeaningPair.get(askWord)
if meaning == None:
    print("Word not found!")
else:
    print(wordMeaningPair.get(askWord))