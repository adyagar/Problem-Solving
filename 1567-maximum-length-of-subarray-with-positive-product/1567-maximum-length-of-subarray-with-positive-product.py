class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the number of negatives, 
        # the position of the first negative, the position of the last negative, 
        # and the maximum length found so far.
        num_negatives, first_negative, last_negative, max_len = 0, -1, -1, 0

        # The `left` pointer marks the start of the current subarray.
        left = 0

        for right in range(len(nums)):
            # If the current number is negative, we update our tracking variables.
            if nums[right] < 0:
                num_negatives += 1
                if first_negative == -1:
                    first_negative = right
                last_negative = right

            # If we find a zero, we can't use this subarray (product would be zero).
            # We reset all tracking variables and move the `left` pointer past the zero.
            if nums[right] == 0:
                num_negatives, first_negative, last_negative = 0, -1, -1
                left = right + 1
            else:
                # If the current subarray has an even number of negatives, the product is positive.
                if num_negatives % 2 == 0:
                    max_len = max(max_len, right - left + 1)
                else:
                    # If there's an odd number of negatives, the product is negative.
                    # To get the longest subarray with a positive product, we have two choices:
                    # 1. Exclude the first negative number.
                    # 2. Exclude the last negative number.
                    # We calculate the lengths for both options and update `max_len` accordingly.
                    max_len = max(max_len, right - first_negative, last_negative - left)

        return max_len
