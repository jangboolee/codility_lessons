def solution(A):

    # Pre-calculate initial sum values of each tape piece
    left_sum = 0
    right_sum = sum(A)

    # Create a list of the difference for each possible P value
    diffs = []
    for P in range(0, len(A)-1):
        left_sum += A[P]
        right_sum -= A[P]
        diffs.append(abs(left_sum - right_sum))

    return min(diffs)
