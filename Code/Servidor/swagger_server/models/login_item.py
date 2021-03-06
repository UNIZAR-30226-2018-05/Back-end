# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LoginItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mail: str=None, _pass: str=None):  # noqa: E501
        """LoginItem - a model defined in Swagger

        :param mail: The mail of this LoginItem.  # noqa: E501
        :type mail: str
        :param _pass: The _pass of this LoginItem.  # noqa: E501
        :type _pass: str
        """
        self.swagger_types = {
            'mail': str,
            '_pass': str
        }

        self.attribute_map = {
            'mail': 'mail',
            '_pass': 'pass'
        }

        self._mail = mail
        self.__pass = _pass

    @classmethod
    def from_dict(cls, dikt) -> 'LoginItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LoginItem of this LoginItem.  # noqa: E501
        :rtype: LoginItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mail(self) -> str:
        """Gets the mail of this LoginItem.


        :return: The mail of this LoginItem.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this LoginItem.


        :param mail: The mail of this LoginItem.
        :type mail: str
        """
        if mail is None:
            raise ValueError("Invalid value for `mail`, must not be `None`")  # noqa: E501

        self._mail = mail

    @property
    def _pass(self) -> str:
        """Gets the _pass of this LoginItem.


        :return: The _pass of this LoginItem.
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass: str):
        """Sets the _pass of this LoginItem.


        :param _pass: The _pass of this LoginItem.
        :type _pass: str
        """
        if _pass is None:
            raise ValueError("Invalid value for `_pass`, must not be `None`")  # noqa: E501

        self.__pass = _pass
