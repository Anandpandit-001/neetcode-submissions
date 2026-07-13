class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        all_dictionary_key = self.dictionary[key]
        if timestamp in  all_dictionary_key:
            value = all_dictionary_key[timestamp]
            return value
        else:
            values = list(all_dictionary_key.values())
            keys = list(all_dictionary_key.keys())
            sorted_keys = sorted(keys)
            left = 0
            right = len(keys) -1
            mid = left + (right - left) // 2

            while(left <= right ):

                mid = left + (right - left) // 2

                if sorted_keys[mid] > timestamp:
                    right = mid - 1
                else:
                    left = mid + 1

            if right >= 0: 
                floor_value = sorted_keys[right]
                return all_dictionary_key[floor_value]
            else:
                return ""
            

            







        
