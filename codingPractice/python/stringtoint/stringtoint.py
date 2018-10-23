
import re
import pdb
class Solution(object):
    def myAtoi(self, str):
        print (str, type(str))
        if not str :
            return 0
        str = str.strip()
        print (str.strip())
        print (str, type(str))
        out = re.search(r"[+-]?\d+",str)
        print (out, type(out))
        if out:
            s = out.start()
            e = out.end()
            print (s, type(s))
            print (e, type(e))
            if re.search(r"[\D]+",str[:s]):
                return 0
            i = int(str[s:e])
            if i > 2**31 - 1:
                return 2**31 - 1
            if i < -2**31:
                return -2**31
            
            return i
        return 0

obj = Solution()
obj.myAtoi("3125 and words")