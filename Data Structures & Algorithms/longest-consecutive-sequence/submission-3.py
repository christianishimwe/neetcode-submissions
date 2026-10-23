class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # just have a set
        all_elts = set(nums)
        max_count = 0
        for num in all_elts:
            if num - 1 not in all_elts:
                # this is a start
                count = 0
                while num in all_elts:
                    count += 1
                    num += 1
                max_count = max(max_count, count)
        return max_count
                