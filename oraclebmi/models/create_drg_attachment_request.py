# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
The original license is below.

    Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems

class CreateDrgAttachmentRequest(object):

    def __init__(self):
        """
        CreateDrgAttachmentRequest - a model defined in Swagger
        """
        self.swagger_types = {
            'display_name': 'str',
            'drg_id': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'vcn_id': 'vcnId'
        }

        self._display_name = None
        self._drg_id = None
        self._vcn_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrgAttachmentRequest.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this CreateDrgAttachmentRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrgAttachmentRequest.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this CreateDrgAttachmentRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        Gets the drg_id of this CreateDrgAttachmentRequest.
        The OCID of the DRG.

        :return: The drg_id of this CreateDrgAttachmentRequest.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateDrgAttachmentRequest.
        The OCID of the DRG.

        :param drg_id: The drg_id of this CreateDrgAttachmentRequest.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateDrgAttachmentRequest.
        The OCID of the VCN.

        :return: The vcn_id of this CreateDrgAttachmentRequest.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDrgAttachmentRequest.
        The OCID of the VCN.

        :param vcn_id: The vcn_id of this CreateDrgAttachmentRequest.
        :type: str
        """
        self._vcn_id = vcn_id

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
        Returns true if objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

