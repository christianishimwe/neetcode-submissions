class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        - use a map to map each number you have seen to idx
        - map: num -> index
        - now iterate through all the elements, num
        - check if target - num in the dictionary, if yes return the indices

        """
        dict_numbers = {}
        for i, num in enumerate(numbers):
            if target - num in dict_numbers:
                return [dict_numbers[target - num] + 1, i + 1]
            dict_numbers[num] = i
        return []



        