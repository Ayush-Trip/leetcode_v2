class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        count = 0
        s = s.replace("-", "")
        for i in reversed(range(len(s))):
            result.append(s[i].upper())
            count += 1
            if count == k and i != 0:
                result.append("-")
                count = 0
        return ''.join(result[::-1])