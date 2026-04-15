class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return s

        first, last = 0, len(s) - 1
        while first < last:
            if not s[first].isalnum():
                first += 1
                continue

            if not s[last].isalnum():
                last -= 1
                continue

            if s[first].lower() != s[last].lower():
                return False
            
            last -= 1
            first += 1

        return True