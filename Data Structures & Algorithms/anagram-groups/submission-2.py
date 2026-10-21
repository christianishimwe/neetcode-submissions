class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - you could store a sorted key
        - "sorted string" -> [all anagrams]
        - initialize a dict 
        - when you see string, sort it, then check if you have see it before
        - at the ned, return all values
        - O(m * nlogn)
        
        anagrams = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            #anagrams[sorted_word] = anagrams.get(sorted_word, []).append(word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())
        """
        anagrams = dict()
        for word in strs:
            # get its frequency map
            fr_map = [0] * 26
            for c in word:
                fr_map[ord(c) - ord('a')] += 1
            tuple_word = tuple(fr_map)
            if tuple_word in anagrams:
                anagrams[tuple_word].append(word)
            else:
                anagrams[tuple_word] = [word]
        return list(anagrams.values())
        