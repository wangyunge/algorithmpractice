'''
QuickSort
'''
class QuickSorter1:
    def sort(self,nums):
        self.nums = nums
        L = 0
        R = len(nums) - 1
        self.recursiveSort(L,R)
        return self.nums
    def recursiveSort(self,L,R):
        if L < R:
            mid = self.partition(L,R)
            self.recursiveSort(L,mid-1)
            self.recursiveSort(mid+1,R)
    def partition(self,start,end):
        left = start
        right = end
        rivet = self.nums[start]
        while left < right:
            while self.nums[left] <= rivet and left < right:
                left += 1
            while self.nums[right] > rivet and left < right:
                right -= 1
            self.nums[left],self.nums[right] = self.nums[right],self.nums[left]
        
        if self.nums[start] >= self.nums[left]:
            self.nums[start],self.nums[left] = self.nums[left],self.nums[start]
        else:
            left -= 1
            self.nums[start],self.nums[left] = self.nums[left],self.nums[start]
        return left
class QuickSorter2(object):
    def sort(self,arr):
        self.arr = arr
        left = 0
        right = len(arr)-1
        self.sortHelper(left,right)
        return self.arr
    def sortHelper(self,left,right):
        if left < right:
            pivot = self.partition(left,right)
            self.sortHelper(left,pivot-1)
            self.sortHelper(pivot+1,right)
    def partition(self,left,right):
        povit = left
        for i in xrange(left+1,right+1):
            if self.arr[i] <= self.arr[left]:
                povit += 1
                self.arr[i],self.arr[povit] = self.arr[povit],self.arr[i]
        self.arr[left],self.arr[povit] = self.arr[povit],self.arr[left]
        return povit

def main():
    test = [2,3,1,7,5,3,2]
    sol = QuickSorter2()
    res = sol.sort(test)
    print res
if __name__ == '__main__':
    main()