# a dictionary contains questions and answers
# mark the scores
# loop through the dictionary using key value pairs
# display each question to the user and allow them to answer
# tell them that is wrong or right
# show the result at the final

quiz = {
    "Q1": {
        "q":"What is the Capital of India?",
        "a":"New Delhi"
    },
    "Q2": {
        "q":"What is the Capital of Australia?",
        "a":"Canberra"
    },
    "Q3": {
        "q":"What is the Capital of UK?",
        "a":"London"
    },
    "Q4": {
        "q":"What is the Capital of Russia?",
        "a":"Moscow"
    },
}

score = 0

for key,value in quiz.items():
    print(value["q"])
    ans = input("Your answer is ")
    
    if ans.lower() == value["a"].lower():
        print("You are correct!!!")
        score = score + 1
        print("Your Score is ", str(score))
        print()
    
    else:
        print("You are wrong!")
        print("The correct answer is ", value["a"])
        score = score - 1
        print("Your Score is ", str(score))
        print()

print("You got ", str(score), " out of 4 questions correctly")
print("Your percentage is ", str(int(score / 4 * 100)), "%")    