class Solution:
    def minSubarray(self, nums, p):
        n, target = len(nums), sum(nums)%p

        if target == 0:
            return 0 

        dict1, running_sum, min_len = {}, 0, n

        for right in range(n):
            running_sum += nums[right]

            if (running_sum-target)%p == 0:
                min_len = min(min_len,right+1)

            if (running_sum-target)%p in dict1:
                min_len = min(min_len,right-dict1[(running_sum-target)%p])

            dict1[running_sum%p] = right

        return min_len if min_len != n else -1