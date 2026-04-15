from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams =[]
        counters = []
        for word in strs:
            cur_counter = Counter(word)
            for i, counter in enumerate(counters):
                if counter == cur_counter:
                    anagrams[i].append(word)
                    break
            else:
                anagrams.append([word])
                counters.append(cur_counter)
        return anagrams