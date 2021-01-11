########################################################
# Ruvi Jaimes                                          #
# Lab  5: COSC 1336                                    #
# This program displays the menu:                      #
# 1. Make Change                                       #
# 2. High Card                                         #
# 3. Quit                                              #
# Asks the user for option at the begging of game      #
# and after the game chosen ends.                      #
#                                                      #
# Plays game                                           #
# Make Change: asks the user for the money owed and    #
# given, then it gives how many dollars, quarters,     #
# nickels, and pennies are needed for change           #
#                                                      #
# High Card: asks both users for names, randomly       #
# distributes cards to players, displays what card     #
# they got (ex. Mike your card is a King), and finally #
# displays the winner of who got the highest card.     #
#                                                      #
# Deal Hand: gives the user 5 cards                    #
#                                                      #
########################################################

import random


def welcome_message():
    print("-------------------------------------------------")
    print("-          * Welcome to Lame Game. *            -")
    print("-    This program displays the game menu:       -")
    print("-            Game Menu:                         -")
    print("-            1. Make Change                     -")
    print("-            2. High Card                       -")
    print("-            3. Deal Hand                       -")
    print("-            4. Quit                            -")
    print("-                                               -")
    print("-    Then promts for option to play the game    -")
    print("-                                               -")
    print("-------------------------------------------------")
    

def get_option():
    print()
    print("Game Menu:")
    print("1. Make Change")
    print("2. High Card")
    print("3. Deal Hand")
    print("4. Quit")
    # Ask user to choose option
    option = int(input("Enter menu option: "))
    # Check invalid options
    while option < 1 or option >= 5:
    
        print()
        print("ERROR: Invalid Option. Enter an integer 1-3 or 4 to quit.")
        print()
        print("Game Menu:")
        print("1. Make Change")
        print("2. High Card")
        print("3. Deal Hand")
        print("4. Quit")
    # Ask user to choose option
        option = int(input("Enter menu option: "))
    return option

def make_change():
    print()
    print("* Make Change *")
    money_owed = float(input("Enter amount owed: "))
    money_paid = float(input("Enter amount paid: "))

    #validation loop
    while money_owed < 0:
        print("ERROR: The money owed is less than zero")
        money_owed = float(input("Enter amount owed: "))
    while money_paid < 0:
        print("ERROR: The money paid is less than zero")
        money_paid = float(input("Enter amount paid: "))
    while money_owed < 0 and money_paid < 0:
        print("ERROR: The money owed and money paid is less than zero")
        money_owed = float(input("Enter amount owed: "))
        money_paid = float(input("Enter amount paid: "))
        
    # If change is change is greater than paid
    if money_paid < money_owed:
        print("You have not payed enough.")

    else:
        
        # math equation
        change= money_paid - money_owed
        print()
        # Display to user
        print("You owe the customer $", format(change,".2f"), sep="")
        print("\t\t $", format(change,".2f"), sep="")
        
        # Dollars
        dollars = int(change)
        if dollars == 1:
            print("\t\t 1 dollar")
        else:
            print("\t\t",dollars, "dollars")
        change = change - dollars

        # Quarters
        quarter = int(change//.25)
        if change >= 0.25:
            if quarter == 1:
                print("\t\t 1 quarter")
            else:
                print("\t\t",quarter, "quarters")
        else:
            print("\t\t 0 quarters")
        change = float(format(change % .25,".2f"))

        # Nickels
        nickels = int(change // 0.05)
        if change >= .05:
            if nickels == 1:
                print("\t\t 1 nickel")
            else:
                print("\t\t",nickels, "nickels")
        else:
            print("\t\t 0 nickels")
        change = float(format(change % 0.05, ".2f"))

        # Pennies
        pennies = int(change //.01)
        if pennies == 1: 
            print("\t\t 1 penny")
        else:
            print("\t\t",pennies, "pennies")

    
def high_card():
    print()
    print("* High Card *")
    
    # Ask for names
    player_1 = input("Enter name for player 1: ")
    player_2 = input("Enter name for player 2: ")


    print()
    # Deal card for player_1
    num1 = random.randint(1, 13)

    if num1 == 1:
        print(player_1, "your card is an Ace.")
    elif num1 == 2:
        print(player_1, "your card is a Two.")
    elif num1 == 3:
        print(player_1, "your card is a Three.")
    elif num1 == 4:
        print(player_1, "your card is a Four.")
    elif num1 == 5:
        print(player_1, "your card is a Five.")
    elif num1 == 6:
        print(player_1, "your card is a Six.")
    elif num1 == 7:
        print(player_1, "your card is a Seven.")
    elif num1 == 8:
        print(player_1, "your card is an Eight.")
    elif num1 == 9:
        print(player_1, "your card is a Nine.")
    elif num1 == 10:
        print(player_1, "your card is a Ten.")
    elif num1 == 11:
        print(player_1, "your card is a Jack.")
    elif num1 == 12:
        print(player_1, "your card is a Queen.")
    elif num1 == 13:
        print(player_1, "your card is a King.")


    # Deal card for player_2
    num2 = random.randint(1, 13)

    if num2 == 1:
        print(player_2, "your card is an Ace.")
    elif num2 == 2:
        print(player_2, "your card is a Two.")
    elif num2 == 3:
        print(player_2, "your card is a Three.")
    elif num2 == 4:
        print(player_2, "your card is a Four.")
    elif num2 == 5:
        print(player_2, "your card is a Five.")
    elif num2 == 6:
        print(player_2, "your card is a Six.")
    elif num2 == 7:
        print(player_2, "your card is a Seven.")
    elif num2 == 8:
        print(player_2, "your card is an Eight.")
    elif num2 == 9:
        print(player_2, "your card is a Nine.")
    elif num2 == 10:
        print(player_2, "your card is a Ten.")
    elif num2 == 11:
        print(player_2, "your card is a Jack.")
    elif num2 == 12:
        print(player_2, "your card is a Queen.")
    elif num2 == 13:
        print(player_2, "your card is a King.")

    # Who won?
    print()
    if num1 > num2:
        print(player_1, "you won!")
    if num2 > num1:
        print(player_2, "you won!")
    if num2 == num1:
        print ("You are both tied")

def display_face_value(num):
    if num == 1:
        num = "Ace"
    elif num == 2:
        num = "Two"
    elif num == 3:
        num = "Three"
    elif num == 4:
        num = "Four"
    elif num == 5:
        num = "Five"
    elif num == 6:
        num = "Six"
    elif num == 7:
        num = "Seven"
    elif num == 8:
        num = "Eight"
    elif num == 9:
        num = "Nine"
    elif num == 10:
        num = "Ten"
    elif num == 11:
        num = "Jack"
    elif num == 12:
        num = "Queen"
    elif num == 13:
        num = "King"
    print (num)  
    
def deal_hand():
    print()
    print("* Deal Hand *")
    # Need 5 random numbers between 1- 13
    print("Your cards are:")    
    num1 = random.randint(1, 13)
    display_face_value(num1)
    
    num2 = random.randint(1, 13)
    display_face_value(num2)

    num3 = random.randint(1, 13)
    display_face_value(num3)

    num4 = random.randint(1, 13)
    display_face_value(num4)

    num5 = random.randint(1, 13)
    display_face_value(num5)


         


def main():
    welcome_message()
    option = get_option()
    print()

    while option != 4:
        if option == 1: 
            make_change()
            
            option = get_option()
           
        elif option == 2:
            high_card()
            
            option = get_option()
            
        elif option == 3:
            deal_hand()
            
            option = get_option()

main()
    
    




