class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in anagrams:
                 anagrams["".join(sorted(strs[i]))].append(strs[i])
            else:
                anagrams["".join(sorted(strs[i]))] = [strs[i]]
        
        
        return list(anagrams.values()) 