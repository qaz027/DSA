def selection_sort(nums):
    for idx in range(len(nums)):
        smallest_idx = idx
        for idx_plus1 in range(idx+1,len(nums)):
            if nums[smallest_idx] > nums[idx_plus1]:
                smallest_idx = idx_plus1
        # swap numbers
        nums[idx], nums[smallest_idx] = nums[smallest_idx], nums[idx]
    return nums
