import pdb
class insertionSort:
    def __init__(self, nums):
        self.nums = nums
    
    def ins_sort(self, nums):
        for i in range(1,len(nums)):
            key = nums[i]
            j = i-1
            while j> -1 and key<nums[j]:
                nums[j+1] = nums[j]
                j = j-1
            nums[j+1] = key
        return nums


obj = insertionSort([5,2,6,3,1,4])

print (obj.ins_sort(obj.nums))

