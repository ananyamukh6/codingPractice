import pdb
def multiply(num1, num2):
    if len(num1) == 0 or len(num2) == 0 :
        return 0
    else:
        #pdb.set_trace()
        carry = 0
        sums = 0
        prods = []
        for idx_n2 in range(len(num2), 0, -1):
            for idx_n1 in range(len(num1),0, -1):
                #pdb.set_trace()
                prods += [int(num1[idx_n1-1])*int(num2[idx_n2-1])]
        return prods

aa = multiply('14', '3')
print type(aa[0])
                    
                
                    