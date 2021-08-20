def solution(N):
    
    # Convert int to binary string
    binary_string = f'{N:b}'
    
    # For cases with less than two 1s
    if binary_string.count('1') < 2:
        return 0
    
    # For other cases
    else:
    
        # Find the indices of all 1s
        indices = [i for i, letter in enumerate(binary_string) if letter == '1']

        # Find the gaps between the indices of all 1s
        gaps = []
        for i in range(len(indices)-1):  
            gaps.append(indices[i+1] - indices[i] - 1)

        return max(gaps)
