'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        distance = len(gas)-1
        for start in xrange(0,len(gas)):
            tank = 0
            for steps in xrange(0,len(gas)):
                index = start + steps if start+steps <= distance else distance-(start+steps)-1
                tank  = tank + gas[index] - cost[index]
                if tank < 0 :
                    break
                if steps == len(gas)-1:
                    return start
        return -1
    def canCompleteCircuit(self, gas, cost):
        start,tank,total = 0,0,0
        for i in xrange(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank <0 :
                start = i+1
                total += tank
                tank = 0
        res = -1 if total+tank < 0 else start
        return res
def main():
    sol = Solution()
    res = sol.canCompleteCircuit([1,2],[2,1])
if __name__ == '__main__':
    main()