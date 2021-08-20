def solution(A, K):

    # Create a blank list with 0 as default values with the same length as A
    rotated = [0] * len(A)

    # Return the same list if there is no or one element in the list
    if len(A) < 1:
        return A

    # Adjust K if K is longer than A
    if K > len(A):
        K  = K % len(A)

    # Loop through each index for each element in A
    for i in range(len(A)):
        
        # If the item only needs to be moved right
        if i + K < len(A):
            rotated[i+K] = A[i]

        # If the item needs to be moved left and then right
        else:
            rotated[i-len(A)+K] = A[i]

    return rotated
