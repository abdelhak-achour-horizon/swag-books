# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Book(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, book_id: str=None, book_description: str=None, book_title: str=None, book_author: str=None):  # noqa: E501
        """Book - a model defined in Swagger

        :param book_id: The book_id of this Book.  # noqa: E501
        :type book_id: str
        :param book_description: The book_description of this Book.  # noqa: E501
        :type book_description: str
        :param book_title: The book_title of this Book.  # noqa: E501
        :type book_title: str
        :param book_author: The book_author of this Book.  # noqa: E501
        :type book_author: str
        """
        self.swagger_types = {
            'book_id': str,
            'book_description': str,
            'book_title': str,
            'book_author': str
        }

        self.attribute_map = {
            'book_id': 'bookID',
            'book_description': 'bookDescription',
            'book_title': 'bookTitle',
            'book_author': 'bookAuthor'
        }

        self._book_id = book_id
        self._book_description = book_description
        self._book_title = book_title
        self._book_author = book_author

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def book_id(self) -> str:
        """Gets the book_id of this Book.


        :return: The book_id of this Book.
        :rtype: str
        """
        return self._book_id

    @book_id.setter
    def book_id(self, book_id: str):
        """Sets the book_id of this Book.


        :param book_id: The book_id of this Book.
        :type book_id: str
        """
        if book_id is None:
            raise ValueError("Invalid value for `book_id`, must not be `None`")  # noqa: E501

        self._book_id = book_id

    @property
    def book_description(self) -> str:
        """Gets the book_description of this Book.


        :return: The book_description of this Book.
        :rtype: str
        """
        return self._book_description

    @book_description.setter
    def book_description(self, book_description: str):
        """Sets the book_description of this Book.


        :param book_description: The book_description of this Book.
        :type book_description: str
        """

        self._book_description = book_description

    @property
    def book_title(self) -> str:
        """Gets the book_title of this Book.


        :return: The book_title of this Book.
        :rtype: str
        """
        return self._book_title

    @book_title.setter
    def book_title(self, book_title: str):
        """Sets the book_title of this Book.


        :param book_title: The book_title of this Book.
        :type book_title: str
        """
        if book_title is None:
            raise ValueError("Invalid value for `book_title`, must not be `None`")  # noqa: E501

        self._book_title = book_title

    @property
    def book_author(self) -> str:
        """Gets the book_author of this Book.


        :return: The book_author of this Book.
        :rtype: str
        """
        return self._book_author

    @book_author.setter
    def book_author(self, book_author: str):
        """Sets the book_author of this Book.


        :param book_author: The book_author of this Book.
        :type book_author: str
        """
        if book_author is None:
            raise ValueError("Invalid value for `book_author`, must not be `None`")  # noqa: E501

        self._book_author = book_author
