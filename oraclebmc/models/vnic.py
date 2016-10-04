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


class Vnic(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'private_ip': 'str',
            'public_ip': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'private_ip': 'privateIp',
            'public_ip': 'publicIp',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._private_ip = None
        self._public_ip = None
        self._subnet_id = None
        self._time_created = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        :return: The availability_domain of this Vnic.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        :param availability_domain: The availability_domain of this Vnic.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.

        :return: The compartment_id of this Vnic.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.

        :param compartment_id: The compartment_id of this Vnic.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this Vnic.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this Vnic.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Vnic.
        The VNIC's Oracle ID (OCID).

        :return: The id of this Vnic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vnic.
        The VNIC's Oracle ID (OCID).

        :param id: The id of this Vnic.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Vnic.
        The current state of the VNIC

        :return: The lifecycle_state of this Vnic.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Vnic.
        The current state of the VNIC

        :param lifecycle_state: The lifecycle_state of this Vnic.
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
    def private_ip(self):
        """
        Gets the private_ip of this Vnic.
        The private IP addresses of the VNIC, which is within the VNIC subnet\nand is accessible within the VCN.\n

        :return: The private_ip of this Vnic.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this Vnic.
        The private IP addresses of the VNIC, which is within the VNIC subnet\nand is accessible within the VCN.\n

        :param private_ip: The private_ip of this Vnic.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """
        Gets the public_ip of this Vnic.
        The public IP address of the VNIC, which Oracle performs NAT for at the gateway.\n

        :return: The public_ip of this Vnic.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """
        Sets the public_ip of this Vnic.
        The public IP address of the VNIC, which Oracle performs NAT for at the gateway.\n

        :param public_ip: The public_ip of this Vnic.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.

        :return: The subnet_id of this Vnic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.

        :param subnet_id: The subnet_id of this Vnic.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Vnic.
        The date and time the VNIC was created.

        :return: The time_created of this Vnic.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vnic.
        The date and time the VNIC was created.

        :param time_created: The time_created of this Vnic.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

