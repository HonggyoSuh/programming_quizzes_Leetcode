def removeElement(self, nums, val):
    # i = 0

    # for x in nums:
    #     if x != val:
    #         nums[i] = x
    #         i += 1

    # return i

    # slow = 0
    # for fast in range(len(nums)):
    #     if nums[fast] != val:
    #         nums[slow], nums[fast] = nums[fast], nums[slow]
    #         slow += 1

    # return slow

    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)
