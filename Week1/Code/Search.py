class Search:

    def __init__(self, data:list[int]) -> None:
        self.data = data

    def linear(self, key):
        '''returns index of key if key is in data. 
        else returns -1'''
        for i in range(len(self.data)):
            if self.data[i] == key:
                return i
        return -1

    def binary(self, key):
        '''class data must be sorted'''
        return self.__binary_assist(0, len(self.data)-1, key)

    def __binary_assist(self, left, right, key):
        if left > right:
            return -1
        mid = (left + right) // 2
        if key == self.data[mid]:
            return mid
        elif key > self.data[mid]:
            return self.__binary_assist(mid+1, right, key)
        else:
            return self.__binary_assist(left, mid-1, key)
