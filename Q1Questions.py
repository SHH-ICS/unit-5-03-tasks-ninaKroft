# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer.
# This will be six lines, and then store the questions in the file questions.txt.

numberOfQuestions = int(input("How many questions do you want in your quiz? You can have a maximum of 10 questions."+'\n'))

prefix = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]

questions = open("questions.txt", 'w')

for x in range(0, numberOfQuestions):
    print("Please enter your", prefix[x], "question:")
    question = input()
    questions.write(question +'\n')

    print("Enter the first answer:")
    first = input()
    questions.write(first+'\n')

    print("Enter the second answer:")
    second = input()
    questions.write(second+'\n')

    print("Enter the third answer:")
    third = input()
    questions.write(third+'\n')

    print("Enter the fourth answer:")
    fourth = input()
    questions.write(fourth+'\n')

    print("Which answer is correct? Enter A, B, C, or D.")
    answer = input()
    questions.write(answer+'\n')

print("Your questions are set! Head over to Q2Quiz.py to run your quiz.")

questions.close()

