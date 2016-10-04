# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen


from ..util import formatted_flat_dict


class Error(object):

    def __init__(self):

        self.swagger_types = {
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = None
        self._message = None


    @property
    def code(self):
        """
        Gets the code of this Error.
        A short error code that defines the error, meant for programmatic parsing.

        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.
        A short error code that defines the error, meant for programmatic parsing.

        :param code: The code of this Error.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        Gets the message of this Error.
        A human-readable error string.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.
        A human-readable error string.

        :param message: The message of this Error.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

