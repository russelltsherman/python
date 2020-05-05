
def bubbleSort(arr):
    n = len(arr)  # store array length
    rng = n-1  # store array range

    swaps = 0
    # Traverse through all array elements
    for i in range(rng):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, rng-i):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return(swaps)
