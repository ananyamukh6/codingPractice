class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self, nums, target):
        map_num = {}
        for idx in range(0, len(nums)):
            map_num[idx] = nums[idx]
            rem = target - nums[idx]
            print map_num
            if rem in map_num.values():
                if map_num.values().index(rem) == idx:
                    continue           
                return [map_num.values().index(rem),idx]


obj = Solution([11, 7, 18, 4, 8, 15, -1],16)
aa = obj.twoSum(obj.nums, obj.target)
print aa
#print (obj.nums)
#print (obj.target)



