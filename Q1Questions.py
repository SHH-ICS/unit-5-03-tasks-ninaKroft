# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer.
# This will be six lines, and then store the questions in the file questions.txt.

numberOfQuestions = int(input("How many questions do you want in your quiz? You can have a maximum of 10 questions."+'\n'))

prefix = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]

questions = open("questions.txt", 'w')

correct = False

for x in range(0, numberOfQuestions):
    correct = False
    print("Please enter your", prefix[x], "question:")
    question = input()
    questions.write(question +'\n')

    for y in range(0, 4):
        print("Enter the", prefix[y], "answer:")
        option = input()
        questions.write(option+'\n')

    print("Which answer is correct? Enter A, B, C, or D.")
    while correct == False:
        answer = input()
        if answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D':
            correct = False
            print("Please enter A, B, C, or D.")
        else:
            correct = True

    questions.write(answer+'\n')

print("Your questions are set! Head over to Q2Quiz.py to run your quiz.")

questions.close()
