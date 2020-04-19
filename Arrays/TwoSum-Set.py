def twoSumNumbers(array, targetSum):
    numberSet = set()
    for i in range(len(array)):
        if ((targetSum - array[i]) in numberSet):
            return[array[i], targetSum-array[i]]
        numberSet.add(array[i])
    return []


print(twoSumNumbers([1, 2, 3, 4], 4))
