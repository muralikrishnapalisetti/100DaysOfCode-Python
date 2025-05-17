import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors! First to 3 wins!")


def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        try:
            user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if user_choice not in [0, 1, 2]:
                print("🚨 Invalid choice! Please enter 0, 1, or 2.")
                continue

            print(f"\nYou chose:\n{game_images[user_choice]}")
            computer_choice = random.randint(0, 2)
            print(f"Computer chose:\n{game_images[computer_choice]}")

            if user_choice == computer_choice:
                print("⚖️ It's a draw!")
            elif (user_choice == 0 and computer_choice == 2) or \
                 (user_choice == 1 and computer_choice == 0) or \
                 (user_choice == 2 and computer_choice == 1):
                print("🎉 You win this round!")
                user_score += 1
            else:
                print("😞 You lost this round!")
                computer_score += 1

            print(f"\n🔢 Score: You {user_score} - {computer_score} Computer")

        except ValueError:
            print("🚨 Please enter a valid number (0, 1, or 2).")

    if user_score == 3:
        print("\n🏆 Congratulations! You won the match! 🎉")
        print(r"""
           ✨✨✨✨✨✨✨✨✨✨
         🎉 YOU ARE THE CHAMPION! 🎉
           🏆  VICTORY IS YOURS! 🏆
           ✨✨✨✨✨✨✨✨✨✨
             _______________
            |@@@@|     |####|
            |@@@@|     |####|
            |@@@@|     |####|
            \@@@@|     |####/
             \@@@|     |###/
              `@@|_____|##'
                   (O O)
            ____ooO-(_)-Ooo____
        """)
    else:
        print("\n💻 Computer wins the match! Better luck next time! 🤖")
        print(r"""
            💢 YOU FOUGHT BRAVELY 💢
            ┌─────────────────────┐
            │      YOU LOST!      │
            └─────────────────────┘
                     .-"      "-.
                    /            \
                   |              |
                   |,  .-.  .-.  ,|
                   | )(_o/  \o_)( |
                   |/     /\     \|
                   (_     ^^     _)
                    \__|IIIIII|__/
                     | \IIIIII/ |
                     \          /
                      `--------`
              ✋ Down goes your hand… But not your spirit!
        """)


def main():
    play_game()
    play_again = input("\nDo you want to try again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("\nThanks for playing! See you next time! 👋")


if __name__ == "__main__":
    main()
