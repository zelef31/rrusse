import os
import random

decks = input("Entrez le nombre de deck a utiliser : ")

# choix de decks
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# initialisation scores
wins = 0
Défaites = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "V"
        if card == 12:card = "D"
        if card == 13:card =  "R"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Voulez vous rejouer ? (O/N) : ").lower()
    if again == "o":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Au revoir !")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "V" or card == "D" or card ==  "R":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "V"
    if card == 12:card = "D"
    if card == 13:card =  "R"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("     bienvenue au Black Jack ! ")
    print("-"*30+" ")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mDéfaites:  \033[1;37;40m%s " % (wins, Défaites))
    print("-"*30+" ")
    print ("Le dealer montre un  " + str(dealer_hand) + "Pour un total de  " + str(total(dealer_hand)))
    print ("Vous avez  " + str(player_hand) + " Pour un total de  " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global Défaites
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Félicitation ! vous avez obtenu un BlackJack! ")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Déssolé vous avez perdu ! Le dealer a obtenu un BlackJack. ")
        Défaites += 1
        play_again()

def score(dealer_hand, player_hand):
        # score
        global wins
        global Défaites
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Félicitation ! vous avez obtenu un BlackJack! ")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Désolé vous avez perdu ! Le dealer a obtenu un BlackJack. ")
            Défaites += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Désolé vous avez dépassé donc vous avez perdu. ")
            Défaites += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Le dealer a perdu.  Vous avez gagné ! ")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Désolé votre score n'est pas aussi haut que celui du dealer. Vous avez perdu !' ")
            Défaites += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Félicitations votre score est plus haut que celui du dealer. vous avez gagné ! ")
            wins += 1

def game():
    global wins
    global Défaites
    choice = 0
    clear()
    print("     bienvenue au BlackJack! ")
    print("-"*30+" ")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mDéfaites:  \033[1;37;40m%s " % (wins, Défaites))
    print("-"*30+" ")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("Le dealer montre un  " + str(dealer_hand[0]))
    print ("Vous avez un  " + str(player_hand) + " pour un total de  " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Vous voulez [M]iser, [R]ester, ou [Q]uitter: ").lower()
        if choice == 'm':
            hit(player_hand)
            print(player_hand)
            print("total de la main : " + str(total(player_hand)))
            if total(player_hand)>21:
                print('vous avez dépassé')
                Défaites += 1
                play_again()
        elif choice=='r':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Le dealer a dépassé. Vous avez gagné !')
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "D":
            print("Au-revoir !")
            quit=True
            exit()


if __name__ == "__main__":
   game()