def move_zeroes(nums):
    slow=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[slow],nums[i]=nums[i],nums[slow]
            slow+=1
    return nums
if __name__ == "__main__":
    nums=[0,1,2,0,3,5]
    print(move_zeroes(nums))