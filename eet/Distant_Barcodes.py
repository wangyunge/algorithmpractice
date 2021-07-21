"""
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.



Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
"""

# DFS
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        # count
        table = {}
        for bar in barcodes:
            cnt = table.get(bar, 0)
            table[bar] = cnt + 1
        def _dfs(path, left):
            if len(path) == len(barcodes):
                return path
            for key, cnt in left.items():
                if cnt > 0 and key != path[-1]:
                    new_table = left
                    new_table[key] -= 1
                    _dfs(path+[key], new_table)
            res = _dfs(['0'], table)
            return res[1:]

# Priority Queue
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
# Task Completion
#Fill the most frequency first with every (len(s) / most_freq)-1 positions


