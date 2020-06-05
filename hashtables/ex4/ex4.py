def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    posAndNeg = []
    for i in a:
        if i not in cache and -i not in cache:
            cache[i] = i
        else:
            if i > 0:
                posAndNeg.append(i)
            else:
                posAndNeg.append(-i)
        
        

    return posAndNeg


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
