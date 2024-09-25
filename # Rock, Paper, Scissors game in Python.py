# Rock, Paper, Scissors game in Python

print("Welcome to the Rock, Paper, Scissors game!")

# Define the options
options = ["rock", "paper", "scissors"]

# Loop to allow the player to play multiple rounds
while True:
    # Get the player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    
    # Generate the computer's choice
    import random
    computer_choice = random.choice(options)
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "player"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "player"
    else:
        result = "computer"
    
    # Print the results
    print(f"You chose {player_choice}, the computer chose {computer_choice}.")
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("You lose.")
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break

print("Thanks for playing!")