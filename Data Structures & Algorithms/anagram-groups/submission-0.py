class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - you could store a sorted key
        - "sorted string" -> [all anagrams]
        - initialize a dict 
        - when you see string, sort it, then check if you have see it before
        - at the ned, return all values
        """
        anagrams = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            #anagrams[sorted_word] = anagrams.get(sorted_word, []).append(word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())
        