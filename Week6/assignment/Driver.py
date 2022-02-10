from Sorts import Sorts

class Driver:
    """Driver class provides methods which implement the two algorithms found in Sorts.py 
    for testing"""
    
    def load_log_file(self, file_path):
        """load_file parses an log file, such as 'NovelSortInput.txt' which is provided on canvas,
        in to an array which can be sorted. each index of the array contains a touple. 
        The first index of the touple contains the city name, an the second index of the touple 
        contains the time of which the log was placed. Both indecis are stored as a string
        
        param:
            file_path: (str) directory path to the log file"""

        # reads in the content of the file into 'content'
        opened_file = open(file_path, 'r')
        content = opened_file.read()
        opened_file.close()

        # strips away leading and trailing white space
        content = content.strip()

        # parses the content based on the delimeter '\n\n'
        content = content.split('\n\n')

        # in each line the last 8 indeces are dedicated to the time stamp. 
        # everything prior is the city name
        content = [(line[:-9], line[-8:]) for line in content]

        self.sales = content

    def sort_logs(self, file_path):
        """sort_logs takes a file path to a logs file and passes it into merge_sort
        in the Sorts class to be sorted. Merge sort is chosen for this process due to being
        a stable sort. Thus the time stamps stay sorted
        
        param: 
            file_path: (str) directory path to the log file
            
        return:
            list[(city name (str), timestamp (str))]"""

        self.load_log_file(file_path)
        sorted_log = Sorts().merge_sort(self.sales)
        return self.sales
    
    def test_min_max_sort(self, array):
        """test_min_max_sort takes an array and passes it into the min_max_sorting algorithm 
        found in the Sorts class to be sorted
        
        param:
            array: (list[int]) the array which is to be sorted 
            
        return:
            (str) contains pre-sort and post-sorted array """


        return f"pre-sort array  :  {array}\nPost-sort array  :  {Sorts().min_max_sort(array)}"




if __name__ == "__main__":
    driver = Driver()

### --- UNCOMMENT LINES BELOW TO RUN OR COMMENT TO NOT RUN THEM ---

### --- TESTS THE LOGS SORTING ---
    print("\nSORTING LOGS\n")
    logs = driver.sort_logs('NovelSortInput.txt')
    for log in logs:
        print(log, '\n')

### --- TESTS THE LOGS SORTING FOR MULTI WORD CITIES ---
    print("\nSORTING LOGS WITH MUTLI WORD CITIES\n")
    logs = driver.sort_logs('NovelSortInput_2.txt')
    for log in logs:
        print(log, '\n')

### --- TESTS THE MIN_MAX_SORT ---

    print("\nTEST CASES FOR MIN_MAX_SORT\n")
    print(driver.test_min_max_sort([5, 1, 20, 52, 17, 22, 44, 0, 4, 3]))
    print(driver.test_min_max_sort([-1, -5, -7, -3, -2, -10]))
    print(driver.test_min_max_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(driver.test_min_max_sort([6, 1, 5, 2, 4, 3]))
    print(driver.test_min_max_sort([5, 5, 5, 5, 4, 5, 4]))
    print(driver.test_min_max_sort([1, 2, 3, 4, 5, 6]))
    print(driver.test_min_max_sort([1, 0]))
    print(driver.test_min_max_sort([0]))
    print(driver.test_min_max_sort([]))
  
