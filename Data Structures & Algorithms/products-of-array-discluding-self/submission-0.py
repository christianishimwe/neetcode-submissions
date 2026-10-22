class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prods = [0 for _ in range(n)]
        suffix_prods = [0 for _ in range(n)]
        prefix_prods[0] = nums[0]
        suffix_prods[-1] = nums[-1]
        output = [0 for _ in range(n)]
        for i in range(1, n):
            prefix_prods[i] = prefix_prods[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffix_prods[i] = suffix_prods[i + 1] * nums[i]
        for i, num in enumerate(nums):
            prod = 1
            if i + 1 < n:
                prod *= suffix_prods[i + 1]
            if i - 1 >= 0:
                prod *= prefix_prods[i - 1]
            output[i] = prod
        return output
            

        