class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for n in nums:
            dict[n] = dict.get(n, 0) + 1
            if dict.get(n,0) > 1:
                return True
        else:
            return False

        