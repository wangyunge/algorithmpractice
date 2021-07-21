class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers)-1

        
        while left < right:
            mid = (left+right) // 2
            if numbers[right] < numbers[mid]:
                left = mid + 1
            elif numbers[mid] < numbers[left]:
                right = mid
            else:
                right += 1
        return numbers[left]

        while left < right:
            if numbers[left] < numbers[mid] and numbers[mid] > numbers[right]:
                left = mid + 1
            # elif numbers[left] < numbers[mid] and numbers[mid] < numbers[right]:
            #     return numbers[left]
            # elif numbers[left] < numbers[mid] and numbers[mid] == numbers[right]:
            #     return numbers[left]
            elif numbers[left] == numbers[mid] and numbers[mid] > numbers[right]:
                left = mid + 1
            # elif numbers[left] == numbers[mid] and numbers[mid] < numbers[right]:
            #     return numbers[left]
            elif numbers[left] == numbers[mid] and numbers[mid] == numbers[right]:
                left += 1

            elif numbers[left] > numbers[mid] and numbers[mid] > numbers[right]:
                pass
            elif numbers[left] > numbers[mid] and numbers[mid] < numbers[right]:
                right = mid 
            elif numbers[left] > numbers[mid] and numbers[mid] = numbers[right]:
                right = mid 




