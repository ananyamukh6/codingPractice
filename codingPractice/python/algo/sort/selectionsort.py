def selectionsort(nums):
    for sortidx in range(len(nums)):
        start = sortidx
        for unsortidx in range(start+1, len(nums)):
            if nums[unsortidx]<nums[start]:
                start = unsortidx
        nums[start], nums[sortidx] = nums[sortidx], nums[start]

    return nums



l = [74, 32, 89, 21, 55, 64]
print (selectionsort(l))
