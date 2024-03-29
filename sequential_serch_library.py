def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()

    if title1[0] == title2[0]:
        return True
    
    return False


def sequential_serch(books, book_title):
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']
        
    return "buku tidak ditemukan"

books = [
    {'title': 'python programing', 'shelf': 'A1'},
    {'title': 'Data structures and Algoritms','shelf': 'B2'},
    {'title': 'Introduction to machine learning','shelf':'C3'},
    {'title': 'Database Management systems', 'shelf': 'D4'}
]

book_title = input("Masukan judul buku yang ingin dicari: ")
shelf_location = sequential_serch(books, book_title)
print(shelf_location)