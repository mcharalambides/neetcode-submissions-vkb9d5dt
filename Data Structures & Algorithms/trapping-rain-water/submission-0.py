class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_left[0] = height[0]
        max_right = [0] * n
        max_right[0] = height[-1]
        water = 0
        for i in range(1, n-1):
            max_left[i] =  max(max_left[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        for i in range(1, n):
            level = min(max_left[i], max_right[i])
            if level > height[i]:
                water += level - height[i]

        return water