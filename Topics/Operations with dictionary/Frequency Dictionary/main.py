# put your python code here
list_words = input().lower().split(" ")

dict_statistics = {x: list_words.count(x) for x in list_words}
for key, value in dict_statistics.items():
    print(key + " " + str(value))
