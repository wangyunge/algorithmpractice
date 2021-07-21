"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

  def get_sequence_output(self):
    """
    Returns:
      float32 Tensor in shape [len, bsz, d_model]. The last layer hidden
      representation of XLNet.
    """

    return self.output

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [i for i in range(n+1)]
        for i in range(1, n+1):
            tmp = float('inf')
            sq = 1
            root = 1
            while sq <= i:
                steps = DP[i-sq] + 1
                tmp = min(tmp, steps)
                root += 1
                sq = root*root
            DP[i] = tmp

        return DP[n]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = float('inf')
        def _dfs(sum_res, steps):
            root = 1
            sq = root*root
            while sq < sum_res:
                _def(sum_res - sq, steps+1)
                root += 1
                sq = root*root
            if sq == sum_res:
                res = min(res, steps+1)
        _dfs(n, 0)
        return res



  def get_new_memory(self):
    """
    Returns:
      list of float32 Tensors in shape [mem_len, bsz, d_model], the new
      memory that concatenates the previous memory with the current input
      representations.
      The length of the list equals n_layer.
    """
    return self.new_mems

  def get_embedding_table(self):
    """
    Returns:
      float32 Tensor in shape [n_token, d_model]. The embedding lookup table.
      Used for tying embeddings between input and output layers.
    """
    return self.lookup_table
















