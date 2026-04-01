class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = heights[0]
        right = heights[-1]

        left_index = 0
        right_index = len(heights) - 1
        water = 0
        best = 0
        while left_index < right_index:
            water = (right_index - left_index) * min(left, right)
            best = max(best, water)

            if left > right:
                right_index -= 1
            else:
                left_index += 1
            left = heights[left_index]
            right = heights[right_index]

        return best