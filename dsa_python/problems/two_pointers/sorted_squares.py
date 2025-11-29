def sorted_sqaures(nums):
    result=[]
    start = 0
    end = len(nums)-1
    while start <= end:
        if abs(nums[start]) > abs(nums[end]):
            result.append(nums[start]**2)
            start+=1
        else:
            result.append(nums[end] ** 2)
            end-=1
    return result[::-1]

if __name__ == "__main__":
    nums=[-4,1,3,5]
    print(sorted_sqaures(nums))