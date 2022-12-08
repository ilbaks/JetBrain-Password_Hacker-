import itertools

for first, second, third in itertools.product(main_courses, desserts, drinks):
    sum_ = (price_main_courses[main_courses.index(first)] + price_desserts[desserts.index(second)]
            + price_drinks[drinks.index(third)])
    if sum_ <= 30:
        print(first + " " + second + " " + third + " " + str(sum_))
