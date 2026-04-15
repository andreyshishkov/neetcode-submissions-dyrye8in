class Solution:
    def get_kth(self, a_arr: List[int], m: int, b_arr: List[int], 
    n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return self.get_kth(b_arr, n, a_arr, m, k, b_start, a_start)
        if m == 0:
            return b_arr[b_start + k - 1]
        if k == 1:
            return min(a_arr[a_start], b_arr[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a_arr[a_start + i - 1] > b_arr[b_start + j - 1]:
            return self.get_kth(a_arr, m, b_arr, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a_arr, m - i, b_arr, n, k - i, a_start + i, b_start)
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        
        left_median_value = self.get_kth(nums1, len(nums1), nums2, len(nums2), left)
        right_median_value = self.get_kth(nums1, len(nums1), nums2, len(nums2), right)
        return (left_median_value + right_median_value) / 2.0
        