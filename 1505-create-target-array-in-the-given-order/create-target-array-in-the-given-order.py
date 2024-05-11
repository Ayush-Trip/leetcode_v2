class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for i in range(len(index)):
            a=index[i]
            ans.insert(a,nums[i])
        return ans