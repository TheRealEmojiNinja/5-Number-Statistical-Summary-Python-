'''
Preface: This file consists of all the major functions used to navigate different parts of the main program.

Author: TheEmojiNinja
'''

# Required modules
import statistical_functions as s, math

# Important variables
q1, q3, median = None, None, None
mean, variance, standardDeviation, range = None, None, None, None

# Introduction function that simply welcomes the user and informs them the purpose of this program
def intro() -> None:
    print("Welcome to the Five-Number Summary program.")
    print("This program takes an input of a list of numbers (not required to be sorted) from the user (you!) \nIn order to calculate the Five-Number Summary (Minimum, Q1, Median, Q3, Maximum).")
    print("Additionally it will display the Mean (average), Standard Deviation, Range and Variance for your convenience.")

# The splitOddList function splits a list with an odd amount of observations into two equal halves by
# not including the median within either list. 
def splitOddList(list : list, first : list, second : list, medianIndex : int) -> None:
    i = 0
    for obs in list:
        if i == medianIndex:
            pass
        elif i < medianIndex:
            first.append(obs)
        elif i > medianIndex:
            second.append(obs)
        i += 1

# The splitEvenList function splits a list with an even amount of observations into two equal halves by
# comparing the size of the observation with the median.
def splitEvenList(list : list, first : list, second : list, median : int | float) -> None:
    for obs in list:
        if obs < median:
            first.append(obs)
        elif obs > median:
            second.append(obs)

# The processOddList function is the main function that actually finds most of the useful values for the user.
# This method is called when dealing with a list containing an odd amount of observations. It first calculates
# the median before splitting the list into two equal halves utilizing the methods above, which it then uses to
# find the quartiles.
def processOddList(list : list, n : int) -> None:
    global median, q1, q3
    firstHalf, secondHalf = [], []

    median = s.medianForOddN(list, n)
    medianLocation = s.medianIndex(n)

    splitOddList(list, firstHalf, secondHalf, medianLocation)

    if (len(firstHalf) % 2 == 1):
        q1 = s.medianForOddN(firstHalf, len(firstHalf))
        q3 = s.medianForOddN(secondHalf, len(secondHalf))
    else:
        q1 = s.medianForEvenN(firstHalf, len(firstHalf))
        q3 = s.medianForEvenN(secondHalf, len(secondHalf))
        
# The processEvenList function is the main function that actually finds most of the useful values for the user.
# This method is called when dealing with a list containing an even amount of observations. It first calculates
# the median before splitting the list into two equal halves utilizing the methods above, which it then uses to
# find the quartiles.
def processEvenList(list : list, n : int) -> None:
    global median, q1, q3
    firstHalf, secondHalf = [], []

    median = s.medianForEvenN(list, n)

    splitEvenList(list, firstHalf, secondHalf, median)

    if (len(firstHalf) % 2 == 1):
        q1 = s.medianForOddN(firstHalf, len(firstHalf))
        q3 = s.medianForOddN(secondHalf, len(secondHalf))
    else:
        q1 = s.medianForEvenN(firstHalf, len(firstHalf))
        q3 = s.medianForEvenN(secondHalf, len(secondHalf))

# The processAdditionalInformation function calculates the mean (average), variance, standard deviation and the range.
def processAdditionalInformation(list : list, n : int) -> None:
    global mean, variance, standardDeviation, range
    mean = s.findMean(list, n)
    variance = s.findVariance(list, mean, n)
    standardDeviation = math.sqrt(variance)
    range = list[n-1] - list[0]

# The sortAndPrintList function sorts the list of observations into ascending order and prints it out.
def sortAndPrintList(list : list) -> None:
    list.sort()
    print("Your sorted list in ascending order is: ", end='')
    for obs in list:
        print(obs, end=' ')

# The userConfirmation function checks whether the user enters 'Y' for yes or 'N' for no, and returns a
# boolean value as such.
def userConfirmation(response : str) -> bool:
    if (response == 'Y'):
        return True
    elif (response == 'N'):
        return False
    else:
        print("Enter a valid response!")

# The fiveNumberSummary function prints all the values included in the Five-Number Summary
# (minimum, Q1, median, Q3, and the maximum).
def fiveNumberSummary(list : list, n : int) -> None:
    global q1, median, q3
    print("Minimum: " + str(list[0]))
    print("Q1: " + str(q1))
    print("Median: " + str(median))
    print("Q3: " + str(q3))
    print("Maximum: " + str(list[n-1]))

# The additionalInformation function prints all the other values (mean, variance, standard deviation and the range).
def additionalInformation():
    global mean, variance, standardDeviation, range
    print("Mean: " + str(mean))
    print("Variance: " + str(variance))
    print("Standard Deviation: " + str(standardDeviation))
    print("Range: " + str(range))




            

            
