import random
import math

# Starting chips value
chips = 500

# Assigns card values to Ace and Face cards
card_values = {
    'Ace': 11,
    'J': 10,
    'Q': 10,
    'K': 10
}

# Function that returns a random card in deck
def deal_card():
    card = random.choice(deck)
    deck.remove(card) # Remove card so it can't be drawn again
    return card

# Function for ace functionality
def calculate_score(cards):
    score = 0
    aces = 0

    for card in cards:
        value = card_values.get(card, card)  # lookup if string, else keep number
        score += value
        if card == "Ace":
            aces += 1

    # Adjust Aces if needed
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

print("\nWelcome to Blackjack! You have " + str(chips) + " chips.")

while True: 

    # Creates 52 card deck inside loop for reshuffling
    deck = ['Ace','Ace','Ace','Ace',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']

    while True:
        try:
            bet = int(input("\nChoose your bet: "))
            if 1 <= bet <= chips:
                break
            else:
                print(f"Invalid bet! Must be between 1 and {chips}.")
        except ValueError:
            print("Please enter a valid number for your bet.")

    userCards = [deal_card(), deal_card()]
    dealerCards = [deal_card(), deal_card()]

    userScore = calculate_score(userCards)
    dealerScore = calculate_score(dealerCards)

    print(f"\n{userCards} You have: {userScore}")
    print(f"\nDealer shows: {dealerCards[0]}")

    if userScore == 21 and dealerScore != 21:
        chips = chips + math.ceil(bet * 1.5)
        print(f"\nDealer's cards: {dealerCards}, Dealer's score: {dealerScore}")
        print("\nYou got blackjack! You win!")
        print("You now have: " + str(chips) + " chips")
        continue

    while True:
        choice = input("\nDo you want to hit, stand or double?\n").lower()

        if choice in ["hit", "h"]:
            userCards.append(deal_card())
            userScore = calculate_score(userCards)
            print(f"{userCards} You have: {userScore}")
            if userScore > 21:
                print(f"\nDealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("\nYou went over. You lose!")
                chips = chips - bet
                break
            elif userScore == 21 and dealerScore != 21:
                print(f"\nDealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("\nYou got 21! You win!")
                chips = chips + bet
                break
            elif userScore == 21 and dealerScore == 21:
                print(f"\nDealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("\nIt's a draw!")
            else:
                continue

        elif choice in ["double", "d"]:
            if bet * 2 > chips:
                print("\nYou cannot double your bet.")
                continue
            else:
                bet = bet * 2
                userCards.append(deal_card())
                userScore = calculate_score(userCards)
                print(f"{userCards} You have: {userScore}")

            if userScore > 21:
                print("You went over. You lose!")
                chips = chips - bet
            else:
                print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")

            while dealerScore < 17:
                dealerCards.append(deal_card())
                dealerScore = calculate_score(dealerCards)
                print(f"\nDealer's cards: {dealerCards}, dealer's score: {dealerScore}")
            
            if dealerScore > 21:
                print("Dealer went over. You win!")
                chips = chips + bet
                break

            if dealerScore <= 21:
                if dealerScore > userScore:
                    print("\nDealer wins!")
                    chips = chips - bet
                elif dealerScore < userScore:
                    print("\nYou win!")
                else:
                    print("\nIt's a draw!")

        elif choice in ["stand", "s"]:
            print(f"\nDealer's cards: {dealerCards}, dealer's score: {dealerScore}")

            while dealerScore < 17:
                dealerCards.append(deal_card())
                dealerScore = calculate_score(dealerCards)
                print(f"\nDealer's cards: {dealerCards}, dealer's score: {dealerScore}")

            if dealerScore > 21:
                print("\nDealer went over. You win!")
                chips = chips + bet
                break
            elif dealerScore > userScore:
                print("\nDealer wins!")
                chips = chips - bet
                break
            elif dealerScore < userScore:
                print("\nYou win!")
                chips = chips + bet
                break
            else:
                print("\nIt's a draw!")

            break
        
        else:
            print("Invalid. Indicate hit, stand, or double.") 
            continue

    if chips == 0:
        print("You ran out of chips! Better luck next time!")
        break

    print("\nYou now have: " + str(chips) + " chips")
    playAgain = input("\nWould you like to continue? (y/n): ").lower()
    if playAgain in ['n', 'no']:
        print(f"\nThanks for playing! You finished with: {chips} chips!")
        break