def average_followers(nums):
    if not nums:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)
