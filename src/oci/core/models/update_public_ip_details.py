# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePublicIpDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePublicIpDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdatePublicIpDetails.
        :type display_name: str

        :param private_ip_id:
            The value to assign to the private_ip_id property of this UpdatePublicIpDetails.
        :type private_ip_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'private_ip_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'private_ip_id': 'privateIpId'
        }

        self._display_name = None
        self._private_ip_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePublicIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this UpdatePublicIpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePublicIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this UpdatePublicIpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def private_ip_id(self):
        """
        Gets the private_ip_id of this UpdatePublicIpDetails.
        The OCID of the private IP to assign the public IP to.
        * If the public IP is already assigned to a different private IP, it will be unassigned
        and then reassigned to the specified private IP.
        * If you set this field to an empty string, the public IP will be unassigned from the
        private IP it is currently assigned to.


        :return: The private_ip_id of this UpdatePublicIpDetails.
        :rtype: str
        """
        return self._private_ip_id

    @private_ip_id.setter
    def private_ip_id(self, private_ip_id):
        """
        Sets the private_ip_id of this UpdatePublicIpDetails.
        The OCID of the private IP to assign the public IP to.
        * If the public IP is already assigned to a different private IP, it will be unassigned
        and then reassigned to the specified private IP.
        * If you set this field to an empty string, the public IP will be unassigned from the
        private IP it is currently assigned to.


        :param private_ip_id: The private_ip_id of this UpdatePublicIpDetails.
        :type: str
        """
        self._private_ip_id = private_ip_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
