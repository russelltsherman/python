
"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example s = mom, the list of all anagrammatic pairs is [m,m],[mo,om] at positions [[0],[2]],[[0,1],[1,2]] respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in .

sherlockAndAnagrams has the following parameter(s):

s: a string.

"""


def sherlockAndAnagrams(s):
    n = len(s)  # get length of string
    count = 0  # initialize result
    tmp = {}  # initialize dict
    for i in range(1, n):  # for length of string
        for j in range(n-i+1):  # take progressively bigger bytes
            subs = ''.join(sorted(s[j:j+i]))
            # sorted byte as key of dict
            # value is count byte observations
            if subs in tmp:  # increment if exists
                tmp[subs] += 1
            else:  # else initialize
                tmp[subs] = 1
            count += tmp[subs] - 1  # increment result if count is
    return(count)
