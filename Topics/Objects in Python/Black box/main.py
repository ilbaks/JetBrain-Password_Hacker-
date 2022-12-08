# use the function blackbox(lst) that is already defined
my_lst = [1, 12, 3]
returned_lst = blackbox(my_lst)
print("same" if id(my_lst) == id(returned_lst) else "new")
