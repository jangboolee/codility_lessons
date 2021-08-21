def solution(A):

    # Use the Gaussian formula to find the sum of the list with the missing element
    expected_sum = ((len(A) + 1) * (len(A) + 2))/2
    
    # Find the actual sum of the list
    actual_sum = sum(A)

    # Return the missing element
    return int(expected_sum - actual_sum)
