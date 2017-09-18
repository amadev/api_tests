# coding: utf-8

"""
    Placement API

    This is a sample server Placement API server.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ResourceProvider(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, uuid=None, generation=None, name=None, links=None):
        """
        ResourceProvider - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'uuid': 'str',
            'generation': 'int',
            'name': 'str',
            'links': 'list[Link]'
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'generation': 'generation',
            'name': 'name',
            'links': 'links'
        }

        self._uuid = uuid
        self._generation = generation
        self._name = name
        self._links = links


    @property
    def uuid(self):
        """
        Gets the uuid of this ResourceProvider.


        :return: The uuid of this ResourceProvider.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ResourceProvider.


        :param uuid: The uuid of this ResourceProvider.
        :type: str
        """

        self._uuid = uuid

    @property
    def generation(self):
        """
        Gets the generation of this ResourceProvider.


        :return: The generation of this ResourceProvider.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this ResourceProvider.


        :param generation: The generation of this ResourceProvider.
        :type: int
        """

        self._generation = generation

    @property
    def name(self):
        """
        Gets the name of this ResourceProvider.


        :return: The name of this ResourceProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceProvider.


        :param name: The name of this ResourceProvider.
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """
        Gets the links of this ResourceProvider.


        :return: The links of this ResourceProvider.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ResourceProvider.


        :param links: The links of this ResourceProvider.
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other