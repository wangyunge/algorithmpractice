'''
Find the kth smallest element in an unsorted array. Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not k:
            return -1
        heap = [ -1]  * k
        for e in nums:
            if e > heap[0]:
                self.insert_head(heap, e)
        if heap:
            return heap[0] 
        else:
            return 

    def heapify(self, arr, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[smallest] > arr[left]:
            smallest = left
        if right < len(arr) and arr[smallest] > arr[right]:
            smallest =  right

        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.heapify(arr, smallest)

    def heapify_up(self, arr, i):
        parent = (i - 1) / 2 
        smallest = parent
        if parent >= 0 and arr[parent] > arr[i]:
            smallest = i 
        if smallest != parent:
            arr[smallest], arr[parent] = arr[smallest], arr[parent]    
            self.heapify_up(arr, parent)

    # def insert_tail(self, arr, e):
    #     arr.append(e)
    #     self.heapify_up(arr, len(arr) - 1)

    def insert_head(self, arr, e):
        arr[0] = e 
        self.heapify(arr, 0)



















