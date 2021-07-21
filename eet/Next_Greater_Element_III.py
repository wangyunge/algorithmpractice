"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        for i in range(len(n)-2, -1, -1):
            if n[i+1] > n[i]:
               for j in range(len(n)-1, i, -1): 
                if n[i] < n[j]:
                    n[j], n[i] = n[i], n[j]
                    for k in range(1, (len(n)-1-i)//2+1):
                        n[i+k], n[len(n)-k] = n[len(n)-k], n[i+k]
                    res = int(''.join(n))
                    if res < 2**31-1:
                        return res
        return -1

def main():
    sol = Solution()
    res = sol.nextGreaterElement(12)
    print(res)
   
if __name__ == '__main__':
     main() 
"""
Here is one simple example.
index: 012345
given: 124651
ans : 125146
procedure:
Starting from the rightmost digit, going to left. Find the first digit which is smaller than the previous digit.
In this example, 4 is smaller than 6. Remember 4 and its index 2.
Going from rightmost again. This time, find the first digit which is bigger than 4. It is 5 here.
Swap 4 and 5. The number becomes 125641.
Reverse all the digits which are right to 4's original index (That is 2), 641 should be reversed to 146 here.
And the answer is reached which is 125146.
"""