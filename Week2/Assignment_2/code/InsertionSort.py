class InsertionSort:
    '''The InsertionSort class allows the client to sort a list using an 
    implementation of the insertion sort algorithm
    '''
    def __init__(self, data) -> None:
        '''params:
        data: list - list to be sorted '''
        self.data = data

    def sort(self):
        '''sorts the instance variable data, using insertion sort'''
        for j in range(1, len(self.data)):
            key = self.data[j]
            i = j-1
            while i > -1 and self.data[i] > key:
                self.data[i+1] = self.data[i]
                i -= 1
            self.data[i+1] = key
