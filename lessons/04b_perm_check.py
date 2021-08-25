def solution(A):

    # Create a list to count elements in A
    counter = [0] * len(A)

    # Loop through elements
    for i in A:

        # Exit loop if any elements are less than 1 or skip numbers
        if i < 1 or i > len(A):
            return 0
        
        # If the element is within range
        else:

            # Exit loop if the element has already been counted
            if counter[i-1] != 0:
                return 0
            
            # Add count of the element by 1
            else:
                counter[i-1] += 1

    # If the loop finishes without any exceptional cases
    return 1
  
