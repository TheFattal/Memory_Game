import random


def shuffle_cards():
    """ Shuffle and return a list of 12 cards with 6 pairs. """
    cards = ['A'] * 2 + ['B'] * 2 + ['C'] * 2 + ['D'] * 2 + ['E'] * 2 + ['F'] * 2
    random.shuffle(cards)
    return cards


def display_board(board, revealed):
    """ Display the board with revealed cards. """
    for index, card in enumerate(board):
        if revealed[index]:
            print(card, end=' ')
        else:
            print('*', end=' ')
    print()


def play_game():
    """ Play the matching pairs game. """
    cards = shuffle_cards()
    revealed = [False] * len(cards)
    attempts = 0
    matches = 0

    while matches < len(cards) // 2:
        display_board(cards, revealed)

        try:
            input1 = input('Enter the index of the first card (0-11) or "R" to restart: ').strip().upper()
            if input1 == 'R':
                return 'RESTART'
            index1 = int(input1)

            input2 = input('Enter the index of the second card (0-11) or "R" to restart: ').strip().upper()
            if input2 == 'R':
                return 'RESTART'
            index2 = int(input2)

            if not (0 <= index1 < len(cards)) or not (0 <= index2 < len(cards)):
                print("Indices must be between 0 and 11.")
                continue

            if index1 == index2:
                print("You selected the same index twice. Choose different indices.")
                continue

            if revealed[index1] or revealed[index2]:
                print("One or both of these cards are already revealed.")
                continue

            # Reveal the chosen cards
            revealed[index1] = True
            revealed[index2] = True
            display_board(cards, revealed)

            if cards[index1] == cards[index2]:
                print("It's a match!")
                matches += 1
            else:
                print("Not a match.")
                revealed[index1] = False
                revealed[index2] = False

            attempts += 1
        except ValueError:
            print("Invalid input. Please enter integer values between 0 and 11.")

    print(f"Game over! You found all pairs in {attempts} attempts.")
    return 'END'


def main_menu():
    """ Main menu to start or restart the game. """
    while True:
        result = play_game()
        if result == 'END':
            restart = input("Do you want to play again? (yes/no): ").strip().lower()
            if restart != 'yes':
                print("Thank you for playing!")
                break
            else:
                print("Restarting the game...\n")
        elif result == 'RESTART':
            print("Restarting the game...\n")


# Start the game
main_menu()
