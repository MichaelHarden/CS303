from InsertionSort import InsertionSort
import time

class InsertionDriver:
    '''InsertionDriver  mplements the InsertionSort class. It provides methods
    to test the methods in the InsertionSort class, to calculate runtime for 
    sorting a list, and to parse a file of integers.
    '''

    def __init__(self) -> None:
        self.data = list[int]

    def load_file(self, filepath, delimiter=' '):
        '''load_file parses a file, and stores its content in the varible data.
        param:
            filepath: str, the filepath for the file to parse. /filename would be
            searching in the same directory where InsertionDrivdr.py is stored
        
            delimiter: str (default ' ') the sring to split the file with.
        '''
        # opens the file for reading, then reads the file and stores its content
        # into content.
        num_file = open(filepath, 'r')
        content = num_file.read()
        num_file.close()

        # splits the content along the passed delimiter and reassigns to content. 
        # Converts each str(int) inside content into an int.
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
        for file in file_names:
            # loads in the data from the current file using
            self.load_file('../inputs/' + file,)
            
            # passes data on to the sorting class
            clss = InsertionSort(self.data)

            # stores the start time, sorts, and then compares the start to end 
            # time. That time is saved in to elapsed, and printed to console
            start = time.time()
            clss.sort()
            end = time.time()
            elapsed = end - start
            print (file, "sorting time :", elapsed)

    def test(self, lst:list[int]):
        '''tests the sort method with the list pasted through the parameter.
        param:
            lst: list[int] list to be sorted
        '''
        # prints the list once it has been sorted
        clss = InsertionSort(lst)
        clss.sort()
        return clss.data
        


if __name__ == '__main__':
    driver = InsertionDriver()

    ### Timing the sort Method - uncomment the following method call to time the sorting method.
    driver.time_method()

    ### Testing Method - uncomment the following test cases for them to run.
    print(driver.test([10, 4, 6, 3, 2, 9, 16, 0, 3, -1])) 
    print(driver.test([4, 3, 3, 3, 2, -2]))
    print(driver.test([-3, -103, - 5, -2, -10, -44, -31]))
    print(driver.test([10]))
    print(driver.test([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(driver.test([]))
    
