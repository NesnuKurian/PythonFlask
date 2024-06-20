from mongoengine import *

class Book(Document):
    bookId=IntField(required= True)
    bookName=StringField(required= True)
    authorName=StringField(required= False)
    genre=StringField(default= None)
    borrowDate=DateField()
    returnDate= DateField()
    available= BooleanField(default=True)
    
    def to_dict(self):
        return {
            'bookId': self.bookId,
            'bookName': self.bookName,
            'authorName': self.authorName,
            'genre': self.genre,
            'borrowDate': self.borrowDate,
            'returnDate': self.returnDate,
            'available': self.available,
            
        }
    



