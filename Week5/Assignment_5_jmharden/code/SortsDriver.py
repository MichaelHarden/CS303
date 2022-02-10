from Sorts import Sorts
import time
import sys

class SortsDriver:
    '''InsertionDriver  mplements the InsertionSort class. It provides methods
    to test the methods in the InsertionSort class, to calculate runtime for 
    sorting a list, and to parse a file of integers.
    '''

    def __init__(self):
        self.data = list[int]

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
                      'input_10000.txt', 'input_50000.txt', 'input_100000.txt', 
                      'input_500000.txt']

        ### TIMING QUICK SORT
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
            print(file, "quick sorting, with median pivot, time :", elapsed)


        ### TIMING MERGE SORT
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
            print(file, "merge sorting time :", elapsed)

        ### TIMING HEAP SORT
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
            print(file, "heap sorting time :", elapsed)

        ### TIMING INSERTION SORT
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
            print (file, "insertion sorting time :", elapsed)



    def compare_quick_sorts(self, files, path):
        

        ### TIMING QUICK SORT WITH MEDIAN VALUE
        for file in files:
            # loads in the data from the current file using
            self.load_file(path + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.quick_sort_med_piv()
            end = time.time()
            elapsed = end - start
            print(file, "quick sorting, with median pivot, time :", elapsed)

        ### TIMING QUICK SORT
        for file in files:
            # loads in the data from the current file using
            self.load_file(path + file)

            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.quick_sort()
            end = time.time()
            elapsed = end - start
            print(file, "quick sorting, with last index pivot, time :", elapsed)


    def test_quick_sort(self, lst:list[int]):
        '''tests the insertion sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.quick_sort()
        return clss.data
    
    def test_quick_sort_med(self, lst:list[int]):
        '''tests the insertion sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.quick_sort_med_piv()
        return clss.data


if __name__ == '__main__':
    driver = SortsDriver()

    quick_sort_input_files = [
        'input_16.txt', 'input_32.txt', 'input_64.txt',
        'input_128.txt', 'input_256.txt', 'input_512.txt',
        'input_1024.txt', 'input_2048.txt', 'input_4096.txt',
        'input_8192.txt'
    ]

    tests_files = [
        'Input_Random.txt',
        'Input_ReversedSorted.txt',
        'Input_Sorted.txt'
    ]
    
### Timing the sort Method - uncomment the following method call to time the sorting method.

    driver.time_method()



### Timing the Quick Sort methods using Sorted, Reverse sorted and Randomly sorted lists 
### -- uncomment the following 2 lines to compare the Quick sort implementations --

    # sys.setrecursionlimit(1500)
    # driver.compare_quick_sorts(tests_files, "../tests/")



### Timing the Quick Sort methods using the quick_sort_input files
### -- uncomment the following line to run --

    # driver.compare_quick_sorts(quick_sort_input_files, '../quick_sort_inputs/')
    


### Testing Quick Sort Method - uncomment the following test cases for them to run.
    # print(driver.test_quick_sort_med([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_quick_sort_med([4, 3, 3, 3, 2, -2]))
    # print(driver.test_quick_sort_med([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_quick_sort_med([4, 2]))
    # print(driver.test_quick_sort_med([10]))
    # print(driver.test_quick_sort_med([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_quick_sort_med([]))
    


### Testing Quick Sort Method - uncomment the following test cases for them to run.
    # print(driver.test_quick_sort([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_quick_sort([4, 3, 3, 3, 2, -2]))
    # print(driver.test_quick_sort([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_quick_sort([4, 2]))
    # print(driver.test_quick_sort([10]))
    # print(driver.test_quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_quick_sort([]))
    

    
    
