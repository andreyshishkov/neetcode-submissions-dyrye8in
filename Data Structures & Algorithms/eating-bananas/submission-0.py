import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = 0
        while left <= right:
            cur_speed = (left + right) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / cur_speed)
            if total_time <= h:
                right = cur_speed - 1
                result = cur_speed
            elif total_time > h:
                left = cur_speed + 1
        return result