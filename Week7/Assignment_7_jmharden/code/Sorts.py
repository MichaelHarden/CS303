class Sorts:
    '''The InsertionSort class allows the client to sort a list using an 
    implementation of the insertion sort algorithm. 
    '''
    def __init__(self, data):
        '''params:
        data: list - list to be sorted '''
        self.data = data


### --- INSERTION SORT ---

    def insertion_sort(self):
        '''sorts the instance variable data, using insertion sort'''
        for j in range(1, len(self.data)):
            key = self.data[j]
            i = j-1
            while i > -1 and self.data[i] < key:
                self.data[i+1] = self.data[i]
                i -= 1
            self.data[i+1] = key



### --- SELECTION SORT ---

    def selection_sort(self):
        
        for i in range(len(self.data)-1):
            smallest_idx = i
            for j, curr_num in zip(range(i+1, len(self.data)), self.data[i+1:]):
                if curr_num < self.data[smallest_idx]:
                    smallest_idx = j
            self.swap(i, smallest_idx) 



### --- REVERSE SELECTION SORT ---

    def reverse_selection_sort(self):
        for i in range(len(self.data)-1):
            smallest_idx = i
            for j, curr_num in zip(range(i+1, len(self.data)), self.data[i+1:]):
                if curr_num > self.data[smallest_idx]:
                    smallest_idx = j
            self.swap(i, smallest_idx) 



### --- BUBBLE SORT ---

    def bubble_sort(self):
        if len(self.data) <= 1:
            return
        
        for i in range(len(self.data)-1):

            noSwaps = True
            for j in range(len(self.data)-i-1):
                if self.data[j] > self.data[j+1]:
                    self.swap(j, j+1)
                    noSwaps = False
                
            if noSwaps:
                return



### --- REVERSE BUBBLE SORT ---

    def reverse_bubble_sort(self):
        if len(self.data) <= 1:
            return

        noSwaps = True
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-i-1):
                if self.data[j] < self.data[j+1]:
                    self.swap(j, j+1)
                    noSwaps = False

        
        if noSwaps:
            return

### --- QUICK SORT ---

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
            if self.data[left] < pivot and self.data[right] > pivot:
                self.swap(left, right)
            if self.data[left] >= pivot:
                left += 1
            if self.data[right] <= pivot:
                right -= 1
        self.swap(last_idx, left)
        self.__quick_sort_helper(first_idx, right)
        self.__quick_sort_helper(left+1, last_idx)
        


### --- MEDIAN VALUE QUICK SORT ---
    def quick_sort_med_piv(self):
        self.__quick_sort_helper_med_piv(0, len(self.data)-1)
        
    # QUICK SORT HELPERS
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
            if self.data[left] < self.data[pivot_idx] and self.data[right] > self.data[pivot_idx]:
                self.swap(left, right)
            if self.data[left] >= self.data[pivot_idx]:
                left += 1
            if self.data[right] <= self.data[pivot_idx]:
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



### --- HEAP SORT ---

    def heap_sort(self):
        '''Sorts a list using heap sort'''
        self.build_min_heap()
        heapSize = len(self.data)
        for i in range(len(self.data)-1, 0, -1):
            self.swap(0, i)
            heapSize -= 1
            self.min_heapify(0, heapSize)

    # HEAP SORT HELPERS
    def build_min_heap(self):
        '''Builds a max heap out of the instance variable data'''
        heapSize = len(self.data)
        for i in range(heapSize, -1, -1):
            self.min_heapify(i, heapSize)

    def min_heapify(self, i, heapSize):
        '''Takes an array and starting at index i reheapify a max heap for every element under i. 
        heapSize tells the code where in the array is the end of the heap'''
        leftChild = (2*i) + 1
        rightChild = (2*i) + 2
        largest = i
        if leftChild < heapSize and self.data[leftChild] < self.data[largest]:
            largest = leftChild
        if rightChild < heapSize and self.data[rightChild] < self.data[largest]:
            largest = rightChild
        if largest != i:
            self.swap(i, largest)
            self.min_heapify(largest, heapSize)



### --- MERGE SORT ---

    def merge_sort(self):
        if len(self.data) <= 1:
            return
        aux_arr = self.data[:]
        self.__merge_helper(self.data, 0, len(self.data)-1, aux_arr)
        
    # MERGE SORT HELPERS 
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
            elif temp_arr[i] >= temp_arr[j]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                arr[k] = temp_arr[j]
                j += 1
            k += 1
        return arr



### --- MIN MAX SORT ---

    def min_max_sort(self):
        if len(self.data) <= 1:  # if there is only one element, the list is sorted
            return self.data

        # left and right pointers, where the min and max elements will be inserted.
        l, r = 0, len(self.data) - 1
        # these pointers for each iteration move in towards one another by one index until they are equal.
        # if they are equal, the last element will already be in the correct place.
        while (l < r):
            ### the first index is assumed to be the largest and smallest elements
            min_ptr, max_ptr = l, l
            ### finds the actual smallest and largests elements
            for i in range(l+1, r+1):
                if self.data[i] < self.data[min_ptr]:
                    min_ptr = i
                elif self.data[i] > self.data[max_ptr]:
                    max_ptr = i

        # checks 3 conditions to proprly insert the min and max values in the array.
            if (max_ptr == r) and (min_ptr == l):
                self.swap(max_ptr, min_ptr)
            elif (max_ptr == r):
                self.swap(max_ptr, l)
                self.swap(min_ptr, r)
            else:
                self.swap(min_ptr, r)
                self.swap(max_ptr, l)

            ### narrows the seraching range for the next iteration so the same max and min aren't found again.
            l, r = l+1, r-1

### OTHER METHODS

    def swap(self, swapA, swapB):
        '''swaps the two elemetns in place in an array at the given indecies'''
        self.data[swapA], self.data[swapB] = self.data[swapB], self.data[swapA]
