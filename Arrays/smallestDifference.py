def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    result = []
    l1 = 0
    l2 = 0
    smallest = float("inf")
    current = float("inf")
    while l1 < len(arrayOne) and l2 < len(arrayTwo):
        firstNum = arrayOne[l1]
        secondNum = arrayTwo[l2]
        current = abs(arrayOne[l1] - arrayTwo[l2])
        # if abs(arrayOne[l1] - arrayTwo[l2]) == 0:
        #     return [arrayOne[l1], arrayTwo[2]]
        if firstNum < secondNum:
            l1 = l1 + 1
        elif firstNum > secondNum:
            l2 = l2 + 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            result = [firstNum, secondNum]

    return result


print(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))
