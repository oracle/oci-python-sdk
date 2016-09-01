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

from pprint import pformat
from six import iteritems

class SecurityList(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'id': 'str',
            'ingress_security_rules': 'list[IngressSecurityRule]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'id': 'id',
            'ingress_security_rules': 'ingressSecurityRules',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._egress_security_rules = None
        self._id = None
        self._ingress_security_rules = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.

        :return: The compartment_id of this SecurityList.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.

        :param compartment_id: The compartment_id of this SecurityList.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's not changeable.

        :return: The display_name of this SecurityList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's not changeable.

        :param display_name: The display_name of this SecurityList.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        Gets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.

        :return: The egress_security_rules of this SecurityList.
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.

        :param egress_security_rules: The egress_security_rules of this SecurityList.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def id(self):
        """
        Gets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).

        :return: The id of this SecurityList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).

        :param id: The id of this SecurityList.
        :type: str
        """
        self._id = id

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.

        :return: The ingress_security_rules of this SecurityList.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.

        :param ingress_security_rules: The ingress_security_rules of this SecurityList.
        :type: list[IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityList.
        The security list's current state.

        :return: The lifecycle_state of this SecurityList.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityList.
        The security list's current state.

        :param lifecycle_state: The lifecycle_state of this SecurityList.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityList.
        The date and time the security list was created.

        :return: The time_created of this SecurityList.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityList.
        The date and time the security list was created.

        :param time_created: The time_created of this SecurityList.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.

        :return: The vcn_id of this SecurityList.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.

        :param vcn_id: The vcn_id of this SecurityList.
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
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

