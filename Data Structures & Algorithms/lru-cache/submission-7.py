class LRUCache:

    def __init__(self, capacity: int):
        self.dictionary = {}
        self.capacity = capacity
        self.empty_array = []

    def get(self, key: int) -> int:
        if key in self.dictionary:
            location_of_key = 0
            for p in range (len(self.empty_array)):
                if self.empty_array[p] == key :
                    location_of_key = p
                    break
            removed_item = self.empty_array.pop(p)
            self.empty_array.append(removed_item)
            value = self.dictionary[key]
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary[key] = value
            self.empty_array.remove(key)  # Removes the specific key from wherever it is
            self.empty_array.append(key)  # Puts it at the end (most recently used)
        else:
            if len(self.empty_array) < self.capacity :
                self.dictionary[key] = value
                self.empty_array.append(key)
            else:
                removed_item = self.empty_array.pop(0)
                removed_value = self.dictionary.pop(removed_item, None)
                #del self.dictionary[removed_item]
                self.dictionary[key] = value
                self.empty_array.append(key)  








        
