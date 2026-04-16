from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(counter_t)
        res_len = float('inf')
        res_ends = [-1, -1]
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in counter_t and window[ch] == counter_t[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res_ends = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in counter_t and window[s[left]] < counter_t[s[left]]:
                    have -= 1
                left += 1
        left, right = res_ends
        return s[left:right + 1] if res_len != float('inf') else ''
         
        