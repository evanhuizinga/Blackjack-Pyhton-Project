import random

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

print("Welcome to Blackjack! You have " + str(chips) + " chips.")

while True: 

    # Creates 52 card deck inside loop for reshuffling
    deck = ['Ace','Ace','Ace','Ace',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']

    while True:
        bet = int(input("\nChoose your bet: "))
        if 1 <= bet <= chips:
            break
        else:
            print(f"Invalid bet! You must bet between 1 and {chips}")

    userCards = [deal_card(), deal_card()]
    dealerCards = [deal_card(), deal_card()]

    userScore = calculate_score(userCards)
    dealerScore = calculate_score(dealerCards)

    print(f"\n{userCards} You have: {userScore}")
    print(f"\nDealer shows: {dealerCards[0]}")

    if userScore == 21 and dealerScore != 21:
        print(f"Dealer's cards: {dealerCards}, Dealer's score: {dealerScore}")
        print("You got blackjack! You win!")
        chips = chips + (bet * 1.5)
        continue

    while True:
        choice = input("\nDo you want to hit, stand or double?\n").lower()

        if choice == "hit":
            userCards.append(deal_card())
            userScore = calculate_score(userCards)
            print(f"{userCards} You have: {userScore}")
            if userScore > 21:
                print(f"Dealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("You went over. You lose!")
                chips = chips - bet
                break
            elif userScore == 21 and dealerScore != 21:
                print(f"Dealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("You got 21! You win!")
                chips = chips + bet
                break
            elif userScore == 21 and dealerScore == 21:
                print(f"Dealer's cards: {dealerCards}, Dealer's Score: {dealerScore}")
                print("It's a draw!")
            else:
                continue

        elif choice == "double":
            if bet * 2 > chips:
                print("You cannot double your bet.")
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
                print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")
            
            if dealerScore > 21:
                print("Dealer went over. You win!")
                chips = chips + bet
                break

            if dealerScore <= 21:
                if dealerScore > userScore:
                    print("Dealer wins!")
                    chips = chips - bet
                elif dealerScore < userScore:
                    print("You win!")
                else:
                    print("It's a draw!")

        elif choice == "stand":
            print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")

            while dealerScore < 17:
                dealerCards.append(deal_card())
                dealerScore = calculate_score(dealerCards)
                print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")

                userScore = calculate_score(userCards)
                dealerScore = calculate_score(dealerCards)

                if dealerScore > 21:
                    print("Dealer went over. You win!")
                    chips = chips + bet
                    break
                elif dealerScore > userScore:
                    print("Dealer wins!")
                    chips = chips - bet
                    break
                elif dealerScore < userScore:
                    print("You win!")
                    chips = chips + bet
                    break
                else:
                    print("It's a draw!")

            break

    print("You now have: " + str(chips) + " chips")