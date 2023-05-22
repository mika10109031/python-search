def sequential_search(phonebook, name):
    for entry in phonebook:
        if entry[0] == name:
            return entry[1]
    return "Nomor telepon tidak ditemukan"

phonebook = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

name_to_search = "Jane Smith"
phone_number = sequential_search(phonebook, name_to_search)

print(f"Nomor telepon {name_to_search}: {phone_number}")