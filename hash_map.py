class HashMap:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.


    def __init__(self, initial_capacity=10):
        # initialize the hash map with empty bucket list entries.
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    #create a hash key
    #o(1)
    def hash_key(self, key):
        return int(key) % len(self.map)

    #insert package info into the table
    #o(n) one for loop
    def insert(self, key, value):
        #get index
        key_hash = self.hash_key(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

        # Searches for an item with matching key in the hash table.
        # Returns the item if found, or None if not found.
    #search for a package in the hash table
    #o(n) one for loop
    def search(self, key):
        key_hash = self.hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    #update a package in the hash table
    #o(n) one loop
    def update(self, key, value):
        key_hash = self.hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    print(pair[1])
                    return True


