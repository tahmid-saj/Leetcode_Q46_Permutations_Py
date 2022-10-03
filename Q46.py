class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = [False for _ in range(len(nums))]
        sol = []
        def permutation(res, data):
            if len(data) == len(nums):
                sol.append(data.copy())
                return
            for i in range(len(nums)):
                if not res[i]:
                    res[i] = True
                    data.append(nums[i])
                    permutation(res, data)
                    res[i] = False
                    data.pop()
        permutation(flag, [])
        return sol
