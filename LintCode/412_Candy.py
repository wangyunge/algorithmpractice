'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.

Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Have you met this question in a real interview? Yes
Example
Given ratings = [1, 2], return 3.

Given ratings = [1, 1, 1], return 3.

Given ratings = [1, 2, 2], return 4. ([1,2,1]).
'''
class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
    def candy(self, ratings):
        helper1 = [1] * len(ratings)
        helper2 = [1] * len(ratings)
        res = 0
        for i in xrange(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                helper1[i] = helper1[i-1]+1
            else:
                helper1[i] = 1
        for i in range(len(ratings)-1)[::-1]:
            if ratings[i] > ratings[i+1]:
                helper2[i] = helper2[i+1]+1
            else:
                helper2[i] = 1
        for i in xrange(len(ratings)):
            res += max(helper2[i],helper1[i])
        return res    