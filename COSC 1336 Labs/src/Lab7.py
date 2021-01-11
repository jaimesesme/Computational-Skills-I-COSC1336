########################################################
# Ruvi Jaimes                                          #
# Lab  7: COSC 1336                                    #
# This program displays the menu:                      #
# 1. Make Change                                       #
# 2. High Card                                         #
# 3. Quit                                              #
# Asks the user for option at the begging of game      #
# and after the game chosen ends.                      #
#                                                      #
# Make Change: asks the user for the money owed and    #
# given, then it gives how many dollars, quarters,     #
# nickels, and pennies are needed for change           #
#                                                      #
# High Card: asks both users for names, randomly       #
# distributes cards to players, displays what card     #
# they got (ex. Mike your card is a King), and finally #
# displays the winner of who got the highest card.     #
#                                                      #
# Deal Hand: gives the user 5 cards and displays       #
# the value of the card                                #
#                                                      #
# Save Dream Hand: asks the user to enter 5 cards,     #
# then asks for the file name which he/she will like   #
# to export the cards to.                              #
#                                                      #
# Display Dream Hand: will open the file and display   #
# the card values.                                     #
########################################################

import random

def main():
    welcome_message()
    option = get_option()
    print()
    while option != 6:
        if option == 1: 
            make_change()
        elif option == 2:
            high_card()     
        elif option == 3:
            stats = deal_hand()
            for i in range (5):
                display_face_value(stats[i])
            hand_stats(stats)
        elif option == 4:
            save_dream_hand()
        elif option == 5:
            display_dream_hand()
            option = get_option()
        option = get_option()


#############################################           
# Funtion: welcome_message                  #
# Input: none                               #
# Outputs: none                             #
# Description: displays the menu and tells  #
# what program is about                     #
#############################################

def welcome_message():
    print("-------------------------------------------------")
    print("-          * Welcome to Lame Game. *            -")
    print("-                                               -")
    print("-    This program displays the game menu:       -")
    print("-            Game Menu:                         -")
    print("-            1. Make Change                     -")
    print("-            2. High Card                       -")
    print("-            3. Deal Hand                       -")
    print("-            4. Save Dream Hand                 -")
    print("-            5. Display Dream Hand              -")
    print("-            6. Quit                            -")
    print("-                                               -")
    print("-    Then prompts for option to play the game   -")
    print("-                                               -")
    print("-------------------------------------------------")

    
#############################################           
# Funtion: get_option                       #
# Input: none                               #
# Outputs: option                           #
# Description: displays the menu and asks   #
# the user for their option. It also        #
# checks for invalid options                #
#############################################

def get_option():
    try:
        print()
        print("Game Menu:")
        print("1. Make Change")
        print("2. High Card")
        print("3. Deal Hand")
        print("4. Save Dream Hand")
        print("5. Display Dream Hand")
        print("6. Quit")
        # Ask user to choose option
        option = int(input("Enter menu option: "))
        # Check invalid options
        while option < 1 or option > 6:
            print()
            print("ERROR: Invalid Option. Enter an integer 1-5 or 6 to quit.")
            print()
            print("Game Menu:")
            print("1. Make Change")
            print("2. High Card")
            print("3. Deal Hand")
            print("4. Save Dream Hand")
            print("5. Display Dream Hand")
            print("6. Quit")
        # Ask user to choose option
            option = int(input("Enter menu option: "))
    except ValueError as err:
        print(err)
        option = 0

    return option

#############################################           
# Funtion: make_change                      #
# Input: none                               #
# Outputs: none                             #
# Description: asks the user for the amount #
# owed and paid, then gives the change in   #
# dollars, quarter, nickels, and pennies    #
# also checks for an invalid input for      #
# the amount paid                           #
#############################################

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


#############################################           
# Funtion: high_card                        #
# Input: none                               #
# Outputs: none                             #
# Description: promts for player 1 and      #
# player 2's names, generates two random    #
# numbers between 1 - 13, displays value of #
# cards, and displays who wins              #
#############################################

def high_card():
    print()
    print("* High Card *")
    
    # Ask for names
    player_1 = input("Enter name for player 1: ")
    player_2 = input("Enter name for player 2: ")


    print()
    # Deal card 
    num1 = random.randint(1, 13)
    num2 = random.randint(1, 13)
    

    print(player_1, ", your card is: ", sep="", end="")
    display_face_value(num1)

    print(player_2, ", your card is: ", sep="", end= "")
    display_face_value(num2)

    # Who won?
    print()
    if num1 > num2:
        print(player_1, "you won!")
    if num2 > num1:
        print(player_2, "you won!")
    if num2 == num1:
        print ("You are both tied")


#############################################           
# Funtion: display_face_value               #
# Input: number                             #
# Outputs: value of number                  #
# Description: takes the number and returns #
#  it as a value                            #
#############################################

def display_face_value(num):
    if num == 1:
        print("Ace")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    elif num == 4:
        print("Four")
    elif num == 5:
        print("Five")
    elif num == 6:
        print( "Six")
    elif num == 7:
        print("Seven")
    elif num == 8:
        print("Eight")
    elif num == 9:
        print( "Nine")
    elif num == 10:
        print("Ten")
    elif num == 11:
        print("Jack")
    elif num == 12:
        print("Queen")
    elif num == 13:
        print("King")
    


#############################################           
# Funtion: deal_hand                        #
# Input: none                               #
# Outputs: list rand_num                    #
# Description: generates five random        #
# numbers from 1 - 13                       #
#############################################

def deal_hand():
    print()
    print("* Deal Hand *")
    
    # Need 5 random numbers between 1- 13
    print("Your cards are:")

    rand_num = [ ]

    for i in range(5):
        number = random.randint(1,13)
        rand_num.append(number)

    return rand_num

#############################################           
# Funtion: hand_stats                       #
# Input: numbers from list rand_num         #
# Outputs: none                             #
# Description: calculates the total value   #
# of all the numbers and averages the value #
# of the cards by adding all cards and      #
# dividing by 5. Displays total and average #
#############################################
    
def hand_stats(list1):
    print()
    total = list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
    print ("Your total is ", total)
    average = total/5
    print ("Your average is ", average)


#############################################           
# Funtion: save_dream_hand                  #
# Input: none                               #
# Outputs: none                             #
# Description: asks the user for 5 numbers  #
# from 1 -13, puts the numbers in a list,   #
# and then exports the list to the file     #
# that the user has chosen.                 #
#############################################
    
def save_dream_hand():

    print()
    print("* Save Dream Hand *")
    
    try:
        card_list=[ ]
        for i in range(5):
            card = int(input("Enter card value for dream hand (1-13) : "))
            while card > 13 or card <= 0:
                print("ERROR:Invalid Answer.")
                card = int(input("Enter card value for dream hand (1-13) : "))
            card_list.append(card)          
        name = str(input("Enter name for file: "))
        name = name + ".txt"
        outfile = open(name, "w")
        for i in range(5):
            outfile.write(str(card_list[i])+"\n") #ri.txt
        outfile.close()
        print("Your file, ", name, "has been saved.")
                
    except ValueError as err:
        print(err)


#############################################           
# Funtion: display_dream_hand               #
# Input: none                               #
# Outputs: none                             #
# Description: asks user for the file name, #
# opens it up, and displays the value of    #
# cards                                     #
#############################################
        
def display_dream_hand():
    
    print("* Display Dream Hand *")
    try:
        filename = input("Enter file name: ")
        infile = open(filename, "r")
        print()
        print("Your Dream Hand Cards are:")
        for i in range(5):
            card = infile.readline()
            card = card.rstrip("\n")
            display_face_value(int(card))
        infile.close()
        
    except FileNotFoundError as err:
        print(err)


main()
    
    




