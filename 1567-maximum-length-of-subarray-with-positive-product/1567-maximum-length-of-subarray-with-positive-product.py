class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive, negative, ans = 0,0,0

        for num in nums:
            if num == 0:
                positive, negative = 0,0
            elif num > 0:
                positive +=1
                # negative zero means we have not seen negative yet - it means later on if we get another negative no then it wont
                # be maximum so no need to track length. but if we have seen negative now(negative is not 0) then we need to keep track of negative
                #  because later on if it we see another negative, there is chance it can be positive and max product
                negative = 0 if negative == 0 else negative + 1
            else:
                positive, negative = 0 if negative == 0 else negative + 1, positive + 1

            # max of positive because with all +ve -ve nums and its products, what was max length we ended up in 
            # pos value..even after even no of -ve values..we swapped and ended up in positive value..that max is capture
            # in pos value
            ans = max(ans, positive)

        return ans