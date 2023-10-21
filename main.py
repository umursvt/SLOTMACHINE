import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 10,
    "B": 5,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit(balance):
    while True:
        amount = input("What would you like to deposit? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance += amount
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print('Please enter a valid number.')
    return balance

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}) $: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number.')
    return lines

def get_bet():
    while True:
        bet = input(f"What would you like to bet on each line? (${MIN_BET}-{MAX_BET}) $: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print('Please enter a number.')
    return bet

def main():
    balance = 0
    balance = deposit(balance)
    playing = True

    while playing and balance > 0:  
        lines = get_number_of_lines()

        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. Your balance is only ${balance}.")
            else:
                print(f"The bet is completed. Amount of bet: ${total_bet}")
                break

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print("Slot Machine Spin:")
        print_slot_machine(slots)

        winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_count)
        if winnings > 0:
            balance += winnings
            print(f"You won ${winnings} on lines: {', '.join(map(str, winnings_lines))}. Your balance is now ${balance}.")
        else:
            balance -= total_bet
            print(f"Sorry, you didn't win this time. Your balance is now ${balance}.")

        if balance <= 0:
            print("Game over! Your balance has reached 0.")
            break

        play_again = input("Press 'q' to quit or any other key to play again: ")
        if play_again.lower() == 'q':
            playing = False

if __name__ == "__main__":
    main()
