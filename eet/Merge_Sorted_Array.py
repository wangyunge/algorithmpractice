'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Subscribe to see which companies asked this question
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        a=0
        b=0
        while i < m+n:
            if a >=m:
                nums1.append(nums2[b])
                b+=1
            elif b >=n:
                a+=1
            elif nums1[i]>nums2[b]:
                nums1.insert(i,nums2[b])
                b+=1
            else:
                a+=1
            i+=1
        return nums1
def main():
    sol = Solution()
    nums1 = [1,2,4,5,7]
    nums2 = [3,6,8,9]
    res = sol.merge(nums1,5,nums2,4)
    print res
if __name__ == '__main__':
    main()




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = n-1
        b = m-1
        nums1.extend(nums2)
        idx = m+n-1
        while a >=  0 and b >= n:
            if nums1[a] > nums2[b]:
                nums1[idx] = nums1[a]
                a -= 1
            else:
                nums1[idx] = nums2[b]
                b -= 1
            idx -= 1
        if a < 0:
            while b >= 0:
                nums1[idx] = nums2[b]
                b -= 1
                idx -= 1


