class Solution:
    def removeDuplicates(self, nums):
        # If the array has 2 or fewer elements, return its length
        if len(nums) <= 2:
            return len(nums)

        # Pointer where the next valid element will be placed
        k = 2

        # Start checking from the 3rd element
        for i in range(2, len(nums)):
            # Keep the current element only if it is different
            # from the element two positions before k
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k     