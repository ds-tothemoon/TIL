class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = dict()
        res = []
        for ele in strs:
            key = ''.join(sorted(ele))
            if hash_map.get(key) == None:
                hash_map[key] = [ele]
            else:
                hash_map[key].append(ele)
        
        for key in hash_map.keys():
            res.append(hash_map[key])
        
        return res