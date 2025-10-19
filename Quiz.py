ques = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ",
                       "Which HTTP status code means 'Not Found'?",
                       "How do you select an element with id='app' in CSS?",
                       "Which language runs in a web browser?",
                       "Which is a JavaScript framework?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                   ("A. 200", "B. 404", "C. 500", "D. 301"),
                   ("A. #app", "B. .app", "C. app", "D. *app"),
                   ("A. JavaScript", "B. Python", "C. C++", "D. Java"),
                   ("A. React", "B. Django", "C. Laravel", "D. Spring"))

ans = ("C", "D", "A", "A", "B", "B", "A", "A", "A")
guesses = []
score = 0
ques_num = 0

for question in ques:
    print(question)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == ans[ques_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{ans[ques_num]} is the correct answer")
    ques_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

score = int(score / len(ques) * 100)
print(f"Your score is: {score}%")
