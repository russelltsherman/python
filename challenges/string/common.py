
"""
Given two strings, determine if they share a common substring. 
A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring a. 
The words "be" and "cat" do not share a substring.

Function Description

Complete the function common below. 
It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze.
"""


def common(s1, s2):
    if (set(s1) & set(s2)):
        return("YES")
    return("NO")
