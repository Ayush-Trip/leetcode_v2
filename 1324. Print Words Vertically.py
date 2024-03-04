class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(' ')
        n = float('-inf')
        for i in range(len(s)):
            n = max(n, len(s[i]))
        ans=[""]*n
        for i in range (n):
            c=[]
            for j in range (len(s)):
                if len(s[j])<=i:
                    c.append(' ')
                else:
                    c.append(s[j][i])
            ans[i]=''.join(c)
        ans = [''.join(c1.rstrip()) for c1 in ans]
        return ans

        