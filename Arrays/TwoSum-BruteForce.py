def twoSumNumbers(array, targetSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j] == targetSum and i != j):
                return [array[i], array[j]]

    return []


print(twoSumNumbers([1, 2, 3, 4], 5))
