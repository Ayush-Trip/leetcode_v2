class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        dup = x
        while(x>0):
            last = x % 10
            num = (num * 10) + last
            x = x // 10

        if (num == dup):
            return True
        else:
            return False