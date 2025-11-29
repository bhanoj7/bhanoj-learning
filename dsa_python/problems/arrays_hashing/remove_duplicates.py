def remove_duplicates(nums):
    # keep original order
    seen = set()
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen.add(nums[i])
            i+=1
        else:
            nums.pop(i)
    return nums
if __name__ == "__main__":
    nums = [9,2,3,1,2,13,7,1]
    print(remove_duplicates(nums))