class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in s:
            if i == "A":
                absent += 1
                if absent == 2:
                    return False
            if i == "L":
                late += 1
                if late > 2:
                    return False
            else:
                late = 0
        return True