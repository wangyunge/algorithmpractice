class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)
        right = min(C, G)

        top = min(D, H)
        bottom = max(B, F)

        L = max(0, right-left)
        H = max(0, top-bottom)
        first = (C-A) * (D-B)
        second = (G-E) * (H-F)
        return first + second - L * H
