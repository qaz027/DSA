import math

def log_scale(data, base):
    log_list = []
    if not data:
        return None
    for item in data:
        log_list.append(math.log(item, base))

    return log_list