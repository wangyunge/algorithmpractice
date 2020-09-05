'''
QuickSort
'''
class HeapSort:
    def sort(self,nums):

        right_limit = len(nums)
        def _build_heap():
            for idx in range(0, (len(nums) + 1) // 2 ):
                _heapfy(idx)

        def _heapfy(idx):
            if 2*idx+1 < right_limit and nums[2*idx+1] < nums[idx] 
                if 2*idx+2 < right_limit and nums[2*idx+1] < nums[2*idx+2]:
                    nums[2*idx+1] , nums[idx] = nums[idx], nums[2*idx+1]
                    _heapfy[2*idx+1]
                if 2*idx+2 >= right_limit:
                    _heapfy[2*idx+1] 

            elif 2*idx+2 < right_limit and nums[2*idx+2] < nums[idx] and nums[2*idx+2] < nums[2*idx+1]:
                nums[2*idx+2] , nums[idx] = nums[idx], nums[2*idx+2]
                _heapfy[2*idx+2]

        _build_heap()
        while right_limit > 0:
            nums[0], nums[right_limit]

        return nums[::-1]



def main():
    test = [2,3,1,7,5,3,2]
    sol = HeapSort()
    res = sol.sort(test)
    print res
if __name__ == '__main__':
    main()
