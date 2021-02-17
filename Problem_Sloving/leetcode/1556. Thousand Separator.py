class Solution(object):
    def thousandSeparator(self, n):
        return format(n, ",").replace(",",".")
#        return f"{n:,}".replace(",",".")

Solution().thousandSeparator(123456789)