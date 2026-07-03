class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        p = len(numbers)-1
        

        while(i < p):
            if (numbers[i] + numbers[p]) == target:
                return [i+1 , p+1]
            elif (numbers[i] + numbers[p]) > target:
                p = p - 1
            else :
                i = i + 1

