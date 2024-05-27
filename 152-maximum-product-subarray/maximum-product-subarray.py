class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        n = len(nums)
        ans = 0
        if n == 1 and nums[0] < 0:
            return nums[0]
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf =1
            pre = pre * nums[i]
            suf = suf * nums[n-i-1]
            ans = max(ans,max(pre,suf))
        return ans