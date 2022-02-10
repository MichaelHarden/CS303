from HashMap import HashMap
import time

greeting = """
====================================================================================================

    Hello, Welcome to the HashTable test enviroment!

    If you would like to fill up a Hash Map with your own values please enter: 1

    If you want to test the run time to search for values in the hash table press 2:

"""

prob_requ = """
Enter desired probing method:

    1: (defalt) hash function (7H(x) + 1)

    2: linear probing (H(x) + 1)

    3: quadratic probing (H(x) + i**2)


"""


class Driver:

    def start(self):

        ''' allows for user input and all terminal control'''
        option = int(input(greeting))
        
        if option == 1:
            size = int(input("\n\n Enter size of table:\t"))
            probing_meth = int(input(prob_requ))

            probe = HashMap._hash
        
            if probing_meth == 2:
                probe = HashMap._linear
            elif probing_meth == 3:
                probe = HashMap._quadratic

            table = HashMap(size, probe)
            for _ in range(size):
                key = int(input("Enter key:\t"))
                value = input("Enter value:\t")
                table.put(key, value)
            
            search = 0
            while search != -1:
                search = int(input("Enter key to search.\nEnter '-1' to exit\n"))
                print(table.get(search))


        elif option == 2:
            self.time()


    def load_file(self, file_path):
        '''loads the content of a file'''
        opened = open(file_path)
        content = opened.readlines()
        opened.close()
        content = [line.strip().split(',', maxsplit=1) for line in content]
        content = [(int(line[0]), line[1]) for line in content]
        return content

    def load_keys(self, file_path):
        '''loads the keys file'''
        opened = open(file_path)
        keys = [int(word) for word in opened.readlines()]
        opened.close()
        return keys

    def time(self):
        '''times the get method'''
        files = ["newUPC.csv", "newUPC-random.csv"]
        sizes = [50, 100, 500, 1_000]
        probes = [(HashMap._hash, "7H(x) + 1"), (HashMap._linear, "Linear"), (HashMap._quadratic, "Quadratic")]
        keys = self.load_keys("../files/KEYs.csv")

        for f in files:
            content = self.load_file('../files/'+ f)


            for prob in probes:
                for s in sizes: 

                    table = HashMap(s, prob[0])
                    for item in content:
                        table.put(*item)

                    start = time.time()
                    for key in keys:
                        table.get(key)
                    end = time.time()
                    elapsed = end - start
                    avg = elapsed / len(keys)
                    print(f"Table size: {s}\t Probing method: {prob[1]}\t file: {f}\tAverage Search Time: {avg}\t Total Search Time: {elapsed}")
                    
                        
    def test_hash_map(self):
        '''tests the implementation of the hash map data structure'''
        table = HashMap(8, HashMap._hash)
        table.put(1, 'a')
        table.put(2, 'b')
        table.put(3, 'c')
        table.put(4, 'd')
        table.put(5, 'e')
        table.put(6, 'f')
        table.put(7, 'g')
        table.put(8, 'h')
        table.put(9, 'i')

        print(f"when using has key 1: Expected False\t {table.get(1)}")
        print(f"when using hash key 9: Expected (9, i)\t {table.get(9)}")
        print(f"when using hash key 5: Expected (5, f)\t {table.get(5)}")

        
        table = HashMap(8, HashMap._linear)
        table.put(1, 'a')
        table.put(2, 'b')
        table.put(3, 'c')
        table.put(4, 'd')
        table.put(5, 'e')
        table.put(6, 'f')
        table.put(7, 'g')
        table.put(8, 'h')
        table.put(9, 'i')

        print(f"when using linear key 1: Expected False\t {table.get(1)}")
        print(f"when using linear key 9: Expected (9, i)\t {table.get(9)}")
        print(f"when using linaer key 5: Expected (5, f)\t {table.get(5)}")


        table = HashMap(8, HashMap._quadratic)
        table.put(1, 'a')
        table.put(2, 'b')
        table.put(3, 'c')
        table.put(4, 'd')
        table.put(5, 'e')
        table.put(6, 'f')
        table.put(7, 'g')
        table.put(8, 'h')
        table.put(9, 'i')

        print(f"when using quadratic key 1: Expected False\t {table.get(1)}")
        print(f"when using quadratic key 9: Expected (9, i)\t {table.get(9)}")
        print(f"when using quadratic key 5: Expected (5, f)\t {table.get(5)}")
        

    def test_probing(self):
        table = HashMap(5, HashMap._hash)
        table.put(0, 'a')
        table.put(8, 'b')
        table.put(16, 'c')
        table.put(24, 'd')
        table.put(32, 'e')

        print(f"when using hash, key: 0\t Expected: (0, 'a')\t{table.get(0)}")
        print(f"when using hash, key: 8\t Expected: (8, 'b')\t{table.get(8)}")
        print(f"when using hash, key: 16\t Expected: (16, 'c')\t{table.get(16)}")
        print(f"when using hash, key: 24\t Expected: (24, 'd')\t{table.get(24)}")
        print(f"when using hash, key: 32\t Expected: (32, 'e')\t{table.get(32)}")

        table = HashMap(5, HashMap._hash)
        table.put(0, 'a')
        table.put(8, 'b')
        table.put(16, 'c')
        table.put(24, 'd')
        table.put(32, 'e')

        print(f"when using linear, key: 0\t Expected: (0, 'a')\t{table.get(0)}")
        print(f"when using linear, key: 8\t Expected: (8, 'b')\t{table.get(8)}")
        print(f"when using linear, key: 16\t Expected: (16, 'c')\t{table.get(16)}")
        print(f"when using linear, key: 24\t Expected: (24, 'd')\t{table.get(24)}")
        print(f"when using linear, key: 32\t Expected: (32, 'e')\t{table.get(32)}")
    
        table = HashMap(5, HashMap._hash)
        table.put(0, 'a')
        table.put(8, 'b')
        table.put(16, 'c')
        table.put(24, 'd')
        table.put(32, 'e')

        print(f"when using quadratic, key: 0\t Expected: (0, 'a')\t{table.get(0)}")
        print(f"when using quadratic, key: 8\t Expected: (8, 'b')\t{table.get(8)}")
        print(f"when using quadratic, key: 16\t Expected: (16, 'c')\t{table.get(16)}")
        print(f"when using quadratic, key: 24\t Expected: (24, 'd')\t{table.get(24)}")
        print(f"when using quadratic, key: 32\t Expected: (32, 'e')\t{table.get(32)}")


if __name__ == "__main__":
    driver = Driver()
    driver.start()
    
    # driver.test_hash_map()
    # driver.test_probing()

