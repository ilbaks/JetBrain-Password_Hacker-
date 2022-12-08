#  write your code here 
input_file = open('.\\data\\dataset\input.txt')
list_strings = input_file.readlines()
input_file.close()
total_count = 0
for line in list_strings:
    total_count += line.count("summer ") + line.count("summer\n")
print(total_count)
