input_string = input()
list_of_bytes = []
list_of_bytes = bytes(input_string, encoding='utf-8')
print(list_of_bytes[-1])
