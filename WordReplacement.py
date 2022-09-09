def wordReplacement():
    msg = "hi, I am from Python, hi hi hi"

    wordToReplace = input("Enter the word to replace: ")
    replacementWord = input("Enter the replacement word: ")
    
    print(msg.replace(wordToReplace, replacementWord))

wordReplacement()