def starArrange(s):
    lst = []
    endrange = (s/2)+1 if s%2 ==0 else ((s+1)//2)+1
    for i in range(2,endrange):
        #print i
        if s%(2*i-1) == i or s%(2*i -1) == 0:
            lst += [(i, i-1)]
        if s%i == 0:
            lst += [(i,i)]
    print lst

starArrange(32767)

