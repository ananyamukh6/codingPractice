import random, pdb

def median(arr):
    return helper(arr, len(arr)//2)

def genpivotidx(arr):
    pivotidx = 0 #random.randint(0, len(arr)-1)        
    return pivotidx

def pivot(arr, pidx):
    left = []; right = []; eq = 0
    for i in arr:
        if i<arr[pidx]:
            left += [i]
        elif i>arr[pidx]:
            right += [i]
        else:
            eq += 1
    return left, eq, right
def helper(arr, k):
    assert (k < len(arr))
    if k==0 and len(arr) == 1:
        return arr[0]
    else:
        pidx = genpivotidx(arr)
        left, numpvtelems, right = pivot(arr, pidx)
        if len(left) >= k:
            return helper(left, k)
        elif len(left) + numpvtelems >= k:
            return arr[pidx]
        else:
            return helper(right, k-len(left)-numpvtelems)

xx = [2,5,2,5,7,3,6,8,9]
print median(xx)
print sorted(xx)[len(xx)//2]
print (sorted(xx))