########################################################
# Ruvi Jaimes                                          #
# Lab  4: COSC 1336                                    #
# This program displays the menu:                      #
# 1. Make Change                                       #
# 2. High Card                                         #
# 3. Quit                                              #
# Asks the user for option at the begging of game      #
# and after the game chosen ends.                      #
#                                                      #
# Plays game                                           #
#                                                      #
# High Card: asks both users for names, randomly       #
# distributes cards to players, displays what card     #
# they got (ex. Mike your card is a King), and finally #
# displays the winner of who got the highest card.     #
########################################################

import random

# Welcome message
print("-------------------------------------------------")
print("-          * Welcome to Lame Game. *            -")
print("-    This program displays the game menu and    -")
print("-    then promts for option to play the game    -")
print("-                   chosen.                     -")
print("-------------------------------------------------")
print()
# Display menu options
print("Game Menu:")
print("1. Make Change")
print("2. High Card")
print("3. Quit")

# Ask user to choose option
option = int(input("Enter menu option: "))
print()
print("---------------------")
print()

# Invalid Number
while option < 1 or option > 3:
    print("Invalid Option")
# Display menu options
    print()
    print("Game Menu:")
    print("1. Make Change")
    print("2. High Card")
    print("3. Quit")
    option = int(input("Enter menu option: "))
    print()
    print("---------------------")
    print()
    
while option == 1 or option == 2:

    ####### Options #######

    ## Option 1
    
    while option == 1:
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
            
            # Display to user
            print("You owe the customer $", format(change,".2f"), sep="")
            print("$", format(change,".2f"), sep="")
            
            # Dollars
            dollars = int(change)
            if dollars == 1:
                print("1 dollar")
            else:
                print(dollars, "dollars")
            change = change - dollars

            # Quarters
            quarter = int(change//.25)
            if change >= 0.25:
                if quarter == 1:
                    print("1 quarter")
                else:
                    print(quarter, "quarters")
            else:
                print("0 quarters")
            change = float(format(change % .25,".2f"))

            # Nickels
            nickels = int(change // 0.05)
            if change >= .05:
                if nickels == 1:
                    print("1 nickel")
                else:
                    print(nickels, "nickels")
            else:
                print("0 nickels")
            change = float(format(change % 0.05, ".2f"))

            # Pennies
            pennies = int(change //.01)
            if pennies == 1: 
                print("1 penny")
            else:
                print(pennies, "pennies")
        

        # Display menu options
        print()
        print("---------------------")
        print()
        print("Game Menu:")
        print("1. Make Change")
        print("2. High Card")
        print("3. Quit")

        # Ask user to choose option
        option = int(input("Enter menu option: "))
        print()
    
        # Invalid Number
        while option < 1 or option > 3:
            print("---------------------")
            print()
            print("Invalid Option")
            # Display menu options
            print()
            print("Game Menu:")
            print("1. Make Change")
            print("2. High Card")
            print("3. Quit")
            option = int(input("Enter menu option: "))
            print()
            print("---------------------")
            print()

    # Option 2
    while option == 2:
        print("* High Card *")
        
        #ask for names
        player_1 = input("Enter name for player 1: ")
        player_2 = input("Enter name for player 2: ")
       

        #deal card for player_1
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
            
        # Display menu options
        print()
        print("---------------------")
        print()
        print("Game Menu:")
        print("1. Make Change")
        print("2. High Card")
        print("3. Quit")
        # Ask user to choose option
        option = int(input("Enter menu option: "))
        print()
        print("---------------------")
        print()
        # Invalid Number
        while option < 1 or option > 3:
            print("Invalid Option")
            # Display menu options
            print()
            print("Game Menu:")
            print("1. Make Change")
            print("2. High Card")
            print("3. Quit")
            option = int(input("Enter menu option: "))
            print()
            print("---------------------")
            print()


# Option 3






