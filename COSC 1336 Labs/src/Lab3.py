#####################################
# Ruvi Jaimes                       #
# Lab  3                            #
# This program will let user choose #
# the menu option. If user chooses  #
# option 1, they will be able to    #
# input amount owed and amount paid #
# to find how many dollar bills,    #
# quarters, nickels, and pennies    #
# are owed                          #
#####################################

# Welcome message 
print("Welcome to 'Lame Game,' this program will display the menu options \
and allow the user to choose their option.")

# Display menu options
print("Game Menu:")
print("1. Make Change")
print("2. High Card")
print("3. Quit")

# Ask user to choose option
option = int(input("Enter menu option: "))

####### Options #######

## Option 1
if option == 1:
    money_owed = float(input("Enter amount owed: "))
    money_paid = float(input("Enter amount paid: "))

# If change is change is greater than paid

    if money_paid < money_owed:
        print("You have not payed enough.")

    else:
# math equation
        change= money_paid - money_owed
        print("You owe the customer $", format(change,".2f"), sep="")
        print("$", format(change,".2f"), sep="")
        dollars = int(change)
        if dollars == 1:
            print("1 dollar")
        else:
            print(dollars, "dollars")

           
        # Will have to divide by 25, 5, 1
        change = change - dollars
        quarter = int(change // .25)
        if quarter == 1:
            print("1 quarter")
        else:
            print(quarter, "quarters")
        change = change - .25*quarter
        nickels = int(change //.05)
        if nickels == 1:
            print("1 nickel")
        else:
            print(nickels, "nickels")
        change = change - .05*nickels
        pennies = int(change //.01)
        if change!= 0 and change != 1 and change!= 2 and change!= 3 and change!=4:
            print( pennies + 1, "pennies")
        else:
            if pennies == 1: 
                print("1 penny")
            else:
                print(pennies, "pennies")

# Option 2
elif option == 2:
    print("High Card is coming soon.")

# Option 3

# Invalid Number
elif option < 1 or option > 3:
    print("Invalid Option")





