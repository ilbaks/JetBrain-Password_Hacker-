# the list "meals" is already defined
# your code here
sum_kcal = 0
for x in meals:
    sum_kcal += x.get('kcal', 0)
print(sum_kcal)
