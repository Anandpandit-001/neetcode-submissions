class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending_index = []
        stack = []
        return_list = [0] * len(temperatures)

        for index, value in enumerate(temperatures):
            if len(stack) == 0 or value <= stack[-1]:
                stack.append(value)
                pending_index.append(index)


            if value > stack[-1]:
                while(len(stack) > 0 and value > stack[-1]  ):
                    index_pop = pending_index.pop()
                    return_list[index_pop] = index - index_pop
                    stack.pop()
            

                stack.append(value)
                pending_index.append(index)

        return return_list






