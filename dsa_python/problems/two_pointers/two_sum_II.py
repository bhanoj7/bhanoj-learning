def two_sum(numbers,target):
    start = 0
    end = len(numbers)-1
    while start < end:
        if numbers[start] + numbers[end] > target:
            end-=1
        elif numbers[start] + numbers[end] < target:
            start+=1
        else:
            return [start+1, end+1]
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(two_sum(numbers,target))