def num_possible_orders(num_posts):
    factoral = 1
    for num in range(num_posts):
        factoral = factoral * (num+1)

    return factoral