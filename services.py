import datetime
from model import Book

class BookServices:
    def add_new_book(self):
        new_book= Book()
        new_book['bookId']=self['bookId']
        new_book['bookName']=self['bookName']
        new_book['authorName']=self['authorName']
        new_book['genre']=self['genre']
        book_exists= Book._get_collection().find_one({'bookId': new_book['bookId']})
        if not book_exists:
            Book._get_collection().insert_one(new_book.to_dict())
            return True
        else:
            return False
        
    def borrow_book(self):
        book_available= Book._get_collection().find_one({'bookName': self['bookName'],"available": True})
        print(book_available)
        if book_available:
            Book._get_collection().update_one(
                {'bookId': book_available['bookId']},
                {"$set": {"available": False,"borrowDate":datetime.datetime.now(tz=datetime.timezone.utc)}}
            ) 
            return True
        else:
            return False
    
    def return_book(self):
        book_available= Book._get_collection().find_one({'bookId': self['bookId'],"available": False})
        print(book_available)
        if book_available:
            Book._get_collection().update_one(
                {'bookId': book_available['bookId']},
                {"$set": {"available": True,"returnDate":datetime.datetime.now(tz=datetime.timezone.utc)}}
            )
            return("Book returned successfully")
        else:
            return("Book cannot be returned")
        
    def display_book(self):
        book_available= Book._get_collection().aggregate([
                        {
                            '$match': {
                                'bookId': self["bookId"]
                            }
                        }, {
                            '$project': {
                                '_id': 0
                            }
                        }
                    ])
        
        if book_available:
            return(list(book_available))
        else:
            return("Book not found")
        
    def display_all_book(self):
        book_available= Book._get_collection().aggregate([
                        {
                            '$project': {
                                '_id': 0
                            }
                        }
                    ])
        
        if book_available:
            return(list(book_available))
        else:
            return("Book not found")
    
    def delete_book(self):
        book_available= Book._get_collection().find_one({'bookId': self['bookId']})
        if book_available:
            Book._get_collection().delete_one(
                {'bookId': book_available['bookId']}
            )
            return("Book deleted")
        else:
            return("Book not found")
    

