# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

quiz = open("questions.txt", 'r')


letters = ["A.)", "B.)", "C.)", "D.)"]

question = quiz.readline()
print(question)

for x in range(0, 4):
    answers = quiz.readline()
    letter = letters[x]
    print(letter, answers)

answer = quiz.readline()

userAnswer = input("What is the answer?"+'\n')

#if answer == userAnswer:
    #print("Correct")
#else:
    #print("Incorrect")

quiz.close()