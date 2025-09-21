import random

chips = 500
A = 11
deck = [A,A,A,A,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10]
def deal_card():
    return random.choice(deck)

print("Welcome to Blackjack! You have " + str(chips) + " chips.")
bet = int(input("\nChoose your bet: "))
userCards = [deal_card(), deal_card()]
dealerCards = [deal_card(), deal_card()]

userScore = sum(userCards)
dealerScore = sum(dealerCards)

print(f"\n{userCards} You have: {userScore}")
print(f"\nDealer shows: {dealerCards[0]}")

while True:
    choice = input("\nDo you want to hit, stand or double?\n").lower()

    if choice == "hit":
        userCards.append(deal_card())
        userScore = sum(userCards)
        print(f"{userCards} You have: {userScore}")
        print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")
        if userScore > 21:
            print("You went over. You lose!")
            chips = chips - bet
            break
        elif userScore == 21:
            print("You got a blackjack! You win!")
            chips = chips + bet
            break

    elif choice == "double":
        bet = bet *2
        userCards.append(deal_card())
        userScore = sum(userCards)
        print(f"{userCards} You have: {userScore}")
        print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")
        if userScore > 21:
            print("You went over. You lose!")
            chips = chips - bet
            break
        if userScore == dealerScore:
            print("It's a draw!")
            break

    elif choice == "stand":
        print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")

        while dealerScore < 17:
            dealerCards.append(deal_card())
            dealerScore = sum(dealerCards)
            print(f"Dealer's cards: {dealerCards}, dealer's score: {dealerScore}")

            userScore = sum(userCards)
            dealerScore = sum(dealerCards)

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