class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)

        low = 1
        high = max_val

        return_val = max_val

        while( low <= high ):

            mid = low + (high - low) // 2

            h_calculated = 0

            for val in piles:
                if (val % mid) == 0:
                    h_calculated = h_calculated + val // mid
                else:
                    h_calculated = h_calculated + val // mid + 1

            if h_calculated <= h:
                if mid <= return_val:
                    return_val = mid

                high = mid - 1

            elif h_calculated > h:
                low = mid + 1

        return return_val
            








