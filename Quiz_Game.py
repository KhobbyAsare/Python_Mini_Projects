# python quiz game

questions = (
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the square root of 64?",
    "Which planet is known as the Red Planet?",
    "Who painted the Mona Lisa?"
)

options = [
    ("A. Paris", "B. London", "C. Rome", "D. Berlin"),
    ("A. J.K. Rowling", "B. Harper Lee", "C. Ernest Hemingway", "D. Mark Twain"),
    ("A. 6", "B. 7", "C. 8", "D. 9"),
    ("A. Venus", "B. Earth", "C. Mars", "D. Jupiter"),
    ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet")
]

answers = ("A", "B", "C", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("✔ Correct")
    else:
        print("❌ Incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------")
print(" RESULTS ")
print("----------------")

zipped = zip(answers, guesses)
print("Correct Answer - Guess")
for answer, guess in zipped:
    print(f"{answer}       -         {guess}")

print(f"You scored {score}/{len(questions)}")
