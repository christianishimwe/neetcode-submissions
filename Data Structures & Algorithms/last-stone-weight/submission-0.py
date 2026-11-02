import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [2, 3, 6, 2, 4]
        [2, 3, 6, 2, 4]
        use heap
        # create a heap
        # put all the numbers
        # at some point, pop 2 numbers, and crush them together
        # put the remaineder back
        """
        q = [-1 * stone for stone in stones]
        heapq.heapify(q)
        while q:
            # get the two numbers
            first = -1 * heapq.heappop(q)
            print(first)
            if q:
                second = -1 * heapq.heappop(q)
            else:
                return first
            # find their diffrerence
            diff = first - second
            if diff > 0:
                heapq.heappush(q, -1 * diff)
        return 0