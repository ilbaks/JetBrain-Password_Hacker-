input_string = input()
result_list = []
for x in input_string:
    result_list.append(chr(ord(x) + 1))

print("".join(result_list))
