class Solution:
    def customSortString(self, order: str, s: str) -> str:
        st=''
        for char in order:
            while True:
                if char in s:
                    st+=char
                    ind=s.index(char)
                    s=s[:ind]+s[ind+1:]
                else:
                    break
        if s:
            st+=s
        return st