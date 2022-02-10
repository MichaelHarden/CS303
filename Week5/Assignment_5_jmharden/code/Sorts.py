class Sorts:
    '''The InsertionSort class allows the client to sort a list using an 
    implementation of the insertion sort algorithm
    '''
    def __init__(self, data) -> None:
        '''params:
        data: list - list to be sorted '''
        self.data = data


### INSERTION SORT

    def insertion_sort(self):
        '''sorts the instance variable data, using insertion sort'''
        for j in range(1, len(self.data)):
            key = self.data[j]
            i = j-1
            while i > -1 and self.data[i] > key:
                self.data[i+1] = self.data[i]
                i -= 1
            self.data[i+1] = key


### QUICK SORT

    ### Right index pivot
    def quick_sort(self):
        self.__quick_sort_helper(0, len(self.data)-1)
        

    def __quick_sort_helper(self, first_idx, last_idx):
        '''helper method to the quick_sort method. Sorts using the last index as partition

        param:
            first_idx: the index of the first element in the partition
            last_idx: the index of the last element in the partition
        '''
        if first_idx >= last_idx:
            return
        pivot = self.data[last_idx]
        left , right = first_idx , last_idx-1
        while (left <= right):
            if self.data[left] > pivot and self.data[right] < pivot:
                self.swap(left, right)
            if self.data[left] <= pivot:
                left += 1
            if self.data[right] >= pivot:
                right -= 1
        self.swap(last_idx, left)
        self.__quick_sort_helper(first_idx, right)
        self.__quick_sort_helper(left+1, last_idx)
        

    ### Median value pivot
    def quick_sort_med_piv(self):
        self.__quick_sort_helper_med_piv(0, len(self.data)-1)
        

    def __quick_sort_helper_med_piv(self, first_idx, last_idx):
        '''helper method to the quick_sort_med_piv method. 
        Sorts using the median of three index as partition
        
        param:
            first_idx: the index of the first element in the partition
            last_idx: the index of the last element in the partition
        '''
        if first_idx >= last_idx:
            return
        i, j, k = first_idx, last_idx, (first_idx + last_idx) // 2
        pivot_idx = self.median_of_3(i, j, k)
        self.swap(last_idx, pivot_idx)
        pivot_idx = last_idx

        left , right = first_idx , last_idx-1
        while (left <= right):
            if self.data[left] > self.data[pivot_idx] and self.data[right] < self.data[pivot_idx]:
                self.swap(left, right)
            if self.data[left] <= self.data[pivot_idx]:
                left += 1
            if self.data[right] >= self.data[pivot_idx]:
                right -= 1
        self.swap(last_idx, left)
        self.__quick_sort_helper_med_piv(first_idx, right)
        self.__quick_sort_helper_med_piv(left+1, last_idx)


    def median_of_3(self, i, j, k):
        '''Returns the median of the three parameters i, j, and k'''
        a, b, c = self.data[i], self.data[j], self.data[k]

        if (c < a and a < b) or (b < a and a < c):
            return i
        elif (a < c and c < b) or (b < c and c < a):
            return k
        else:
            return j


### HEAP SORT

    def heap_sort(self):
        '''Sorts a list using heap sort'''
        self.build_max_heap()
        heapSize = len(self.data)
        for i in range(len(self.data)-1, 0, -1):
            self.swap(0, i)
            heapSize -= 1
            self.max_heapify(0, heapSize)

    def build_max_heap(self):
        '''Builds a max heap out of the instance variable data'''
        heapSize = len(self.data)
        for i in range(heapSize, -1, -1):
            self.max_heapify(i, heapSize)

    def max_heapify(self, i, heapSize):
        '''Takes an array and starting at index i reheapify a max heap for every element under i. 
        heapSize tells the code where in the array is the end of the heap'''
        leftChild = (2*i) + 1
        rightChild = (2*i) + 2
        largest = i
        if leftChild < heapSize and self.data[leftChild] > self.data[largest]:
            largest = leftChild
        if rightChild < heapSize and self.data[rightChild] > self.data[largest]:
            largest = rightChild
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest, heapSize)


### MERGE SORT

    def merge_sort(self):
        if len(self.data) <= 1:
            return
        aux_arr = self.data[:]
        self.__merge_helper(self.data, 0, len(self.data)-1, aux_arr)
        
    ### HELPER METHODS

    def __merge_helper(self, arr, left, right, temp_arr):
        if left == right:
            return
        mid = (left + right) // 2
        self.__merge_helper(temp_arr, left, mid, arr)
        self.__merge_helper(temp_arr, mid+1, right, arr)
        self.__merge(arr, left, mid, right, temp_arr)

    def __merge(self, arr, left, mid, right, temp_arr):
        i, j, k = left, mid+1, left

        while i <= mid or j <= right:
            if i > mid:
                arr[k] = temp_arr[j]
                j += 1
            elif j > right:
                arr[k] = temp_arr[i]
                i += 1
            elif temp_arr[i] <= temp_arr[j]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                arr[k] = temp_arr[j]
                j += 1
            k += 1
        return arr

### OTHER METHODS

    def swap(self, swapA, swapB):
        '''swaps the two elemetns in place in an array at the given indecies'''
        self.data[swapA], self.data[swapB] = self.data[swapB], self.data[swapA]
