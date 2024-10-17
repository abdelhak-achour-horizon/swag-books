import connexion
import six
from swagger_server.models.create_book_request import CreateBookRequest  # noqa: E501
from swagger_server.models.create_book_response import CreateBookResponse  # noqa: E501
from swagger_server.models.delete_book_response import DeleteBookResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_book_by_id_response import GetBookByIdResponse  # noqa: E501
from swagger_server.models.list_books_response import ListBooksResponse  # noqa: E501
from swagger_server.models.update_book_request import UpdateBookRequest  # noqa: E501
from swagger_server.models.update_book_response import UpdateBookResponse  # noqa: E501
from swagger_server import util

# In-memory storage for books
books = {}

def create_book(book):  # noqa: E501
    """create_book

     # noqa: E501

    :param book: 
    :type book: dict | bytes

    :rtype: CreateBookResponse
    """
    if connexion.request.is_json:
        book_data = CreateBookRequest.from_dict(connexion.request.get_json())  # noqa: E501

        if book_data.book_id in books:
            response = CreateBookResponse(status="error", message="Another book with the same ID exists.")
            return response, 403

        # Store the book
        books[book_data.book_id] = book_data
        response = CreateBookResponse(status="success", message="Book created successfully.")
        return response, 200

def delete_book(book_id):  # noqa: E501
    """delete_book

     # noqa: E501

    :param bookID: 
    :type bookID: str

    :rtype: DeleteBookResponse
    """
    if book_id in books:
        del books[book_id]
        response = DeleteBookResponse(status="success", message="Book deleted successfully.")
        return response, 200
    else:
        return ErrorResponse(status="error", message="Book not found."), 404

def get_book_by_id(book_id):  # noqa: E501
    """get_book_by_id

     # noqa: E501

    :param bookID: 
    :type bookID: str

    :rtype: GetBookByIdResponse
    """
    if book_id in books:
        book = books[book_id]
        response = GetBookByIdResponse(status="success", message="Book retrieved successfully.", book=book)
        return response, 200
    else:
        return ErrorResponse(status="error", message="Book not found."), 404

def list_books():  # noqa: E501
    """list_books

     # noqa: E501

    :rtype: ListBooksResponse
    """
    return list(books.values()), 200

def update_book(book_id, book):  # noqa: E501
    """update_book

     # noqa: E501

    :param bookID: 
    :type bookID: str
    :param book: 
    :type book: dict | bytes

    :rtype: UpdateBookResponse
    """
    if connexion.request.is_json:
        book_data = UpdateBookRequest.from_dict(connexion.request.get_json())  # noqa: E501

        if book_id not in books:
            return ErrorResponse(status="error", message="Book not found."), 404

        # Update the book
        existing_book = books[book_id]
        existing_book.book_title = book_data.book_title
        existing_book.book_author = book_data.book_author
        existing_book.book_description = book_data.book_description

        response = UpdateBookResponse(status="success", message="Book updated successfully.")
        return response, 200

