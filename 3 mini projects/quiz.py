questions = ("Which animal has the largest brain?: ",
            "Which of the planetary blood components is responsible for its color?: ",
            "What is the deepest natural lake in the world?: ",
            "In what year was the first car with an internal combustion engine patented?: ",
            "Which of the following warriors was not a Viking?: ")

options = (("A. Human", "B. Dolphin", "C. Sperm whale/Cachalot", "D. Elephant"),
            ("A. Hemoglobin", "B. Lymphocytes", "C. Thrombocytes", "D. Erythrocytes"),
            ("A. Dead Sea", "B. Lake Baikal", "C. Lake Tanganyika", "D. Lake of Gennesaret"),
            ("A. 1866", "B. 1885", "C. 1901", "D. 1922"),
            ("A. Ragnar Lodbrok", "B. Harald Fairhair", "C. Leif Erikson", "D. Attila"))

answers = ("C", "D", "B", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Yor score is: {score}%")