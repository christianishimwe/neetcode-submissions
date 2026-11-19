class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. initialize all_chars[26] to store the counts of the chars you have seen
        2. start with i = 0, j = 0, max_f = 0, result = 0
        3. expand j, calculate new max_f, 
        3.1 if the current window size - max_f > k, shrink window by increasing i
        3.2 update result
        "A AAB B" size = 2, max = 3, k = 0
        - this is fine until A ceases to be the max and another letter takes over
        - AAABBB
        """
        all_chars = [0] * 26
        i = 0
        j = 0
        max_f = 0
        l = len(s)
        res = 0
        while j < l:
            # check this current letter
            c_letter = s[j]
            c_idx = ord(c_letter) - ord('A')
            all_chars[c_idx] += 1
            max_f = max(all_chars[c_idx], max_f)
            while (j - i + 1) - max_f > k and i <= j:
                # shrink the left
                # remove the letter at i
                let_idx = ord(s[i]) - ord('A')
                all_chars[let_idx] -= 1
                i += 1
            res = max(res, j - i + 1)

            j += 1
        return res