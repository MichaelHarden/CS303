import random

class Sorts():

    def min_max_sort(self, arr):
        if len(arr) <= 1: # if there is only one element, the list is sorted
            return arr

        # left and right pointers, where the min and max elements will be inserted.
        l, r = 0 , len(arr) - 1
        # these pointers for each iteration move in towards one another by one index until they are equal.
        # if they are equal, the last element will already be in the correct place.
        while (l < r):
            ### the first index is assumed to be the largest and smallest elements
            min_ptr, max_ptr = l, l
            ### finds the actual smallest and largests elements
            for i in range(l+1, r+1):
                if arr[i] < arr[min_ptr]:
                    min_ptr = i
                elif arr[i] > arr[max_ptr]:
                    max_ptr = i
            
        # checks 3 conditions to proprly insert the min and max values in the array.
            if (max_ptr == l) and (min_ptr == r):
                self.swap(arr, max_ptr, min_ptr)
            elif (max_ptr == l):
                self.swap(arr, max_ptr, r)
                self.swap(arr, min_ptr, l)
            else:
                self.swap(arr, min_ptr, l)
                self.swap(arr, max_ptr, r)

            ### narrows the seraching range for the next iteration so the same max and min aren't found again.
            l, r = l+1, r-1

        return arr



    def merge_sort(self, arr):
        if len(arr) <= 1:
            return
        aux_arr = arr[:]
        self.__merge_helper(arr, 0, len(arr)-1, aux_arr)

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
            elif temp_arr[i][0] <= temp_arr[j][0]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                arr[k] = temp_arr[j]
                j += 1
            k += 1
        return arr



    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
            











