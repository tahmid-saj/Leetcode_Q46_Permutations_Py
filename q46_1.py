class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def helper(index, currentPermutation):
            if len(nums) == index: self.result.append(currentPermutation)
            else:
                for i in range(0, len(currentPermutation) + 1):
                    newPermutation = list(currentPermutation)
                    newPermutation.insert(i, nums[index])
                    helper(index + 1, newPermutation)
        
        helper(0, [])
        return self.result
