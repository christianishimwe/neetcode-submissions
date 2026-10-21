class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        PLAN:
        - [1,2, 3, 2, 3,3]
        - [1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7]
        - keep a heap
        - keep only k elements in the heap
        [1, 2, 2]
        - build a hashmap, val -> counts
        - extract [(counts, val)]
        - extract the k most frequent 
        """
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        elements = [(count, val) for val, count in counts.items()]
        elements.sort(key=lambda x: -1 * x[0])
        output = elements[:k]
        return [elem for _, elem in output]

