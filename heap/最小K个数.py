#sort   时间复杂度O(NlogN)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        arr.sort()
        return arr[:k]


#快排
class Solution(object):
    def getLeastNumbers(self, arr, k):
        # 方法一:partition方法(基于快速排序)
        if k > len(arr) or k <= 0:
            return [] 
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            print(index)
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low

#大根堆
class Solution(object):
    def getLeastNumbers(self, arr, k):
        if k <= 0 or k > len(arr):
            return []
        heap = self.build_heap(arr[:k])
        print(heap)
        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.sink(heap, 0)
        return heap

    def sink(self, array, k):
        n = len(array)
        left = 2 * k + 1
        right = 2 * k + 2
        if left >= n: return
        max_i = left 
        if right < n and array[left] < array[right]:
            max_i = right
        if array[max_i] > array[k]:
            array[max_i], array[k] = array[k], array[max_i]
            self.sink(array, max_i)

    def build_heap(self, list_):
        n = len(list_)
        for i in range(n//2, -1, -1):
            self.sink(list_, i)
        return list_