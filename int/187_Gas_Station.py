'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

 Notice

The solution is guaranteed to be unique.

Have you met this question in a real interview? Yes
Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0
        for i in xrange(len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        if total >= 0:
            return start
        else:
            return -1