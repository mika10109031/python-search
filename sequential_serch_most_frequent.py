def sequential_serch_most_frequent(data):
    count_dich = {}
    for item in data:
        if item in count_dich:
            count_dich[item] += 1
        else:
            count_dich[item] = 1
    most_freuent = None
    max_count = 0
    for key in count_dich:
        if count_dich[key] > max_count:
            most_freuent = key
            max_count = count_dich[key]
    return most_freuent

my_list = [3, 7, 2, 5, 7, 3, 7, 2, 7]
frequent_element = sequential_serch_most_frequent(my_list)
print(f"Elemen yang sering muncul adalah {frequent_element}")
