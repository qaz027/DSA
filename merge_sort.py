def merge_sort(nums):
    if len(nums) < 2:
        return nums

    midpt = len(nums)//2
    print(f"nums is {nums}")
    print(f"midpt is {midpt}")
    print(f"calling merge sort on {nums[:midpt]} and {nums[midpt:]}")
    
    return merge(merge_sort(nums[0:midpt]),merge_sort(nums[midpt:]))


def merge(first, second):
    final = []
    i = 0
    j = 0
    print(f"Inputs are as follows: final is {final}, i is {i}, j is {j}")
    print(f"merging {first} and {second} items")
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            print(f"comparing {first[i]} and {second[j]} - appending {first[i]} to final")
            final.append(first[i])
            print(f"appending {first[i]} to final")
            print(f"final is {final}")
            i += 1
        else:
            print(f"adding {second[j]} to final")
            final.append(second[j])
            print(f"final is {final}")
            j += 1

    if i < len(first):
        for i in range(i, len(first)):
            final.append(first[i])

    if j < len(second):
        for j in range(j, len(second)):
            final.append(second[j])

    print(f"final is now {final}")
    return final
