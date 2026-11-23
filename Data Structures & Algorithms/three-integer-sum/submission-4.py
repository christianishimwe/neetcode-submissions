class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - map: (num -> idx)
        - set (all_tuples)
        - start k = last point, 
        - for all i
            for j bigger than i
                start k from where we left of
        [-4, -3, -2, -1, 0, 1, 1, 2, 3, 5, 6, 7]
        """
        nums_with_idx = [(num, i) for i, num in enumerate(nums)]
        nums_with_idx.sort()
        print(nums_with_idx)
        seen = set()
        all_tuples = set()
        n = len(nums)
        k = n - 1
        for i in range(n):
            num_1, _ = nums_with_idx[i]
            for j in range(i + 1, n):
                num_2, _ = nums_with_idx[j]
                sum_1_2 = num_1 + num_2
                target = 0 - sum_1_2
                # check if we have seen it before
                if target in seen:
                    tup = (num_1, num_2, target)
                    tup = sorted(tup)
                    all_tuples.add(tuple(tup))
                else:
                    while k > j:
                        num_3, _ = nums_with_idx[k]
                        if target == num_3:
                            tup = (num_1, num_2, num_3)
                            tup = sorted(tup)
                            all_tuples.add(tuple(tup))
                        elif num_3 < target:
                            break
                        # add ti to mark it seen
                        seen.add(num_3)
                        k -= 1
        return [list(tup) for tup in all_tuples]




        

        