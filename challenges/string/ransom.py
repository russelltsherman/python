
"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No.

"""


# second iteration
def ransom(magazine, note):
    for word in note:  # iterate words in desired message
        try:
            magazine.remove(word)  # remove word from a2 if it exists
        except ValueError:
            return "No"  # word not found in a2
    return "Yes"

# first iteration - two test failures Your code did not execute within the time limits
# def ransom(magazine, note):
#     for word in note:  # iterate words in desired message
#         try:
#             magazine.index(word)  # check for match in a2
#             magazine.remove(word)  # remove word from a2
#         except ValueError:
#             return "No"  # word not found in a2
#     return "Yes"
