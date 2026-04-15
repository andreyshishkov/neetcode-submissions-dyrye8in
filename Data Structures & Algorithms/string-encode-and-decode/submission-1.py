class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            L = len(s)
            encoded += f'{L}_{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        L = len(s)

        strings = []
        while s:
            n, s = s.split('_', 1)
            n = int(n)
            string = s[:n]
            strings.append(string)
            s = s[n:]
        return strings

            
