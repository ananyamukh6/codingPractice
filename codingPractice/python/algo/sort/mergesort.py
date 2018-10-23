class mergeSort:
    def __init__(self, nums):
        self.nums = nums

    def merge(self,lst1, lst2):
        if lst1 == []:
            return lst2
        if lst2 == []:
            return lst1
        if lst1[0]<lst2[0]:
            return ([lst1[0]]+self.merge(lst1[1:],lst2))
        else:
            return ([lst2[0]]+self.merge(lst1, lst2[1:]))

    def msort(self, nums):
        if len(nums) <=1:
            return nums
        mid = len(nums)/2
        return self.merge(self.msort(nums[:mid]), self.msort(nums[mid:]))

    

obj = mergeSort([5,2,6,3,1,4,7])
print (obj.msort(obj.nums))