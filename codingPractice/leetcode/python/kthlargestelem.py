max0 = -inf  //largest
max1 = -inf
max2 = -inf  //3rd largest
max
for i in arr:
    if i > max2 && i < max1 && i < max0:
        max2 = i
    elif i > max1 && i < max0:
        max2 = max1
        max1 = i
    elif i > max0:
        tmpmax1 = max1
        max1 = max0
        max2 = tmpmax1
        max0 = i
return max2

max = [-inf] * m .... here
for i in arr:  arr has n elements
    if i > max[-1]: #i is larger than th esmallest element in max array
        idx = binsearch(max, i) #find the location in max where i would fit O(log m)
        swap(max, idx, i) Place i in max .... O(m)
    #else:
    #    do nothing

O(nm) vs O(n lg n)


create O(n)
extract 