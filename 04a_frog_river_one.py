def solution(X, A):

    # Create an empty dictionary to store {leaf: last_timing}
    leaves = {}

    # Loop through each given leaf with an index
    for timing, leaf in enumerate(A):

        # Assign the last timing for each leaf number
        leaves[leaf] = timing

        # If there are at least one leaf for each position
        if len(leaves) == X:

            # Return the timing
            return timing

    # If there are at least one empty position with no leaves, return -1
    return -1
