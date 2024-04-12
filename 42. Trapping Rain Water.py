class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        result = 0
        i = 0
        j = len(height) - 1
        imax = height[i]
        jmax = height[j]

        while i < j:
            if imax < jmax:
                result += imax - height[i]
                i += 1
                imax = max(imax, height[i])
            else:
                result += jmax - height[j]
                j -= 1
                jmax = max(jmax, height[j])
        return result