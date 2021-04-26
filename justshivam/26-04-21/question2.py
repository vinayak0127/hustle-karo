class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, l = [], len(nums)
        for i in range(l):
            j = i + 1
            k = l - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                if k < l - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return res
