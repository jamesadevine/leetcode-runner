import random

values = [i for i in range(10)]
target = random.randint(0, 15)


def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle

        if target < values[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(binary_search(values, target))
