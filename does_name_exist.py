def does_name_exist(first_names, last_names, full_name):
    for fname in first_names:
        for lname in last_names:
            comparison = f"{fname} {lname}"
            if full_name == comparison:
                return True

    return False
