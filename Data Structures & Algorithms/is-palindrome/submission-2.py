class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, last = 0, len(s) - 1
        while start < last:
            if not s[start].isalpha() and not s[start].isdigit():
                start += 1
                continue
            if not s[last].isalpha() and not s[last].isdigit():
                last -= 1
                continue

            if s[start].lower() == s[last].lower():
                start += 1
                last -= 1
            else:
                return False
        return True 
