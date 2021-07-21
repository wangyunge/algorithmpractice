"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:

Input: [1, 2, 1, 2]
Output: False
Note:

The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 3 ops
        res = False
        # op 1
        def _str_divid(nor, dor):

        def _str_plus(a, b):

        def _str_mins(a ,b):

        def _str_mul(a, b):


        cand = map(nums, lambda x: str(x))
        def _dfs(candi):
            if len(candi) == 1 and candi[0] == 24:
                res = True
            # + or *
            for i in range(len(candi)):
                for j in range(i+1, len(candi)):
                    add = _str_plus(candi[i], candi[j])
                    mul = _str_mul(candi[i], candi[j])
                    nc = candi[:i] +candi[i+1:j] + candi[j+1:] +[add]
                    _dfs(nc)
                    nc = candi[:i] +candi[i+1:j] + candi[j+1:] +[mul]
                    _dfs(nc)
            for i in range(len(candi)):
                for j in range(len(candi)):



