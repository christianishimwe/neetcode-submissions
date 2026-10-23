class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_to_index = {num: i for i, num in enumerate(nums)}
        l = len(nums)
        before = [-1 for _ in range(l)]
        after = [-1 for _ in range(l)]
        max_count = 0
        for i, num in enumerate(nums):
            prev_num = num - 1
            next_num = num + 1
            if prev_num in num_to_index:
                prev_idx = num_to_index[prev_num]
                before[i] = prev_idx
                after[prev_idx] = i
            if next_num in num_to_index:
                next_idx = num_to_index[next_num]
                before[next_idx] = i
                after[i] = next_idx
        for i in range(l):
            if before[i] == -1:
                # follow the chain
                this_count = 0
                j = i
                while j != -1:
                    this_count += 1
                    j = after[j]
                max_count = max(max_count, this_count)
        return max_count
                
                    