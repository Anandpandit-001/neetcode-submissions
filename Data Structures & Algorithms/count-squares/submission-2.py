class CountSquares:

    def __init__(self):
        self.dictionary = {}
        

    def add(self, point: List[int]) -> None:
        provided_point = tuple(point)
        self.dictionary[provided_point] = self.dictionary.get(provided_point , 0) + 1
        return None
        

    def count(self, point: List[int]) -> int:
        total = 0

        point_tuple = tuple(point)
        #if abs(qx - nx) == abs(qy - ny) and qx != nx:


        for key in self.dictionary:

            if abs(key[0] -point[0] ) == abs(key[1] - point[1]) and key[0] != point[0]:
                list1 = [point[0] , key[1]]
                tuple1 = tuple(list1)
                if tuple1 in self.dictionary:
                    list2 = [ key[0] , point[1]]
                    tuple2 = tuple(list2)
                    if tuple2 in self.dictionary:
                        total= total + self.dictionary[key] * self.dictionary[tuple1] * self.dictionary[tuple2]

        return total    
        
        
        
