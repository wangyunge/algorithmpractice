'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return [] 
        self.res = []
        self.heap = []
        self.heap.append([0, 10000, 0])
        self.right_end = self.heap[0][1]
        for new_building in buildings:

            while self.right_end < new_building[0]:
                self.end_highest()

            if new_building[2] > self.heap[0][2]:
                self.res.append([new_building[0], new_building[2]])

            self.heap.append(new_building) 
            self.heapify_up(self.heap, len(self.heap)-1)
            self.right_end = self.heap[0][1]
        while len(self.heap) > 1  :
            self.end_highest()
        return self.res

    def end_highest(self):
        while self.right_end >= self.heap[0][1]:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify(self.heap, 0)
        self.res.append([self.right_end,self.heap[0][2]])
        self.right_end = self.heap[0][1]

    def heapify_up(self, arr, i):
        parent = (i - 1) / 2
        largest = parent
        if parent >= 0 and arr[i][2] > arr[parent][2]:
            largest = i 
        if largest != parent:
            arr[largest], arr[parent] = arr[parent], arr[largest]
            self.heapify_up(arr, parent)

    def heapify(self, arr, i):
        largest = i 
        left = i * 2
        right = i * 2 + 1
        if left < len(arr) and arr[left][2] > arr[largest][2]:
            largest = left
        if right < len(arr) and arr[right][2] > arr[largest][2]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest)

def main():

    sol = Solution()
    res = sol.getSkyline([[0,2147483647,2147483647]])
    print  res
if __name__ == '__main__':
    main()