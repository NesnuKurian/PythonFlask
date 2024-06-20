from flask import Blueprint
from flask_restful import request
from services import BookServices

api= Blueprint("pages",__name__)

class Controller:
    @api.route('/library/add_book',methods=['POST'])
    def add_book():
        payload= request.json
        result= BookServices.add_new_book(payload)
        if result is False:
            return('Book not added')
        else:
            return('Book added successfully ')
        
    @api.route('/library/borrow_book',methods=['PUT'])
    def borrow_book():
        payload= request.json
        result= BookServices.borrow_book(payload)
        if result is False:
            return('Book not available')
        else:
            return('Book lent successfully ')
    
    @api.route('/library/return_book',methods=['PUT'])
    def return_book():
        payload= request.json
        result= BookServices.return_book(payload)
        return(result)

    @api.route('/library/display_book',methods=['GET'])
    def display_book():
        payload= request.json
        if payload['bookId']!= None:
            result= BookServices.display_book(payload)
        else:
            result= BookServices.display_all_book(payload)
        return(result)
    
    @api.route('/library/delete_book',methods=['DELETE'])
    def delete_book():
        payload= request.json
        result= BookServices.delete_book(payload)
        return(result)