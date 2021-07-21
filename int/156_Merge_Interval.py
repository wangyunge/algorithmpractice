'''
Given a collection of intervals, merge all overlapping intervals.

Have you met this question in a real interview? Yes
Example
Given intervals => merged intervals:

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
    	res = []
    	for newInter in intervals:
    		tmp = []
    		while res:
    			setted = res.pop()
    			if self.overLap(setted,newInter):
    				newInter.start = min(setted.start,newInter.start)
    				newInter.end = max(setted.end,newInter.end)
    			else:
    				tmp.append(setted)
    		tmp.append(newInter)
    		res = tmp
    	return sorted(res,key = lambda interval:interval.start)
    def overLap(self,first,second):
    	i=0
    	while i < 2:
    		i+=1
    		if i == 2:
    			first,second = second,first
    		if first.start <= second.start <= first.end or first.start <= second.end <= first.end:
    			return True
    		if first.start <= second.start and first.end >= second.end:
    			return True
    	return False
def main():
	test = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
	sol = Solution()
	sol.merge(test)
if __name__ == '__main__':
	main()