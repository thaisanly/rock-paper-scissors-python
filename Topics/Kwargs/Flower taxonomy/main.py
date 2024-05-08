def translate(**kwargs):
    for word in kwargs.items():
        print(word[0], ":", word[1])


words = {"mother": "madre", "father": "padre", "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
