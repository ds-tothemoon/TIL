class Solution(object):
    def simplifyPath(self, path):
        res = []
        pass_value = ['.', '']
        slash = '/'
        for e in path.split('/'):
            if e == '..':
                if len(res) > 0:
                    res.pop()
            elif e in pass_value:
                pass
            else:
                res.append(e)
        return slash + slash.join(res)

Solution().simplifyPath("/a/./b/../../c/")