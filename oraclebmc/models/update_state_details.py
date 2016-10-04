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


class UpdateStateDetails(object):

    def __init__(self):

        self.swagger_types = {
            'blocked': 'bool'
        }

        self.attribute_map = {
            'blocked': 'blocked'
        }

        self._blocked = None


    @property
    def blocked(self):
        """
        Gets the blocked of this UpdateStateDetails.
        Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).\n

        :return: The blocked of this UpdateStateDetails.
        :rtype: bool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """
        Sets the blocked of this UpdateStateDetails.
        Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).\n

        :param blocked: The blocked of this UpdateStateDetails.
        :type: bool
        """
        self._blocked = blocked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

