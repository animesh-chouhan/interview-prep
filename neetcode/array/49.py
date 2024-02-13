from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            c = tuple(sorted(Counter(s).items()))
            hashmap[c].append(s)
        return list(hashmap.values())


s = Solution()
print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams(strs=[""]))
print(s.groupAnagrams(strs=["a"]))
