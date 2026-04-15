class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        k = 0
        while k < len(s):
            cur = k
            while s[cur] != '#':
                cur += 1
            len_string = int(s[k:cur])
            string = s[cur + 1: cur + 1 + len_string]
            decoded.append(string)
            k = cur + 1 + len_string
        return decoded
