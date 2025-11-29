def remove_duplicates(nums):
    # keep original order
    seen = {}
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen[nums[i]] = seen.get(nums[i],0)+1
            i+=1
        else:
            nums.pop(i)
    return nums
if __name__ == "__main__":
    nums = [67,1,6,8,1,2,1,3,2,5,6,3]
    print(remove_duplicates(nums))