class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p = i + 1
            q = len(nums) - 1

            while p < q:

                s = nums[i] + nums[p] + nums[q]

                if s == 0:
                    ans.append([nums[i], nums[p], nums[q]])

                    p += 1
                    q -= 1

                    while p < q and nums[p] == nums[p - 1]:
                        p += 1

                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1

                elif s < 0:
                    p += 1
                else:
                    q -= 1

        return ans