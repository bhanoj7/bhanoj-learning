from collections import Counter
def intersect(nums1,nums2):
    nums1_freq = Counter(nums1)
    result = []
    for i in nums2:
        if i in nums1 and nums1_freq[i]>0:
            result.append(i)
            nums1_freq[i]-=1
    return result
if __name__ == "__main__":
    nums1=[2,1,2,2]
    nums2=[2,2]
    print(intersect(nums1,nums2))