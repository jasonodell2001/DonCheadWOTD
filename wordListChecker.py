import pandas as pd

#function that checks how many unused words are left in the list
def remainingWords():
    wordList = pd.read_csv('wordList.csv') #load the word list
    remaining = wordList[wordList['Used'].str.contains('N')] #check how many are marked as unused
    N = len(remaining)

    print("Number of unused words remaining: " + str(N)) #print the number of unused words

    #print errors to the console once there are only a few words left
    if N == 1:
        for i in range(10):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("THERE IS ONLY ONE WORD REMAINING, RESTOCK WORDS NOW!")
    elif N <= 7:
        for i in range(10-N):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("THERE ARE ONLY " + str(N) + " WORDS REMAINING")
    elif N == 50:
        print("There are only 50 words left!")
    elif N == 30:
        print("There are only 30 words left. Better restock before the end of the month.")
    elif N == 14:
        print("!!!!!!!!!!!!!")
        print("There are only 2 weeks of words remaining, better get restocking.")

    return 0

def addWords(newWordList,newModifierList):
    print("Adding words: " + str(newWordList))
    wordList = pd.read_csv('wordList.csv')
    N = len(newWordList)
    used = ["N"]*N
    df = pd.DataFrame({"Word":newWordList,"Used":used,"OfTheDay":newModifierList})
    newList = pd.concat([wordList,df], ignore_index=True)
    #print(newList)
    newList.to_csv('wordList.csv', index=False)

def newWordAdder():
    wordList = pd.read_csv('wordList.csv')
    newList = []
    newModifierList = []
    while True:
        newWord = input("Input new word to be checked and added, or type 'QUIT' to quit: ")
        if newWord == 'QUIT':
            if len(newList) > 0:
                print("Saving words...")
                addWords(newList,newModifierList)
                print("Saved!")
            input("Press enter to exit:")
            break
        else:
            newWord = newWord.lower()

        matchingWords = wordList[wordList['Word'].str.contains(newWord)]
        N = len(matchingWords)
        if (N == 0) & (newWord not in newList):
            print("Word is not already in list, adding to queue")
            newList.append(newWord)
            newMod = input("Enter modifier (Don Cheadle __ of the Day): ").lower()
            newModifierList.append(newMod)
        elif N > 0:
            print("Word already exists in list:")
            print(matchingWords)
            override = input("Override? Y/N: ").lower()
            if override == 'y':
                newList.append(newWord)
                newMod = input("Enter modifier (Don Cheadle __ of the Day): ").lower()
                newModifierList.append(newMod)
        elif newWord in newList:
            print("Word already queued to be added:")
            print(newList)
            override = input("Override? Y/N: ").lower()
            if override == 'y':
                newList.append(newWord)
                newMod = input("Enter modifier (Don Cheadle __ of the Day): ").lower()
                newModifierList.append(newMod)