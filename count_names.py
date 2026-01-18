def count_names(list_of_lists, target_name):
    count = 0
    for list in list_of_lists:
        for items in list:
            if items == target_name:
                count += 1

    return count

# Big O notation of NM