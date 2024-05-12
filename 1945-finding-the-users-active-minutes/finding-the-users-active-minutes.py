class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        d = {}
        for log in logs:
            id, min = log
            if id not in d:
                d[id] = set()
            d[id].add(min)

        for value in d.values():
            l = len(value)
            if l > 0:
                ans[l-1] += 1
        
        return ans