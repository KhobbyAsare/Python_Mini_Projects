import random

# Define the options
options = ['rock', 'paper', 'scissors']

# Initialize the scores outside the while loop
userScore: int = 0
computerScore: int = 0

# Ask the user for their option
userOption = input('Type your option-(Rock, Paper or Scissors): ').lower()

# While the user's option is in the options
while userOption in options:
    # Generate a random number for the computer's option
    computeRan = random.randint(1, 3)

    # Determine the computer's option based on the random number
    if computeRan == 1:
        computerOption = 'rock'
    elif computeRan == 2:
        computerOption = 'scissors'
    else:
        computerOption = 'paper'

    # Determine the winner and update the scores
    if userOption == 'scissors' and computerOption == 'paper':
        print("scissors beat paper - User🥳 wins")
        userScore += 1
    elif userOption == 'paper' and computerOption == 'scissors':
        print("scissors beat paper - Computer🤖 wins")
        computerScore += 1
    elif userOption == 'rock' and computerOption == 'paper':
        print(f"paper beat rock - Computer🤖 wins")
        computerScore += 1
    elif userOption == 'paper' and computerOption == 'rock':
        print(f"paper beat rock - User🥳 wins")
        userScore += 1
    elif userOption == 'rock' and computerOption == 'scissors':
        print(f"rock beat scissors - User🥳 wins")
        userScore += 1
    elif userOption == 'scissors' and computerOption == 'rock':
        print(f"scissors beat rock - Computer🤖 wins")
        computerScore += 1
    else:
        print('Neutral Score 🎭')

    # Print the current scores
    print(f'Current Score: Computer {computerScore} : User: {userScore}')

    # Ask the user for their next option
    userOption = input('Type your option-(Rock, Paper or Scissors): ').lower()
