'''
Preface: This file consists of the key statistics-related functions to find different values such as the median,
mean, variance, etc. 

Author: TheEmojiNinja
'''

# Required modules
import math

# The medianIndex function just returns the index of the median for a list with an odd amount of observations.
# This is not a value useful to the user but helps internally with finding the quartiles.
def medianIndex(n : int) -> int:
    if (n % 2 == 1):
        return int((n+1)/2)-1

# The medianForEvenN function finds the median for a list with an even amount of observations.
def medianForEvenN(list : list, n : int) -> int | float:
    return (list[int((n/2)-1)] + list[int(n/2)])/2

# The medianForOddN function finds the median for a list with an odd amount of observations.
def medianForOddN(list : list, n : int) -> int | float:
    return list[int((n+1)/2)-1]

# The findMean function finds the mean (average) of all the observations in the list.
def findMean(list : list, n : int) -> int | float:
    total = 0
    for obs in list:
        total += obs
    return total/n

# The findVariance function finds the variance of all the observations in the list.
# The value this function returns is also used to calculate the standard deviation.
def findVariance(list : list, mean : int | float, n : int) -> int | float:
    total = 0
    for obs in list:
        total += math.pow((obs - mean), 2)
    return total/(n-1)