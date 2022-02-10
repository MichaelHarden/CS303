from Search import Search
import random, time


class SearchDriver:

    def __init__(self) -> None:
        self.linear_time_log, self.binary_time_log = {}, {}
        self.keys = []

    def read_keys(self, filepath:str, delemiter=' '):
        '''file must be contain only numbers'''
        r_file = open(filepath, 'r')
        nums = r_file.readline()
        r_file.close()
        self.keys = list(map(int, nums.split(delemiter)))

    def time_algos(self):
        idx = 16
        limit = pow(2, 25)
        while not (idx > limit):

            #Generate number array to search
            search_space = [random.randint(1,idx) for _ in range(idx)]
            searcher = Search(search_space)

            # Linear Search
            linear_avg_time = 0
            for key in self.keys:
                start = time.time()
                searcher.linear(key)
                end = time.time()
                eclipsed = end-start
                linear_avg_time += eclipsed


            # Binary Search
            binary_avg_time = 0
            sort_time = time.time()
            searcher.data.sort()
            current_time = time.time()
            binary_avg_time += (current_time - sort_time)
            for key in self.keys:
                start = time.time()
                searcher.binary(key)
                end = time.time()
                eclipsed = end-start
                binary_avg_time += eclipsed

            # averages times for each array
            linear_avg_time /= len(self.keys)
            self.linear_time_log[idx] = linear_avg_time

            binary_avg_time /= len(self.keys)
            self.binary_time_log[idx] = binary_avg_time

            # Increment Index
            idx *= 2

    def test_linear(self):
        searcher = Search([5, 22, 12, 62, 50, 35, 62, 72, 85, 91])
        print('Expected idx: 2  Result idx:', searcher.linear(12))
        print('Expected idx: 9  Result idx:', searcher.linear(91))
        print ('Expected idx: 3  Result idx:', searcher.linear(62))
        print('Expected idx: -1  Result idx:', searcher.linear(15))

        searcher2 = Search([4])
        print('Expected idx: 0  Result idx:', searcher2.linear(4))




    def test_binary(self):
        searcher = Search([5, 22, 12, 62, 50, 35, 62, 72, 85, 91])
        searcher.data.sort()
        print('Expected idx: 1  Result idx:', searcher.binary(12))
        print('Expected idx: 9  Result idx:', searcher.binary(91))
        print('Expected idx: 5  Result idx:', searcher.binary(62))
        print('Expected idx: -1  Result idx:', searcher.binary(15))

        searcher2 = Search([1, 2, 3, 4, 5, 6, 7, 8, 9])
        print('Expected idx: 3  Result idx:', searcher2.binary(4))
        print('Expected idx: 8  Result idx:', searcher2.binary(9))
        print('Expected idx: 0  Result idx:', searcher2.binary(1))

        searcher3 = Search([19])
        print('Expected idx: 0  Result idx:', searcher3.binary(19))
        print('Expected idx: -1  Result idx:', searcher3.binary(11))


if __name__ == '__main__':

    driver = SearchDriver()
    driver.read_keys('Numbers.txt')

    # For Testing The Searching Algorithms
    # driver.test_linear()
    # driver.test_binary()

    ### For timing the Searching Algorithms
    driver.time_algos()
    print(driver.binary_time_log)
    print(driver.linear_time_log)
    pass
