 #You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


# Given a full name, your task is to capitalize the name appropriately.

 # 3Input Format

# A single line of input containing the full name, .

# Constraints

# The string consists of alphanumeric characters and spaces.
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

#Output Format

#Print the capitalized string, .

#Sample Input

#chris alan
#Sample Output

#Chris Alan
#Contest ends in 17 hours
#Submissions: 81
#Max Score: 10
#Difficulty: Easy
#Rate This Challenge:

    
#More
 
#1
#!/bin/python3
2
3​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
# Complete the solve function below.
9
def solve(s):
    def solve(r):
    for y in s[:].split():
        r = r.replace(y, y.capitalize())
    return r
