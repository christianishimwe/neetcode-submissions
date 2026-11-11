class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
       - initialize a stack
       - put the first number (num, idx)
       - check the next number, if this next number if greater than what's on the stack (keep doing so); then pop the last number and update result, then append the last num
       - if this is equal, append it just
       - if this is smaller, just append it as well
       try
       - (30, i) j == 1, j - i, put [(38, 1), (36, 3), (35, 4), ()
       - (30)

        """
        our_stack = [(temperatures[0], 0)]
        l = len(temperatures)
        output = [0 for _ in range(l)]
        for k in range(1, l):
            curr = temperatures[k]
            # once you have the curr, 
            while our_stack:
                prev, i = our_stack[-1]
                if curr <= prev:
                    # here just leave it, and keep going
                    break
                # otherwise
                output[i] = k - i
                # pop it as well
                our_stack.pop()
            # whenever you are done, put this k as well
            our_stack.append((curr, k))
        return output


