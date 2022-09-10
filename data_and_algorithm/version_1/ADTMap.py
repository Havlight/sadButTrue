class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __hash__(self, key, size):
        return key % size

    def rehash(self, oldHash, size):
        return (oldHash + 1) % size

    def put(self, key, data):
        hashvalue = self.__hash__(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslots = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslots] != None and self.slots[nextslots] != key:
                    nextslots = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslots] == None:
                    self.data[nextslots] = data
                    self.slots[nextslots] = key

    def get(self, key):
        startslots = self.__hash__(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslots
        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslots:
                    stop = True
            return data

    def __getitem__(self, item):
        self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)
