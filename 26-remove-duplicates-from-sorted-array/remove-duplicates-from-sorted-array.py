class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=set(nums)
        nums1=list(num)
        nums1.sort()
        k=len(nums1)
        for i in range(k):
            nums[i]=nums1[i]
        return k