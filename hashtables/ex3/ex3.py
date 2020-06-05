def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    inAllThree = []
    matchLimit = len(arrays)
    for arr in arrays:
        for i in arr:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
                if cache[i] == matchLimit:
                    inAllThree.append(i)
    return inAllThree

    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
