class Sorts:
    '''The InsertionSort class allows the client to sort a list using an 
    implementation of the insertion sort algorithm
    '''
    def __init__(self, data) -> None:
        '''params:
        data: list - list to be sorted '''
        self.data = data

    def insertion_sort(self):
        '''sorts the instance variable data, using insertion sort'''
        for j in range(1, len(self.data)):
            key = self.data[j]
            i = j-1
            while i > -1 and self.data[i] > key:
                self.data[i+1] = self.data[i]
                i -= 1
            self.data[i+1] = key



    def merge_sort(self):
        if len(self.data) <= 1:
            return
        aux_arr = self.data[:]
        self.__merge_helper(self.data, 0, len(self.data)-1, aux_arr)
        

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

