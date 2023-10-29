# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
strings = 50
symbols = 25
symbol_weight = 4
total_Mb = 1.44

total_b = total_Mb * (1024 ** 2)

one_book = pages * strings * symbols
one_book_weight = one_book * symbol_weight
several_books = int(total_b // one_book_weight)

print("Количество книг, помещающихся на дискету:", several_books)
