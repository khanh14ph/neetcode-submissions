class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=dict()
        for i in nums:
            freq[i]=freq.get(i,0)+1
        print(freq)
        lst=sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        return lst[0:k] 