# TODO Найдите количество книг, которое можно разместить на дискете
bytesInBook = 4 * 25 * 50 * 100
bytesInDisk = 1.44 * 1024 * 1024
books = int(bytesInDisk / bytesInBook)
print("Количество книг, помещающихся на дискету:", books)
