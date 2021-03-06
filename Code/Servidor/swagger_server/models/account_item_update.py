# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AccountItemUpdate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, name: str=None, bio: str=None):  # noqa: E501
        """AccountItemUpdate - a model defined in Swagger

        :param username: The username of this AccountItemUpdate.  # noqa: E501
        :type username: str
        :param name: The name of this AccountItemUpdate.  # noqa: E501
        :type name: str
        :param bio: The bio of this AccountItemUpdate.  # noqa: E501
        :type bio: str
        """
        self.swagger_types = {
            'username': str,
            'name': str,
            'bio': str
        }

        self.attribute_map = {
            'username': 'username',
            'name': 'name',
            'bio': 'bio'
        }

        self._username = username
        self._name = name
        self._bio = bio

    @classmethod
    def from_dict(cls, dikt) -> 'AccountItemUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountItemUpdate of this AccountItemUpdate.  # noqa: E501
        :rtype: AccountItemUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this AccountItemUpdate.


        :return: The username of this AccountItemUpdate.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this AccountItemUpdate.


        :param username: The username of this AccountItemUpdate.
        :type username: str
        """

        self._username = username

    @property
    def name(self) -> str:
        """Gets the name of this AccountItemUpdate.


        :return: The name of this AccountItemUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AccountItemUpdate.


        :param name: The name of this AccountItemUpdate.
        :type name: str
        """

        self._name = name

    @property
    def bio(self) -> str:
        """Gets the bio of this AccountItemUpdate.


        :return: The bio of this AccountItemUpdate.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio: str):
        """Sets the bio of this AccountItemUpdate.


        :param bio: The bio of this AccountItemUpdate.
        :type bio: str
        """

        self._bio = bio
