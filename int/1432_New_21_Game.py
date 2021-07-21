'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points. During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points. What is the probability that she has N or less points?

Example
Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  
Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  
Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Notice
0 \leq K \leq N \leq 100000≤K≤N≤10000
1 \leq W \leq 100001≤W≤10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
'''
class Solution:
    """
    @param N: int
    @param K: int
    @param W: int
    @return: the probability
    """
    def new21Game(self, N, K, W):
        DP = [0] * (N+1)
        DP[0] = 1.0
        mid_sum = 0
        for r in range(1, N+1):
            if r < W:                
                mid_sum += DP[r-1] / W
            if r >= W  and r < K:
                mid_sum = mid_sum - DP[r-W]/W + DP[r-1]/W
            if r >= K and r > W:
                mid_sum -= DP[r-1] / W 
            DP[r] = mid_sum 
 
        return sum(DP[K:])

    def new21Game(self, N, K, W):
        DP = [0] * (N+1)
        DP[0] = 1.0
        for r in range(1, N+1):
            for l in range(max(0, r - W), min(K, r)):
                if l < K :
                    DP[r] += DP[l] / W 
        return sum(dp[K, N+2])

    '''
    Note: Dynamic Program solution, the summation within the window is unnecessary. 
    Optimize it by droping the head and add the tail .
    '''
