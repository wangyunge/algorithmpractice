'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        deepest = 1
        candies = [1 for i in xrange(len(ratings))]
        for i in xrange(len(ratings)):
            if i+1 < len(ratings):
                candies[i+1] = candies[i] + 1 if ratings[i+1] > ratings[i] else candies[i+1]
        for i in xrange(len(ratings)-1,-1,-1):
            if i-1 > -1:
                candies[i-1] = candies[i] +1 if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i] else candies[i-1]

        return sum(candies)
def main():
    sol = Solution()
    res = sol.candy([4,2,3,4,1])
if __name__ == '__main__':
    main()