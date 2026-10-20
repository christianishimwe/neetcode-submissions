class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - construct a map for s: char -> counts
        - go over each char in t, reduce the count in s,
        - if the count drops to 0, remove it
        - at the end check if the dictionary is empty

        """
        dict_s = {}
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        for c in t:
            if c not in dict_s:
                return False
            dict_s[c] -= 1
            if dict_s[c] == 0:
                del dict_s[c]
        # now check if there are no more stuff remaining
        return not dict_s