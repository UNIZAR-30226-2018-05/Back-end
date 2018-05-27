# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.song_item import SongItem  # noqa: F401,E501
from swagger_server import util


class AlbumItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, author_id: str=None, author_name: str=None, publish_date: date=None, description: str=None, songs: List[SongItem]=None):  # noqa: E501
        """AlbumItem - a model defined in Swagger

        :param id: The id of this AlbumItem.  # noqa: E501
        :type id: str
        :param name: The name of this AlbumItem.  # noqa: E501
        :type name: str
        :param author_id: The author_id of this AlbumItem.  # noqa: E501
        :type author_id: str
        :param author_name: The author_name of this AlbumItem.  # noqa: E501
        :type author_name: str
        :param publish_date: The publish_date of this AlbumItem.  # noqa: E501
        :type publish_date: date
        :param description: The description of this AlbumItem.  # noqa: E501
        :type description: str
        :param songs: The songs of this AlbumItem.  # noqa: E501
        :type songs: List[SongItem]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'author_id': str,
            'author_name': str,
            'publish_date': date,
            'description': str,
            'songs': List[SongItem]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'author_id': 'authorID',
            'author_name': 'authorName',
            'publish_date': 'publishDate',
            'description': 'description',
            'songs': 'songs'
        }

        self._id = id
        self._name = name
        self._author_id = author_id
        self._author_name = author_name
        self._publish_date = publish_date
        self._description = description
        self._songs = songs

    @classmethod
    def from_dict(cls, dikt) -> 'AlbumItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlbumItem of this AlbumItem.  # noqa: E501
        :rtype: AlbumItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this AlbumItem.


        :return: The id of this AlbumItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AlbumItem.


        :param id: The id of this AlbumItem.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this AlbumItem.


        :return: The name of this AlbumItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AlbumItem.


        :param name: The name of this AlbumItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def author_id(self) -> str:
        """Gets the author_id of this AlbumItem.


        :return: The author_id of this AlbumItem.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id: str):
        """Sets the author_id of this AlbumItem.


        :param author_id: The author_id of this AlbumItem.
        :type author_id: str
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def author_name(self) -> str:
        """Gets the author_name of this AlbumItem.


        :return: The author_name of this AlbumItem.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name: str):
        """Sets the author_name of this AlbumItem.


        :param author_name: The author_name of this AlbumItem.
        :type author_name: str
        """
        if author_name is None:
            raise ValueError("Invalid value for `author_name`, must not be `None`")  # noqa: E501

        self._author_name = author_name

    @property
    def publish_date(self) -> date:
        """Gets the publish_date of this AlbumItem.


        :return: The publish_date of this AlbumItem.
        :rtype: date
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date: date):
        """Sets the publish_date of this AlbumItem.


        :param publish_date: The publish_date of this AlbumItem.
        :type publish_date: date
        """

        self._publish_date = publish_date

    @property
    def description(self) -> str:
        """Gets the description of this AlbumItem.


        :return: The description of this AlbumItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this AlbumItem.


        :param description: The description of this AlbumItem.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def songs(self) -> List[SongItem]:
        """Gets the songs of this AlbumItem.


        :return: The songs of this AlbumItem.
        :rtype: List[SongItem]
        """
        return self._songs

    @songs.setter
    def songs(self, songs: List[SongItem]):
        """Sets the songs of this AlbumItem.


        :param songs: The songs of this AlbumItem.
        :type songs: List[SongItem]
        """
        if songs is None:
            raise ValueError("Invalid value for `songs`, must not be `None`")  # noqa: E501

        self._songs = songs
