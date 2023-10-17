import random

# Function to generate a random secret code (4-digit number in this case)
def generate_secret_code():
    return str(random.randint(1000, 9999))

# Function to check if a guess is valid (4-digit number)
def is_valid_guess(guess):
    return len(guess) == 4 and guess.isdigit()

# Function to provide hints by comparing the secret code and the guess
def provide_hints(secret, guess):
    hints = []
    for i in range(4):
        if secret[i] == guess[i]:
            hints.append("Exact")
        elif secret[i] in guess:
            hints.append("Partial")
        else:
            hints.append("None")
    return hints

# Main game loop
def play_mastermind():
    print("Welcome to Mastermind!")
    
    player1_score = 0
    player2_score = 0
    
    while True:
        # Player 1 sets the secret code
        secret_code = generate_secret_code()
        print("Player 1, set your secret code.")
        
        # Player 2 guesses the code
        attempts = 0
        while True:
            guess = input("Player 2, make a guess (4-digit number): ")
            
            if not is_valid_guess(guess):
                print("Invalid guess. Please enter a 4-digit number.")
                continue
            
            attempts += 1
            
            if guess == secret_code:
                print("Player 2 guessed the code in", attempts, "attempts!")
                player2_score += 1
                break
            
            hints = provide_hints(secret_code, guess)
            print("Hints:", hints)
        
        # Player 2 sets the secret code
        secret_code = generate_secret_code()
        print("Player 2, set your secret code.")
        
        # Player 1 guesses the code
        attempts = 0
        while True:
            guess = input("Player 1, make a guess (4-digit number): ")
            
            if not is_valid_guess(guess):
                print("Invalid guess. Please enter a 4-digit number.")
                continue
            
            attempts += 1
            
            if guess == secret_code:
                print("Player 1 guessed the code in", attempts, "attempts!")
                player1_score += 1
                break
            
            hints = provide_hints(secret_code, guess)
            print("Hints:", hints)
        
        # Ask if players want to play another round
        another_round = input("Play another round? (yes/no): ")
        if another_round.lower() != "yes":
            break
    
    print("Game over!")
    print("Player 1's score:", player1_score)
    print("Player 2's score:", player2_score)

if __name__ == "__main__":
    play_mastermind()
