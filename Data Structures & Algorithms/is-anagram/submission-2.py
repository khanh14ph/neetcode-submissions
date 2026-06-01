class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_s=self.count_freq(s)
        res_t=self.count_freq(t)
        return res_s==res_t
    def count_freq(self, s):
        res=dict()
        for i in s:
            res[i]=res.get(i,0)+1
        return res
        