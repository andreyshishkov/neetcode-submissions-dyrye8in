class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_amount = 0
        while left < right:
            cur_amount = min(heights[left], heights[right]) * (right - left)
            max_amount = max(cur_amount, max_amount)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_amount