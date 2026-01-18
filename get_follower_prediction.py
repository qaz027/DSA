def get_follower_prediction(follower_count, influencer_type, num_months):
    r = 2
    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3

    return follower_count * r ** num_months
