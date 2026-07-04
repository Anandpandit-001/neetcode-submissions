class Solution:
    def trap(self, height: List[int]) -> int:

        left_max_array = [0]*(len(height))
        right_max_array = [0]*(len(height))

        i = 0
        max_val = 0

        

        for val in height:
            if val > max_val:
                left_max_array[i] = val
                max_val = val
            else:
                left_max_array[i] = max_val
            
            i = i + 1

        i = 0
        max_val = 0
        reversed_arr = height[::-1]

        for val in reversed_arr:
            if val > max_val:
                right_max_array[i] = val
                max_val = val
            else:
                right_max_array[i] = max_val
            
            i = i + 1
        
        right_max_array = right_max_array[::-1]

        sum = 0

        for i in range(len(height)):

            sum = sum + min(left_max_array[i] , right_max_array[i]) - height[i]

        return sum 
            

