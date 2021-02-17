class Solution(object):
    def myAtoi(self, s):
        res = 0
        numbers = '0123456789'
        MAX_VALUE = (2**31)-1      
        MIN_VALUE = -(2**31)

        try:
            tmp = ''
            for i in s.strip().split()[0]:
                if tmp == '' and i in '+-':
                    tmp = i
                else:
                    if i in numbers:
                        tmp += i
                    else:
                        break
            res = int(tmp)
        except:
            pass
        
        if res >= MAX_VALUE:
            return MAX_VALUE
        elif res <= MIN_VALUE:
            return MIN_VALUE
        else:
            return res


Solution().myAtoi("        3       ")