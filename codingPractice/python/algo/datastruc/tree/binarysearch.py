import pdb

'''
class binarySearch:
    def __init__(self, nums, elem):
        self.nums = nums
        self.elem = elem
    
    def search(self, nums, elem):
        if len(nums)>0:
            
            if elem == nums[len(nums)/2]:
                #print (len(nums)/2)
                #print (nums[len(nums)/2])
                return len(nums)/2
            else:
                
                if elem < nums[len(nums)/2]:
                    #pdb.set_trace()
                    return self.search(nums[:len(nums)/2],elem)
                else:
                    return 1+(len(nums)/2) + self.search(nums[(len(nums)/2)+1:], elem)
        else:
            return "The list is empty"

obj = binarySearch([5,10,15,20,25,30,35,40,45,50,55,60,65], 5)
for i in obj.nums:
    idx = obj.search(obj.nums, i)
#idx = obj.search(obj.nums, 15)
    print (idx,i)
'''







import pdb
class binarySearch:
    def __init__(self, nums):
        #assert it is sorted
        self.nums = nums

    def add_to_list(self, new_elem):
        pass

    def del_elem_from_list(self, elem):
        pass

    def del_using_idx_from_list(self, idx):
        pass

    def print_list(self):
        print self.nums:

    def search(self, elem):
        nums = self.nums
        if len(nums)>0:
            
            if elem == nums[len(nums)/2]:
                #print (len(nums)/2)
                #print (nums[len(nums)/2])
                return len(nums)/2
            else:
                
                if elem < nums[len(nums)/2]:
                    #pdb.set_trace()
                    return self.search(nums[:len(nums)/2],elem)
                else:
                    return 1+(len(nums)/2) + self.search(nums[(len(nums)/2)+1:], elem)
        else:
            return "The list is empty"

obj = binarySearch([5,10,15,20,25,30,35,40,45,50,55,60,65])
for i in obj.nums:
    idx = obj.search(i)
#idx = obj.search(obj.nums, 15)
    print (idx,i)

