class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        PLAN:
        - create dict num -> counts
        - have a list[list], size n + 1, indices are the counts ->
        elements is the list of values that have such a count
        - iterate from the end of the list and build the top k elements
        """
        n = len(nums)
        counts = {}
        freq = [[] for _ in range(n + 1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            freq[count].append(num)
        counts_so_far = k
        result = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                result.append(num)
                counts_so_far -= 1
                if counts_so_far == 0:
                    return result
        return result
        

