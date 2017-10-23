# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numDict = {}
    # for i in range(len(nums)):
    #     numDict[nums[i]] = i
    #
    # for i in range(len(nums)):
    #     diff = target - nums[i]
    #     if diff in numDict:
    #         return [i , numDict[diff]]
    #         # return [numDict[diff], i]

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in numDict:
            return [numDict[diff], i]
        else:
            numDict[nums[i]] = i

print twoSum([2, 7, 11, 15], 9)
