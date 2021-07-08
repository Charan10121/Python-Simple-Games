
import random

class Player():
    def __init__(self,balance,sum):
        self.balance=balance
        self.sum=sum

class Computer():
    def __init__(self,sum):
        self.sum=sum

number_of_cards_left = 52

number_of_aces=0

cards=['A',2,3,4,5,6,7,8,9,10,10,10,10]*4   #create a list containing all the cards
cards.insert(0,0)   #making the first element 0 to avoid confusion

def random_card():
    global number_of_cards_left
    global cards
    global number_of_aces

    card1=random.randint(1,number_of_cards_left)    #selecting index of a random card
    x = cards.pop(card1)    #removing card from deck
    number_of_cards_left = number_of_cards_left-1
    if(x=='A'):
        print("Recieved an ace!")
        number_of_aces=number_of_aces+1 #increasing number of aces
        return 0
    return x    #returning card value

def random_computer_card():
    global number_of_cards_left
    global cards

    card1=random.randint(1,number_of_cards_left)    #selecting index of a random card
    x = cards.pop(card1)    #removing card from deck
    number_of_cards_left = number_of_cards_left-1
    if(x=='A'):
        return 0
    return x    #returning card value

while True:
    try:
        initial_sum=int(input('Enter the initial amount of balance: '))
    except ValueError:
        print('Please provide integer value')
    else:
        break

player=Player(initial_sum,0)  #creating player and computer
computer=Computer(0)

while True:          #loops for each time the player wants to keep playing

    print('\n')
    print("\n")
    print(f"Remaining Balance = {player.balance}")

    player.sum=0
    computer.sum=0
    number_of_aces=0
    number_of_cards_left=52
    cards=['A',2,3,4,5,6,7,8,9,10,10,10,10]*4   #create a list containing all the cards
    cards.insert(0,0)   #making the first element 0 to avoid confusion
    
    play_game=''
    while (play_game!='N' and play_game!='Y'):
        play_game = (input('Would you like to play? (Y/N): ')).upper()
        
    if(play_game=='N'):
        break
    
    while True:
        try:
            initial_bet=int(input('Enter the amount you would like to bet: '))
        except ValueError:
            print('Please provide integer value')
        else:
            break

    print('\n')

    if(initial_bet > player.balance):
        print(f"You don't have enough balance for this bet. Please try again") 
        continue
    player.balance= player.balance - initial_bet

    number_of_cards_left = 52

    card1 = random_card()
    if card1==0:
        print(f"Initial 1st Card = A")
    else:
        print(f"Initial 1st Card = {card1}")

    card2 = random_card()
    if card2==0:
        print(f"Initial 1st Card = A")
    else:
        print(f"Initial 2nd Card = {card2}")

    player.sum= player.sum + card1 + card2

    if(player.sum==21):
        print("Player wins by blackjack")

    print(f'Player hand = {player.sum}')

    card_comp1 = random_computer_card()
    if card_comp1==0:
        card_comp1=11
    print(f"Initial Dealer Card = {card_comp1}")

    card_comp2 = random_computer_card()  #setting down a random second card face down

    computer.sum = computer.sum + card_comp1 #storing the dealers card sum for only first card

    player_is_playing=True

    while player_is_playing:
        action=''
        while (action!='H' and action!='S'):
            action=input("Would you like to to Hit or Stand(H/S)?: ").upper()
        if(action=='H'):
            card1 = random_card()
            if card1!=0:
                print(f"New card = {card1}")
            player.sum = player.sum + card1
            
            if number_of_aces>0 and player.sum>21:
                player.sum = player.sum - 10
                number_of_aces= number_of_aces-1
            
            print(f"Player Sum ={player.sum}")
            
            if player.sum>21:
                print('Player Busts')
                player_is_playing = False
        if(action=='S'):
            player_is_playing = False
            while(number_of_aces!=0):
                if(player.sum+11<=21):
                    player.sum=player.sum+11
                else:
                    player.sum=player.sum+1
                number_of_aces=number_of_aces-1
            print(f"Player Sum ={player.sum}")

            if player.sum>21:
                print('Player Busts')
                player_is_playing = False
    
    if player.sum<=21:

        if card_comp2!=0:
            print(f"Dealer's hidden card = {card_comp2}")
            computer.sum=computer.sum+card_comp2
        print(f"Dealer Sum ={computer.sum}")
        if card_comp2==0 and computer.sum + 11 > 21:
            computer.sum = computer.sum + 1
            print(f"Dealer's hidden card = 1(Ace)")
        elif card_comp2==0 and computer.sum + 11 <= 21:
            computer.sum = computer.sum + 11
            print(f"Dealer's hidden card = 11(Ace)")

        while computer.sum < 17:
            card1 = random_computer_card()
            if card1==0 and computer.sum + 11 > 21:
                if computer.sum+11 >= 17 and computer.sum+11<player.sum:
                    computer.sum = computer.sum + 1
                    print(f"Dealer's new card = 1(Ace)")
            elif card1==0 and computer.sum + 11 <= 21:
                computer.sum = computer.sum + 11
                print(f"Dealer's new card = 11(Ace)")

            if card1!=0:
                print(f"Dealer's new card = {card1}")
                computer.sum=computer.sum+card1
            print(f"Dealer Sum ={computer.sum}")

        if computer.sum > 21:
            print("Dealer Bust")
            player.balance = player.balance + (initial_bet*2)
            continue
        
        if computer.sum > player.sum:
            print("Dealer Wins")
            continue

        if computer.sum < player.sum:
            print("Player wins")
            player.balance = player.balance + (initial_bet*2)
            continue

        if computer.sum == player.sum:
            print("TIE")
            player.balance = player.balance + (initial_bet)
            continue




