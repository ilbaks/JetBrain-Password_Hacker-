# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
count = 0
for x,y in test_dict.items():
    if count == 0:
        count +=1
        max_key = x
        min_key = x
        max_val = y
        min_val = y

    if y > max_val:
        max_val = y
        max_key = x
    if y < min_val:
        min_val = y
        min_key = x


print("min: " + str(min_key))
print("max: " + str(max_key))


