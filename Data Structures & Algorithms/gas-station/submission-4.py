class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        PLAN
         -ve sum, you start again
        - if you kept going and came back to the starting point (i), then return i
        - start from index 0
        - calculate the current gas remaining, if it is -ve, reset to the next available index
        and the gas as 0
        - if you happen to come back to the previous index, we won
        diff = [-1, 0, -1, 3]
        diff = [-1, -1, 1]
        diff = [1, 3, -5, 3, 3, -6]
        gas=[1,2,3]
        cost=[2,3,2]
        diff = [-1, -1, 1]
        """
        #gas = [1,2,3]
        #cost = [2,3,2]
        diff = [gas - cost for gas, cost in zip(gas, cost)]
        stable_i = -1
        i = -1
        gas_rem = -1
        n = len(gas)
        travels = 0

        while travels <= (2 * n):
            # we are making this travel from here
            i = (i + 1) % n
            # if we just came back to i
            if i == stable_i and gas_rem >= 0:
                break
            travels += 1
            # check if we still got some gas in the tank
            if gas_rem < 0:
                stable_i = i
                gas_rem = 0
            gas_rem += diff[i]  
        if travels > (n * 2) or gas_rem < 0:
            return -1
        return stable_i






