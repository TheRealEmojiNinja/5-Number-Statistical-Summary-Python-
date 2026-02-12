'''
Preface: This program allows the user to input observations (elements) of a list to find the Five-Number Summary.
The observations may be either of type INT or FLOAT. Additionally, the program will display the mean, range,
variance and the standard deviation. 

Author: TheEmojiNinja
'''

# Required modules
import functions as f

# Key variables
DATATYPELIST = ['I', 'F']

number = None
numberList = []

mainLoopRunning, choosingDataType, addingObs, confirming, exiting = True, True, True, True, True

confirmation = None

# Calls the intro method to welcome the user.
f.intro()

# Main while loop that handles the entire program.
while mainLoopRunning:

    # Block of code to obtain the specific data type of observations the user wants to input (INT or FLOAT).
    print("Please specify whether your data consists of integers or floats (type I or F): ")
    while choosingDataType:
        type = input("> ")
        if (type not in DATATYPELIST):
            print("Enter \'I\' for integer or \'F\' for float!")
        else:
            break
    
    # Block of code to enter all the observations into a list one by one (minimum of 2).
    print("Please enter your list of numbers (type DONE when you finish): ")
    while addingObs:
        number = input("> ")
        try:
            if (number == 'DONE' and len(numberList) > 1):
                break
            elif (number == 'DONE' and len(numberList) < 2):
                print("You need to add at least two numbers!")
            else:
                if (type == 'I'):
                    number = int(number)
                elif (type == 'F'):
                    number = float(number)
        except ValueError:
            print("Enter a valid number!")
            continue
        numberList.append(number)
    
    # Calls the sort and print list method to sort and print the list.
    f.sortAndPrintList(numberList)

    # Block of code to confirm the user's list, otherwise it can be reentered 
    # (program starts over from the data type block of code).
    print("\nConfirm your list (Y/N): ")
    while confirming:
        response = input("> ")
        confirmation = f.userConfirmation(response)
        if (confirmation != None):
            break
    if (not confirmation):
        numberList = []
        confirmation = None
        continue

    # Assigning n the total number of elements in the list.
    n = len(numberList)

    # Processing the list and finding the Five-Number Summary depending on whether it has an 
    # even or odd amount of elements.
    if (n % 2 == 1):
        f.processOddList(numberList, n)
    else:
        f.processEvenList(numberList, n)

    # Processing the additional information (mean, variance, range, standard deviation).
    f.processAdditionalInformation(numberList, n)

    # Printing the values for each.
    print("\n—Your Five-Number Summary—\n")
    f.fiveNumberSummary(numberList, n)
    
    print("\n—Additional Information—\n")
    f.additionalInformation()
    
    # Block of code to ask the user if they want to enter another list 
    # (program starts over from the data type block of code).
    print("\nEnter another list? (Y/N): ")
    while exiting:
        response = input("> ")
        confirmation = f.userConfirmation(response)
        if (confirmation != None):
            break
    if (confirmation):
        numberList = []
        confirmation = None
        continue
        
    # Exit the main while loop if the user enters 'N'.
    break

# Prints an exit message before ending the program.
print("Thank you for using this program! Hope you enjoyed!")

exit()