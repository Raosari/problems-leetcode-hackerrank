# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it 
# were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
def SearchNum(nums,target):
    lp,rp = 0, len(nums) - 1
    while lp < rp:
        mid = (lp + rp) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lp = mid + 1
        else:
            rp = mid - 1
    return lp

target = 2
nums = [1,3,5,7,9,11]

a = SearchNum(nums,target)
print(a)

