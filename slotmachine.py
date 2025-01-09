import random

def spin_reels():
    symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar']
    return [random.choice(symbols) for _ in range(3)]

def calculate_winnings(bet, reels):
    if reels[0] == reels[1] == reels[2]:
        # Jackpot - all three symbols match
        return bet * 10
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        # Partial match - two symbols match
        return bet * 2
    else:
        # No match
        return 0

def main():
    print("Welcome to the Slot Machine Simulator!")
    balance = 100  # Starting balance

    while True:
        print(f"\nYour current balance: ${balance}")
        
        try:
            bet = int(input("Enter your bet amount (or 0 to quit):"))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if bet == 0:
            print("Thanks for playing! Goodbye!")
            break

        if bet > balance:
            print("You don't have enough balance to make this bet. Try a smaller amount.")
            continue

        print("Spinning the reels...")
        reels = spin_reels()
        print(f"Reels: {reels[0]} | {reels[1]} | {reels[2]}")

        winnings = calculate_winnings(bet, reels)
        if winnings > 0:
            print(f"Congratulations! You won ${winnings}!")
        else:
            print("No match. Better luck next time!")

        balance += winnings - bet

        if balance <= 0:
            print("You are out of balance. Game over!")
            break

main()
