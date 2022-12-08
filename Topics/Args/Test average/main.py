def average_mark(*arg):
    average = 0
    count = 0
    for x in arg:
        average += x
        count = count + 1
    return round(average / count, 1)
