import random

def get_user_choice():
    while True:
        print("Enter your choice (rock, paper, scissors): ")
        user_choice = input().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_choices(user_choice, computer_choice):
    choices = {
        'rock': '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''',
        'paper': '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        ''',
        'scissors': '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        '''
    }

    print("Your choice:")
    print(choices[user_choice])

    print("\nComputer's choice:")
    print(choices[computer_choice])

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

