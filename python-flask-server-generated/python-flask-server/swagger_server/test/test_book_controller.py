# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_book_request import CreateBookRequest  # noqa: E501
from swagger_server.models.create_book_response import CreateBookResponse  # noqa: E501
from swagger_server.models.delete_book_response import DeleteBookResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_book_by_id_response import GetBookByIdResponse  # noqa: E501
from swagger_server.models.list_books_response import ListBooksResponse  # noqa: E501
from swagger_server.models.update_book_request import UpdateBookRequest  # noqa: E501
from swagger_server.models.update_book_response import UpdateBookResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        
        """
        book = CreateBookRequest()
        response = self.client.open(
            '/v1/book',
            method='POST',
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book(self):
        """Test case for delete_book

        
        """
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        
        """
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_books(self):
        """Test case for list_books

        
        """
        response = self.client.open(
            '/v1/book',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book(self):
        """Test case for update_book

        
        """
        book = UpdateBookRequest()
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='PUT',
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
