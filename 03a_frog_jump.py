def solution(X, Y, D):

    # The total distance needed to travel by the frog
    travel_distance = Y - X
    
    # Add 1 if there is a remainder to the number of jumps (True = 1)
    return travel_distance // D + (travel_distance % D > 0)
