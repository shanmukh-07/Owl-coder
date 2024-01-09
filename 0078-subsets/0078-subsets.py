class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ll = []
        for i in range(2**l):
            k = []
            for j in range(l):
                if (i>>j)&1:
                    k.append(nums[j])
            ll.append(k)
        return ll