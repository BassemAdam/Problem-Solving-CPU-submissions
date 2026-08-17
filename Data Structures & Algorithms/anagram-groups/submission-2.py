class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in anagrams:
                anagrams[key].append(strs[i])
            else:
                anagrams[key] = [strs[i]]
        
        return list(anagrams.values()) 