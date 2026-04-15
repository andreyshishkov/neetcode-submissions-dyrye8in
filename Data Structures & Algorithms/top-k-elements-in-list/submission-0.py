import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [x[0] for x in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]