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

def main():
    welcome_message()

    option = get_option()

    
    
    print()

    while option != 6:
        if option == 1: 
            make_change()
            
            option = get_option()
           
        elif option == 2:
            high_card()
            
            option = get_option()
            
        elif option == 3:
            deal_hand()
            
            option = get_option()
            
        elif option == 4:
            save_dream_hand()
            
            option = get_option()
            
        elif option == 5:
            display_dream_hand()
            
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
        return option
    except ValueError as err:
        print(err)
        

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
# Outputs: none                             #
# Description: generates five random        #
# numbers from 1 - 13, and displays their   #
# value                                     #
#############################################

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
     


#############################################           
# Funtion: save_dream_hand                  #
# Input: none                               #
# Outputs: card1, card2, card3, card4.      #
# card5 (numbers 1 - 13)                    #
# Description: asks the user for 5 numbers  #
# from 1 -13, converts the numbers into the #
# value, asks user for file name, and       #
# exports the value into that file          #
#############################################
    
def save_dream_hand():

    print()
    print("* Save Dream Hand *")

    try:

        card1 = int(input("Enter card value for dream hand (1-13) : "))
        while card1 > 13 or card1 <= 0:
            print("ERROR:Invalid Answer.")
            card1 = int(input("Enter card value for dream hand (1-13) : "))
       
        
        card2 = int(input("Enter card value for dream hand (1-13) : "))
        while card2 > 13 or card2 <= 0:
            print("ERROR:Invalid Answer.")
            card2 = int(input("Enter card value for dream hand (1-13) : "))
        

        
        card3 = int(input("Enter card value for dream hand (1-13) : "))
        while card3 > 13 or card3 <= 0:
            print("ERROR:Invalid Answer.")
            card3 = int(input("Enter card value for dream hand (1-13) : "))
       
        
        card4 = int(input("Enter card value for dream hand (1-13) : "))
        while card4 > 13 or card4 <= 0:
            print("ERROR:Invalid Answer.")
            card4 = int(input("Enter card value for dream hand (1-13) : "))
       
        
        card5 = int(input("Enter card value for dream hand (1-13) : "))
        while card5 > 13 or card5 <= 0:
            print("ERROR:Invalid Answer.")
            card5 = int(input("Enter card value for dream hand (1-13) : "))
       


        name = str(input("Enter name for file: "))

        name = name + ".txt"

        outfile = open(name, "w")



        outfile.write(str(card1) + "\n")
        outfile.write(str(card2) + "\n")
        outfile.write(str(card3) + "\n")
        outfile.write(str(card4) + "\n")
        outfile.write(str(card5) + "\n")

        
        outfile.close()

        print("Your file, ", name, "has been saved.")
                
    except ValueError as err:
        print(err)


#############################################           
# Funtion: display_dream_hand               #
# Input: none                               #
# Outputs: none                             #
# Description: asks user for the file name  #
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


        card1 = infile.readline()
        card1 = card1.rstrip("\n")
        display_face_value(int(card1))
        
        card2 = infile.readline()
        card2 = card2.rstrip("\n")
        display_face_value(int(card2))
        
        card3 = infile.readline()
        card3 = card3.rstrip("\n")
        display_face_value(int(card3))
        
        card4 = infile.readline()
        card4 = card4.rstrip("\n")
        display_face_value(int(card4))
        
        card5 = infile.readline()
        card5 = card5.rstrip("\n")
        display_face_value(int(card5))

        infile.close()
    except FileNotFoundError as err:
        print(err)




main()
    
    




