
for costs_iter, reavenue_iter, months_iter in zip(costs, revenues, months):
    print(str(months_iter) + " " + str(reavenue_iter - costs_iter))
