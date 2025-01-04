class Solution:
    def reverse(self, x: int) -> int:
        reverseNum = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 
        n = abs(x)
        isNegative = False
        if(x < 0):
            isNegative = True
        while(n > 0):
            last = n % 10
            reverseNum = (reverseNum * 10) + last
            n = n // 10

        if (reverseNum > INT_MAX or reverseNum < INT_MIN):
            return 0
            
        if(isNegative == True):
            return -reverseNum

        
        return reverseNum