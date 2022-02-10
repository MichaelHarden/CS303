from BinarySearchTree import BST
import random
import time

class BTSDriver:
    
    def _load_file(self, file_path):
        csv = open(file_path)
        content = csv.read()
        csv.close()

        lines = content.split('\n')
        lines = [line.split(',', maxsplit=1) for line in lines]
        lines = [
            (int(line[0]), line[1][1:]) if line[1][0] == ','
            else (int(line[0]), line[1])
            for line in lines]

        return lines


    def csv_to_bst(self, file_path):
        lines = self._load_file(file_path)
        random.shuffle(lines)

        self.bst = BST()
        for line in lines:
            self.bst.insert(line)

         
    def load_test(self, file_path):
        return self._load_file(file_path)
        
    def time_BST(self):
        self.csv_to_bst('../UPC.csv')

        tests = self.load_test('../input.dat')

        start = time.time()
        for test in tests:
            self.bst.search(test[0])
        end = time.time()
        elapsed = end - start
        print(elapsed)


    def test_BST(self, key):
        return self.bst.search(key)

    def test_inorder(self):
        tree = BST()
        nodes = [5, 7, 3, 4, 9, 8, 10, 2, 1, 6]

        for node in nodes:
            tree.insert(node)
        
        tree.inorder()



if __name__ == '__main__':

    driver = BTSDriver()

### TIMES THE SEARCHING ###
# uncomment to run
    driver.time_BST()

### TESTS SEARCHING ###
# uncomment to run
    # driver.csv_to_bst('../UPC.csv')
    # print(
    #     f'key: 2056135    Expected value: "LB, BREWSTER CLBY JACK CUBES"\nActual value: {driver.test_BST(2056135).value}\n')
    # print(
    #     f'key: 6913403    Expected value: "1 lb,*KRAFT SHREDDED CHEESE BLEND"\nActual value: {driver.test_BST(6913403).value}\n')
    # print(
    #     f'key: 10016503    Expected value: "Tesco 2 little gem lettuce"\nActual value: {driver.test_BST(10016503).value}\n')

    # print(
    #     f'key: 11772728    Expected value: "None"\nActual value: {driver.test_BST(11772728)}\n')
    # print(
    #     f'key: 20262630    Expected value: "None"\nActual value: {driver.test_BST(20262630)}\n')
    # print(
    #     f'key: 15414542298    Expected value: "None"\nActual value: {driver.test_BST(15414542298)}\n')


### TESTS INORDER ###
# uncomment to run
    # driver.test_inorder()

