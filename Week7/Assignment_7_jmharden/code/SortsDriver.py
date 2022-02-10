from Sorts import Sorts
import time

class SortsDriver:
    '''SortsDriver implements the Sorts class. It provides methods
    to test the sorting algorithms in the Sort class, and calculates runtime for 
    sorting a list, and to parse a file of integers.
    '''
        

    def load_file(self, filepath, delimiter=' '):
        '''load_file parses a file, and stores its content in the varible data.
        param:
            filepath: str, the filepath for the file to parse. /filename would be
            searching in the same directory where InsertionDrivdr.py is stored
        
            delimiter: str (defaults ' ') the sring to split the file with.
        '''
        # opens the file for reading, then reads the file and stores its content
        # into content.
        num_file = open(filepath, 'r')
        content = num_file.read()
        num_file.close()

        # splits the content along the passed delimiter and reassigns to content. 
        # Converts each str(int) inside content into an int.
        content = content.strip()
        content = content.split(delimiter)
        content = [int(num) for num in content]

        #stores the parsed data into the data var
        self.data = content



    def time_method(self):
        '''calculates the time to sort each of the required files
        '''
        file_names = ['input_100.txt', 'input_1000.txt', 'input_5000.txt',
                      'input_10000.txt', 'input_50000.txt']

        ### --- TIMING QUICK SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.quick_sort_med_piv()
            end = time.time()
            elapsed = end - start
            print(f"sorting {file} with quick sort - time elapsed :  {elapsed} ")


        ### --- TIMING MERGE SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.merge_sort()
            end = time.time()
            elapsed = end - start
            print(f'sorting {file} with merge sort - time elapsed :  {elapsed}')


        ### --- TIMING HEAP SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.heap_sort()
            end = time.time()
            elapsed = end - start
            print(f'sorting {file} with heap sort - time elapsed :  {elapsed}')


        ### --- TIMING MIN MAX SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.min_max_sort()
            end = time.time()
            elapsed = end - start
            print(f'sorting {file} with min max sort - time elapsed :  {elapsed}')
        
         ### --- TIMING SELECTION SORT ---
        

        ### --- TIMING INSERTION SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.insertion_sort()
            end = time.time()
            elapsed = end - start
            print(f'sorting {file} with insertion sort - time elapsed :  {elapsed}')
        

        ### --- TIMING SELECTION SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)
            
            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end 
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.reverse_selection_sort()
            end = time.time()
            elapsed = end - start
            print(
                f'sorting {file} with selection sort - time elapsed :  {elapsed}')


        ### --- TIMING BUBBLE SORT ---
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.reverse_bubble_sort()
            end = time.time()
            elapsed = end - start
            print(f'sorting {file} with bubble sort - time elapsed :  {elapsed}')



    def time_selection_sort(self):
        
        files = ['Input_Random.txt', 'Input_ReversedSorted.txt', 'Input_Sorted.txt']
        ### TIMING QUICK SORT WITH MEDIAN VALUE
        for file in files:
            # loads in the data from the current file using
            self.load_file('../tests/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.selection_sort()
            end = time.time()
            elapsed = end - start
            print(file + "  selection sort time :", elapsed)



    def time_bubble_sort(self):
        
        files = ['Input_Random.txt', 'Input_ReversedSorted.txt', 'Input_Sorted.txt']
        ### TIMING QUICK SORT WITH MEDIAN VALUE
        for file in files:
            # loads in the data from the current file using
            self.load_file('../tests/' + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.bubble_sort()
            end = time.time()
            elapsed = end - start
            print(file + "  bubble sort time :", elapsed)


            
    def test_insertion_sort(self, lst):
        '''tests the insertion sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.insertion_sort()
        return clss.data

    def test_merge_sort(self, lst):
        '''tests the merge sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.merge_sort()
        return clss.data

    def test_heap_sort(self, lst):
        '''tests the heap sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.heap_sort()
        return clss.data

    def test_quick_sort(self, lst):
        '''tests the quick sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.quick_sort()
        return clss.data
    
    def test_quick_sort_med(self, lst):
        '''tests the quick sort with median piviot method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.quick_sort_med_piv()
        return clss.data

    def test_min_max_sort(self, lst):
        '''tests the min max sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.min_max_sort()
        return clss.data

    def test_selection_sort(self, lst):
        '''tests the selection sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.selection_sort()
        return clss.data

    def test_bubble_sort(self, lst):
        '''tests the bubble sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.bubble_sort()
        return clss.data
    
    def test_reverse_selection_sort(self, lst):
        '''tests the reversed selection sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.reverse_selection_sort()
        return clss.data

    def test_reverse_bubble_sort(self, lst):
        '''tests the reversed bubble sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.reverse_bubble_sort()
        return clss.data




if __name__ == '__main__':
    driver = SortsDriver()

    
###  --- TIMING THE SORTING METHODS ---
### uncomment the following method calls to time the sorting method.

    driver.time_method()


### --- TIMING THE SELECTION AND BUBBLE SORT METHODS ---
### uncomment the following method calls to time the sorting method.

    # driver.time_selection_sort()
    # driver.time_bubble_sort()


###  --- TEST REVERSE INSERTION SORT --- 
### uncomment the following method calls to time the sorting method.

    # print(driver.test_insertion_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_insertion_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_insertion_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_insertion_sort([4, 2]))
    # print(driver.test_insertion_sort([10]))
    # print(driver.test_insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_insertion_sort([]))


###  --- TEST REVERSE MERGE SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_merge_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_merge_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_merge_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_merge_sort([4, 2]))
    # print(driver.test_merge_sort([10]))
    # print(driver.test_merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_merge_sort([]))


###  --- TEST REVERSE HEAP SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_heap_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_heap_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_heap_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_heap_sort([4, 2]))
    # print(driver.test_heap_sort([10]))
    # print(driver.test_heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_heap_sort([]))


###  --- TEST REVERSE QUICK SORT WITH MEDIAN --- 
### uncomment the following method calls to time the sorting method.

    # print(driver.test_quick_sort_med([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_quick_sort_med([4, 3, 3, 3, 2, -2]))
    # print(driver.test_quick_sort_med([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_quick_sort_med([4, 2]))
    # print(driver.test_quick_sort_med([10]))
    # print(driver.test_quick_sort_med([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_quick_sort_med([]))
    

### --- TEST REVERSE QUICK SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_quick_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_quick_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_quick_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_quick_sort([4, 2]))
    # print(driver.test_quick_sort([10]))
    # print(driver.test_quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_quick_sort([]))


###  --- TEST REVERSE MIN MAX SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_min_max_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_min_max_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_min_max_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_min_max_sort([4, 2]))
    # print(driver.test_min_max_sort([10]))
    # print(driver.test_min_max_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_min_max_sort([]))

    
###  --- TEST SELECTION SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_selection_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_selection_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_selection_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_selection_sort([4, 2]))
    # print(driver.test_selection_sort([10]))
    # print(driver.test_selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_selection_sort([]))


###  --- TEST BUBBLE SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_bubble_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_bubble_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_bubble_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_bubble_sort([4, 2]))
    # print(driver.test_bubble_sort([10]))
    # print(driver.test_bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_bubble_sort([]))


###  --- TEST REVERSE SELECTION SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_reverse_selection_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_reverse_selection_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_reverse_selection_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_reverse_selection_sort([4, 2]))
    # print(driver.test_reverse_selection_sort([10]))
    # print(driver.test_reverse_selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_reverse_selection_sort([]))


###  --- TEST REVERSE BUBBLE SORT ---
### uncomment the following method calls to time the sorting method.

    # print(driver.test_reverse_bubble_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1]))
    # print(driver.test_reverse_bubble_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_reverse_bubble_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_reverse_bubble_sort([4, 2]))
    # print(driver.test_reverse_bubble_sort([10]))
    # print(driver.test_reverse_bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_reverse_bubble_sort([]))
