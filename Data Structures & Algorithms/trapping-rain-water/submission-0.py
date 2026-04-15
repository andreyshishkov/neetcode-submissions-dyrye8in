class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        result = 0
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                result += right_max - height[right]
        return result
        