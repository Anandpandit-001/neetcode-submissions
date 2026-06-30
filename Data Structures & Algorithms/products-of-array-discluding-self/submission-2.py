class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mul = 1
        zero_count = 0
        return_list = []

        for num in nums:
            if num == 0 :
                zero_count = zero_count + 1
            else:
                mul = mul * num

        if (zero_count == 1):
            for val in nums:
                if val == 0:
                    return_list.append(int(mul))
                else:
                    return_list.append(int(0))
            return return_list

        elif(zero_count >= 2):
            for val in nums:
                return_list.append(int(0))

            return return_list

        else:
            for val in nums:
                
                return_list.append(int(mul / val))

            return return_list







