'''
QuickSort
'''
class QuickSorter:
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
def main():
    test = [2,3,1,7,5,3,2]
    sol = QuickSorter()
    res = sol.sort(test)
    print res
if __name__ == '__main__':
    main()