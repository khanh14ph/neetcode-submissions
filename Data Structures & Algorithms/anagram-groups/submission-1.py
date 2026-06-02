class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for i in strs:
            hashed_key = self.create_dict_key(i)
            # FIX: Properly initialize and append
            if hashed_key not in res:
                res[hashed_key] = []
            res[hashed_key].append(i)
            
        # OPTIMIZATION: Just return the values directly
        return list(res.values())

    def create_dict_key(self, s):
        res=dict()
        for i in s:
            res[i]=res.get(i,0)+1
        sorted_items = sorted(res.items()) 
    
        return tuple(item for kv in sorted_items for item in kv)