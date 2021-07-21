'''
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。


'''

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        def _check(base, amount):
            cur = 1
            while amount > 0:
                if amount - cur  < 0:
                    return False 
                amount -= cur   
                cur *= base
            return amount == 0

        n = int(n)
        # Remove expo
        for res in range(2, n):
            if _check(res, n):
                return str(res)
        return str(n)

'''
First things first. Let's see the math behind it.

From given information, we can say one thing- Numbers will be of form-

n = k^m + k^(m-1) + ... + k + 1
=> n-1 = k^m + k^(m-1) + ... + k
=> n-1 = k (k^(m-1) + k^(m-2) + ... + k + 1) ...... [1]

Also, from n = k^m + k^(m-1) + ... + k + 1, we can say,
n-k^m = k^(m-1) + k^(m-2) + ... + k + 1 ...... [2]

from [1] and [2],

n-1 = k (n - k^m)
=>k^(m+1) = nk - n + 1

if you shuffle sides you will end up getting following form,

(k^(m+1) - 1)/(k - 1) = n .... [3]

Also from [1] note that, (n - 1) must be divisible by k.

We know that, n = k^m + k^(m-1) + ... + k + 1

=> n > k^m
=> m-th root of n > k .... [4]

[EDIT] -->

With inputs from @StefanPochmann we can also say, from binomial thorem, n = k^m + ... + 1 < (k+1)^m .... [5]
Therefore, k+1 > m-th root of n > k. .... from [4] and [5]
Thus ⌊m-th root of n⌋ is the only candidate that needs to be tested. [6]

<--

So our number should satisfy this equation where k will be our base and m will be (number of 1s - 1)

This brings us to the search problem where we need to find k and m.

Linear search from 1 to n does not work. it gives us TLE. So it leaves us with performing some optimization on search space.

From [6] we know that the only candidate that needs to be tested is, ⌊m-th root of n⌋

We also know that the smallest base is 2 so we can find our m must be between 2 and log2n else m is (n-1) [7]

That brings me to the code:
'''

import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n,2)) # Refer [7]
        for m in range(max_m,1,-1):
            k = int(n**m**-1)  # Refer [6]
            if (k**(m+1)-1)//(k-1) == n:
                # Refer [3]
                return str(k)
        
        return str(n-1)  