
def is_weird(n):
    if n % 2 == 1:  # is odd number
        return("Weird")
    else:  # is even number
        if n >= 2 and n <= 5:
            return("Not Weird")
        elif n >= 6 and n <= 20:
            return("Weird")
        else:
            return("Not Weird")
