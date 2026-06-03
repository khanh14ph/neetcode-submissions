class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1 for i in nums]
        suff= [1 for i in nums]
        res=[1 for i in nums]
        for idx, i in enumerate(nums):
            if idx>0:
                pref[idx]=pref[idx-1]*nums[idx-1]
        for i in range(len(nums),-1,-1):
            if i < len(nums)-1:
                suff[i]=suff[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=pref[i]*suff[i]
        return res