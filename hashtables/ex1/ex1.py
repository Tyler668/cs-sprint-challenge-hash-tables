def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    for i in range(length):
        remainderNeeded = limit - weights[i]
        cache[i] = (remainderNeeded)
        if i > 0:
            if (limit - remainderNeeded) in cache.values():
                matchIndex = (list(cache.keys())[list(cache.values()).index(limit - remainderNeeded)])
                if (matchIndex) > (i):
                    return [matchIndex, i]
                else:
                    return [i, matchIndex] 
            

weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
length = 9
limit = 7
print(get_indices_of_item_weights(weights, length, limit))

        #         

    # return None
