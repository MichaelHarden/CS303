class HashMap:
    
    _hash = lambda key, i: (7*key + 1) 
    _quadratic = lambda key, i: (key + i*i) 
    _linear = lambda key, i: (key + 1) 

    def __init__(self, size, probing):
        self._table = [None for _ in range(size)]
        self._size = size
        self._probing = probing

        
    def put(self, key, value):
        '''puts a key value pair in to the hash map based on the prescriped probing function'''
        start_key = key % self._size
        current_key = start_key
        current_val = self._table[current_key]

        i=1
        while (current_val is not None):
            current_key = self._probing(current_key, i) % self._size
            current_val = self._table[current_key]
            if current_key == start_key:
                break
            i +=1
        self._table[current_key] = (key, value)

    def get(self, key):
        '''gets a value in a hash map if its present, otherwise, returns False'''
        start_key = key % self._size
        current_key = start_key
        current_val = self._table[current_key]

        i = 1
        while (current_val is not None):
            if current_val[0] == key:
                return current_val
            current_key = self._probing(current_key, i) % self._size
            current_val = self._table[current_key]
            if current_key == start_key:
                return False
            i +=1
        return False





