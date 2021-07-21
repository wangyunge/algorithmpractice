class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        inorder = sorted(postorder)
        in_table = {}
        self.res = True
        for i, num in enumerate(inorder):
            in_table[num] = i
        def _check_node(left, right):
            if postorder:
                pos = in_table[postorder[-1]]
                if left <= pos and pos <= right:
                    postorder.pop()
                    _check_node(pos+1, right)
                    _check_node(left, pos-1)
        _check_node(0, len(inorder)-1)
        return len(postorder) == 0


