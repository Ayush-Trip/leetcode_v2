class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        arr = set(nums)
        for i in range(1,len(nums)):
            if i not in arr:
                ans.append(i)
        if(len(nums) not in arr):
            ans.append(len(nums))
        return ans