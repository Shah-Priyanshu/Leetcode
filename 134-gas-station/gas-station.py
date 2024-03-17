class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1  # If total gas is less than total cost, the trip is impossible
        
        total, current, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            current += gas[i] - cost[i]
            if current < 0:
                # Can't reach the next station from here, try the next station as the starting point
                start = i + 1
                current = 0
        return start if total >= 0 else -1
