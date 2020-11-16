class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        if n % 3 == 0 and n % 5 -> "FizzBuzz"
        if n % 3 == 0 -> "Fizz"
        if n % 5 == 0 -> "Buzz"
        else -> n
        """
        ret = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0: ret.append("FizzBuzz")
            elif i % 3 == 0: ret.append("Fizz")
            elif i % 5 == 0: ret.append("Buzz")
            else: ret.append(str(i))
        
        return ret
            
        