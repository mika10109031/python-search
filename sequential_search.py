def sequential_serch(data, key):
    for item in data:
        if item == key:
            return True
        return False
    
my_list = [3, 6, 2, 9, 4, 7]
key = 6
found = sequential_serch(my_list, key)
if found:
        print("Elemen ditemukan.")
else:
        print("Elemen tidak ditemukan.")