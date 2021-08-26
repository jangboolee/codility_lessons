def solution(N, A):

    # Initialize counters and trackers
    counters = [0] * N
    current_max = 0
    max_val = 0

    for i in A:

        # If the operation meets the first condition
        if 1 <= i <= N:

            # If the max value is greater than the counter
            if max_val > counters[i-1]:
            
                # Set the max value as the counter value
                counters[i-1] = max_val
            
            # Increase the count of the counter
            counters[i-1] += 1

            # If the new value is greater than the current max value
            if current_max < counters[i-1]:

                # Update the current max value
                current_max = counters[i-1]

        # If the operation meets the second condition
        elif i == N + 1:

            # Set the max value to increase all elements by to the current max value
            max_val = current_max

    return [max(max_val, i) for i in counters]
