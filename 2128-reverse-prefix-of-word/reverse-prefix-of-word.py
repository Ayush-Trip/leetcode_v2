class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a= []
        ans = ""
        for i in range (len(word)):
            if word[i] == ch:
                a.append(i)
        t = min(a)
        ans += word[:t+1]
        ans=ans[::-1]
        ans += word[t+1:]
        return ans