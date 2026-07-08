class MinStack:

    def __init__(self):
        self.stack_object = []

    def push(self, val: int) -> None:
        self.stack_object.append(val)
        

    def pop(self) -> None:
        self.stack_object.pop()

    def top(self) -> int:
        length = len(self.stack_object)
        return  self.stack_object[length - 1]

    def getMin(self) -> int:
        return min(self.stack_object)
