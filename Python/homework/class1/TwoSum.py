# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    n = len(nums)
    for i in range(0,n-1,1):
        for j in range((i+1),n,1):
            # print i,j
            s = nums[i] + nums[j]
            # print nums[i],nums[j], s
            if s == target:
                return [i, j]




    # """
    # :type nums: List[int]
    # :type target: int
    # :rtype: List[int]
    # """
    # return [0, 1]

# print twoSum([2, 7, 11, 15], 9)
print twoSum([2, 7, 11, 15], 22)
