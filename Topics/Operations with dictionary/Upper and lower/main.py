# the list with words from string
# please, do not modify it
some_iterable = input().split()
some_iterable_dictionary = {x.upper(): x.lower() for x in some_iterable}
print(some_iterable_dictionary)

# use dictionary comprehension to create a new dictionary
