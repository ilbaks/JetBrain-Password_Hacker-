def translate(**kwargs):
    for word in kwargs:
        word1 = word
        word2 = kwargs[word]
        print(word1, ":", word2)

words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
