class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        # Base case: anything to the power of 0 is 1
        if n == 0:
            return 1.0
        
        # If the power is negative, invert x and make n positive
        if n < 0:
            x = 1 / x
            n = -n
            
        # Divide and conquer: calculate the power of n//2
        half = self.myPow(x, n // 2)
        
        # If n is even, square the result
        if n % 2 == 0:
            return half * half
        # If n is odd, square the result and multiply by x once more
        else:
            return half * half * x
