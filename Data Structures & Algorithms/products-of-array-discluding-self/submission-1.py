class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        prefix = [1] * L
        for i in range(1, L):
            prod = prefix[i - 1] * nums[i - 1]
            prefix[i] = prod

        suffix = [1] * L
        for i in range(L - 2, -1, -1):
            prod = suffix[i + 1] * nums[i + 1]
            suffix[i] = prod

        result = []
        for i in range(L):
            result.append(prefix[i] * suffix[i])
        return result
