def two_sum(nums,target):
    num_index = {}
    for index, num in enumerate(nums):
        if target-num in num_index:
            return [num_index[target-num],index]
        num_index[num] = index
# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))   # Output: [0, 1]