class Solution:
    def pivotInteger(self, n: int) -> int:
        max_sum = n * (n + 1) / 2
        for i in range(1,n+1):
            current_sum = i * (i + 1) / 2
            remain_sum = max_sum - current_sum + i
            if remain_sum == current_sum:
                return i 
        return -1