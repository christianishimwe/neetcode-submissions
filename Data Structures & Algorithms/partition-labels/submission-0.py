class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        - have a list of size 26,
        - keep track of the last max position
        - keep track of the start of this substring
        - when you see a letter, update max end to be max(max_end, last[letter])
        - if i == max_end, this substring is complete, update start and start over

        """
        last_idx = [-1 for _ in range(26)]
        start = 0
        output = []
        max_pos = float('-inf')
        for i, c in enumerate(s):
            # get this leeters position
            pos = ord(c) - ord('a')
            last_idx[pos] = i
        for i, c in enumerate(s):
            pos = ord(c) - ord('a')
            # case 2, we update max pos
            next_pos_c = last_idx[pos]
            max_pos = max(max_pos, next_pos_c)
            # case 1, we hit the max_pos
            if i == max_pos:
                output.append(i - start + 1)
                start = i + 1
                max_pos = float('-inf')

        return output

            




        