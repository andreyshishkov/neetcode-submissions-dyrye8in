class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for num in nums:
            if num in elems:
                return True
            elems.add(num)
        return False