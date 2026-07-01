class Solution:
    
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(n.bit_length()):
            # Shift the number right by i positions and isolate the last bit using AND 1
            bit = (n >> i) & 1
            if bit == 1:
                count = count + 1
        return count