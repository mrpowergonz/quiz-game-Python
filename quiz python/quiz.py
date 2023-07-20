 #Have a dictionary that store questions and answers
 #Have a variable that score the tracks of the player
 #loop through the dictionary using the key value pairs
 #Display each question to the user and allow them to answer
 #Tell them if they are right or wrong
 #Show the final result when quiz is completed

quiz = {
    "question1": {
        "question" : "What is the capital of Spain?",
        "answer" : "Madrid"
    },
    "question2" : {
        "question" : "What is the capital of Germany?",
        "answer" : "Berlin"
    },
    "question3" : {
        "question" : "What is the capital of Italy?",
        "answer" : "Rome"
    },
    "question4" : {
        "question" : "What is the capital of France?",
        "answer" : "Paris"
    },
    "question5" : {
        "question" : "What is the capital of Portugal?",
        "answer" : "Lisbon"
    },
    "question6" : {
        "question" : "What is the capital of Ireland?",
        "answer" : "Dublin"
    },
    "question7" : {
        "question" : "What is the capital of Norway?",
        "answer" : "Oslo"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1 
        print("Your score is : " + str(score))
        print("")
    else:
        print("Wrong")
        print("The answer is : " + value["answer"])
        print("Your score is: " + str(score))
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")