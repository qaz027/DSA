def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1,end):
            #print(f"i is {i}")
            if nums[i-1] > nums[i]:
                #print(f"checking {nums[i-1]} and {nums[i]}")
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                swapping = True
                #print(f"updated nums list is {nums}")

        end = end - 1

    return nums
            

"""
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums
"""