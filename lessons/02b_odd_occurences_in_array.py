def solution(A):

    # One-liner solution
    # return [item for item in A if A.count(item) % 2 == 1][0]

    # More efficient solution that passes time complexity requirement
    count_dict = {}
    for item in A:
        # If the item has not been added already
        if item not in count_dict.keys():
            # Add the item as a key and assign a count value of 1
            count_dict[item] = 1
        # If the item has already been added
        else:
            # Increment the count value by one
            count_dict[item] += 1

    # Find the key with an odd count
    for k, v in count_dict.items():
        if v % 2 == 1:
            return(k)
