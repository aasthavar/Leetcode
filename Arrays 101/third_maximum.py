class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        first_maxm = None
        second_maxm = None
        third_maxm = None
        for e in nums:
            if e == first_maxm or e == second_maxm or e == third_maxm:
                continue
            if first_maxm == None or e > first_maxm:
                third_maxm = second_maxm
                second_maxm = first_maxm
                first_maxm = e
            elif second_maxm == None or e > second_maxm:
                third_maxm = second_maxm
                second_maxm = e
            elif third_maxm == None or e > third_maxm:
                third_maxm = e
                
        if third_maxm == None:
            return first_maxm
        return third_maxm