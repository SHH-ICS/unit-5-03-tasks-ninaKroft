# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.

letters = ["A.)", "B.)", "C.)", "D.)"]

linesRead = 0

score = 0

validAnswer = False

quiz = open("questions.txt", 'r')

lines = len(quiz.readlines())

quiz.close()

quiz = open("questions.txt", 'r')

totalQuestions = 0

while linesRead < lines:

    ques = quiz.readline()
    print(ques)
    linesRead = linesRead + 1

    for x in range(0, 4):
        ans = quiz.readline()
        letter = letters[x]
        print(letter, ans)
        linesRead = linesRead + 1

    answer = quiz.read(1)
    quiz.readline() #It kept on putting a space afterwards which would mess with the answer, so I had to read one character then read the rest so that it would move on to the next line and not put a space after it read the answer.
    linesRead = linesRead + 1

    userAnswer = input("What is the answer? Enter A, B, C, or D."+'\n')

    while validAnswer == False:
        if userAnswer != 'A' and userAnswer != 'B' and userAnswer != 'C' and userAnswer != 'D':
            print("Please enter A, B, C, or D")
            userAnswer = input()
        else:
            validAnswer = True

    if userAnswer == answer:
        score = score + 1

    totalQuestions = totalQuestions + 1

percent = int((score / totalQuestions) * 100)

print("You got", score, "/", totalQuestions, "questions correct. That's", percent, "%.")

quiz.close()