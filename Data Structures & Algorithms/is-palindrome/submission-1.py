class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - set i = 0, j = l - 1
        - if c at i or j is not alpha, skip them first,
        - otherwise compare
        """
        i = 0
        l = len(s)
        j = l - 1
        while i <= j:
            c_at_i = s[i]
            c_at_j = s[j]
            i_is_number = c_at_i >= "0" and c_at_i <= "9"
            j_is_number = c_at_j >= "0" and c_at_j <= "9"
            if not c_at_i.isalpha() and not i_is_number:
                i += 1
                continue
            if not c_at_j.isalpha() and not j_is_number:
                j -= 1
                continue
            # now we can full compare
            if c_at_i.lower() != c_at_j.lower():
                return False
            i += 1
            j -= 1
        return True