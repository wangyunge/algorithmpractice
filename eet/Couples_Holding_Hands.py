"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
"""

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        table = [[0,0] for _ in range(len(row)/2)]
        for idx in range(len(row)):
            key = row[idx] // 2
            s_key = row[idx] % 2
            table[key][s_key] = idx

        def _swap():

        def _dfs(idx, table, steps):
            if idx < len(row) -1 :

                if row[idx]//2 == row[idx+1]//2:
                    _dfs(idx + 2, table, steps)
                # if swap to the place where match other couple

                # else dfs the first one , dfs the second one
              
             