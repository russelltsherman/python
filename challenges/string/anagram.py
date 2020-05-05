"""
Anagram Substring Search (Or Search for all permutations)

Given a text haystack[0..n-1] and a pattern needle[0..m-1]

write a function search(char needle[], char haystack[]) that prints all occurrences of needle[] and its permutations (or anagrams) in haystack[]. 

You may assume that n > m.

"""

MAX = 128


def compare(a, b):
    """
    return true if contents of a[] and b[] are same.
    """
    for i in range(MAX):
        if a[i] != b[i]:
            return False
    return True


def anagram(needle, haystack):
    """
    search for all permutations of needle[] in haystack[]
    """
    needle_len = len(needle)
    haystack_len = len(haystack)

    countP = [0]*MAX  # Store count of all characters of pattern
    countTW = [0]*MAX  # Store count of current window of text

    finds = []

    for i in range(needle_len):
        countP[ord(needle[i])] += 1
        countTW[ord(haystack[i])] += 1

    # iterate remaining characters of pattern
    for i in range(needle_len, haystack_len):
        # Compare counts of current indow of text
        # with counts of pattern[]
        if compare(countP, countTW):
            finds.append(i-needle_len)

        # Add current character to current window
        countTW[ord(haystack[i])] += 1

        # Remove the first character of previous window
        countTW[ord(haystack[i-needle_len])] -= 1

    # Check for the last window in text
    if compare(countP, countTW):
        finds.append(haystack_len-needle_len)

    return(finds)
