class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - you could first sort
        - you could use a hashmap of values (O(N))


        - create an empty hashmap
        - num -> index
        - go through num again, and get the num remaining to get the target
        - if you find it, return both indices

        """
        indices = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            rem = target - num
            if  rem in indices:
                j = indices[rem]
                if j != i:
                    return [i, j]
        return []
        
        
        