from Sorts import Sorts
import time

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

        ### TIMING MERGE SORT
        for file in file_names:
            # loads in the data from the current file using
            self.load_file(file)

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
            self.load_file(file)

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
            self.load_file(file)
            
            # passes data on to the sorting class
            clss = Sorts(self.data)

            # stores the start time, sorts, and then compares the start to end 
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.insertion_sort()
            end = time.time()
            elapsed = end - start
            print (file, "insertion sorting time :", elapsed)

    def test_merge(self, lst:list[int]):
        '''tests the merge sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.merge_sort()
        return clss.data
        
    def test_insertion(self, lst:list[int]):
        '''tests the insertion sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.insertion_sort()
        return clss.data

    def test_heap(self, lst:list[int]):
        '''tests the insertion sort method. Sorts the list passed through the parameter
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = Sorts(lst)
        clss.heap_sort()
        return clss.data

    def test_heap_in100(self):
        self.load_file("input_100.txt")
        sorter = Sorts(self.data)
        sorter.heap_sort()
        print(sorter.data)

if __name__ == '__main__':
    driver = SortsDriver()

    ### Timing the sort Method - uncomment the following method call to time the sorting method.
    driver.time_method()

    ### Testing Heap Sort Method - uncomment the following test cases for them to run.
    # print(driver.test_heap([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    # print(driver.test_heap([4, 3, 3, 3, 2, -2]))
    # print(driver.test_heap([-3, -103, - 5, -2, -10, -44, -31]))
    # print(driver.test_heap([10]))
    # print(driver.test_heap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    # print(driver.test_heap([]))

    ### Testing Heap Sort method with the input_100.txt file - uncomment the following line to run
    # driver.test_heap_in100()

    
    
