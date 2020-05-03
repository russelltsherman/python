
"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! 
There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. 
Initial positions increment by 1 from 1 at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. 
If two people swap positions, they still wear the same sticker denoting their original places in line. 
One person can bribe at most two others.

Write a function that evaluates the current order of the queue and returns the number of bribes required to attain current state.
If the current state of the queue indicates that more bribes than allowed have happened return -1

"""


def chaos(q):
    swapcount = 0

    for i in reversed(range(len(q))):
        cpos = i+1  # correct for 0 based index
        opos = q[i]

        # ignore element if queue position has not changed
        if (opos == cpos):
            continue

        if (cpos == q[i-1]):
            # current positin matches previous element (one bribe)
            swapcount += 1
            # restore order
            q[i], q[i-1] = q[i-1], q[i]
        elif (cpos == q[i-2]):
            # current positin matches second previous element (two bribes)
            swapcount += 2
            # restore order
            q[i], q[i-2] = q[i-2], q[i]
            q[i-1], q[i-2] = q[i-2], q[i-1]
        else:
            # no matches suggest too many bribes happened
            return(-1)

    return(swapcount)
