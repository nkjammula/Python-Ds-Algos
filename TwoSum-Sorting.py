def twoSumNumbers(array, targetSum):

    # 5,8,9,2,4     9
    # after sorting  2,4,5,8,9
    # two piointer

    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right = right - 1
        else:
            left = left + 1
    return[]


print(twoSumNumbers([5, 8, 9, 2, 4], 9))
