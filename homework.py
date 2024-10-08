Little Library

Goal: Design a system that will accept book donations and rent them out free to customers.

The first endpoint should store a record of the book donated. 
The donator can only donate one book title at a time. 
However they can donate multiple of the same title. 
If you receive a duplicate book the number of book for that book title should increase 
by the number of book received. The input to this endpoint will be:

{
   “book_title”: “…”,
   “number_of_books”: 2
}

The second endpoint will allow the customer to rent the book title if the book is in the library. 
Make sure to keep a record of how many books you have of a title 
and how many of the title you have loan out. The input will be:

 {
   “book_title”: “…”
 }

The third endpoint will take in a book title and return to the user how many copies you have 
and how many copies have been lent out. 

@app.get(“/info/{bookTitle})
async def book_info(bookTitle: string):

Return
---------------------------------
book_record = {} # {'how_many_library_own':int, 'current_stock':int}

class Book:
  def __init__(self):
    self.how_many_library_own = 0
    self.current_stock = 0

@app.post("/donate_book")
async def donate_book(input):
  book = Book()
  if input.book_title not in book_record:
    book.how_many_library_own += input.number_of_books
    book.current_stock += input.number_of_books
    book_record[input.book_title] = book
  else:
    temp = book_record[input.book_title]
    temp.how_many_library_own += input.number_of_books
    temp.current_stock += input.number_of_books
    book_record[input.book_title] = temp

@app.post("/rent_book")
async def rent_book(input):
  
  if input.book_title in book_record:
    temp = book_record[input.book_title]
    
    if temp.current_stock == 0:
      print('cannot rent this book at the moment')
    else:
      temp.current_stock -= 1
      book_record[input.book_title] = temp
  else:
    print('that book does not exist')