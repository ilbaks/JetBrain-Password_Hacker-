# read test.txt
file = open('test.txt', 'r')

for w in file:
    print(w[0])

file.close()
