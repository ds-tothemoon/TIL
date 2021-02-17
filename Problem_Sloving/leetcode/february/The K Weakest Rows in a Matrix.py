class Solution(object):
    def kWeakestRows(self, mat, k):
        from functools import reduce
        res = reduce(lambda res, cur: res + [(sum(cur),len(res))], mat, [])
        res = sorted(res, key=lambda item: (item[0],item[1]))[:k]
        res = list(map(lambda x: x[1], res))
        return res
