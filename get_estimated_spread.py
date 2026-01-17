def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0:
        return 0
    sum = 0
    mean = 0
    for follower in audiences_followers:
        sum += follower
    mean = sum / num_followers

    return mean * (num_followers ** 1.2)
