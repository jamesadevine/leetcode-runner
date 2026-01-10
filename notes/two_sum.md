# two sum

Very straightforward problem.

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

## n^2 solution

```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        num1 = nums[i]
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if target == num1 + num2:
                return [i, j]
    return []
```

## Constant time solution

Essentially a hash map. When iterating, check if the complement of the number exists in the hash map: target - current_num. If it does, then report index store in the hash map and the current number. Otherwise, store the current number and index in hash map.