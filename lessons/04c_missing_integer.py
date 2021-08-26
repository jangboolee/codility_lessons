def solution(A):

    # Create a unique set of the values in A
    unique_A = set(A)

    # Return 1 if none of the values are greater than 0
    if max(unique_A) < 0:
        return 1
    
    else:
        
        # Initialize a dictionary of all of the numbers that should be found
        counter = {num + 1: 0 for num in range(len(unique_A)+1)}
        
        # Flag the values that have been found
        for num in unique_A:
            counter[num] = 1
        
        # Return the number that was not found
        for k, v in counter.items():
            if v == 0:
                return k
