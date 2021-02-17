class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.','[.]')

Solution().defangIPaddr("255.100.50.0")