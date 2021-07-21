"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

"""

from collections import deque
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        prev = deque()
        cur = deque()
        prev.append(0)
        row_num = 1

        while row_num < N:
            row_num += 1

            while prev:
                symbol = prev.popleft() 
                if symbol == 1:
                    cur.append(1)
                    cur.append(0)
                if symbol == 0:
                    cur.append(0)
                    cur.append(1)
            prev, cur = cur, prev
        return prev[K-1]


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def _dfs(row_num, idx):
            if row_num == 1:
                return 0

            parent = _dfs(row_num-1, (idx+1)//2)
            if (parent == 0 and idx % 2 == 1) or (parent == 1 and idx % 2 == 0):
                return 0
            if (parent == 1 and idx % 2 == 1) or (parent == 0 and idx % 2 == 0):
                return 1
        return _dfs(N, K)