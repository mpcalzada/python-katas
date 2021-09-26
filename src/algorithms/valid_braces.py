# Write a function that takes a string of braces, and determines if the order of the braces is valid. 
# It should return true if the string is valid, and false if it's invalid.
# 
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], 
# and curly braces {}. Thanks to @arnedag for the idea!
# 
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly 
# braces: ()[]{}.
# 
# What is considered Valid?
# 
# A string of braces is considered valid if all braces are matched with the correct brace.
# 
# Examples
# 
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

from typing import Deque

def validBraces(string):
    stack = Deque()
    braces = {"}": "{", "]": "[", ")": "(",}
    print(string)
    print(braces.values())
    print(braces.keys())
    for letter in string:
        if letter in braces.values(): stack.append(letter)
        elif letter in braces.keys() and (len(stack) == 0 or stack.pop() != braces[letter]): return False
    return len(stack) == 0

if __name__ == "__main__":
    print(validBraces(")(}{]["))