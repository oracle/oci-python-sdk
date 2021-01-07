# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSteeringPolicyAttachmentDetails(object):
    """
    The body for defining an attachment between a steering policy and a domain.


    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSteeringPolicyAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param steering_policy_id:
            The value to assign to the steering_policy_id property of this CreateSteeringPolicyAttachmentDetails.
        :type steering_policy_id: str

        :param zone_id:
            The value to assign to the zone_id property of this CreateSteeringPolicyAttachmentDetails.
        :type zone_id: str

        :param domain_name:
            The value to assign to the domain_name property of this CreateSteeringPolicyAttachmentDetails.
        :type domain_name: str

        :param display_name:
            The value to assign to the display_name property of this CreateSteeringPolicyAttachmentDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'steering_policy_id': 'str',
            'zone_id': 'str',
            'domain_name': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'steering_policy_id': 'steeringPolicyId',
            'zone_id': 'zoneId',
            'domain_name': 'domainName',
            'display_name': 'displayName'
        }

        self._steering_policy_id = None
        self._zone_id = None
        self._domain_name = None
        self._display_name = None

    @property
    def steering_policy_id(self):
        """
        **[Required]** Gets the steering_policy_id of this CreateSteeringPolicyAttachmentDetails.
        The OCID of the attached steering policy.


        :return: The steering_policy_id of this CreateSteeringPolicyAttachmentDetails.
        :rtype: str
        """
        return self._steering_policy_id

    @steering_policy_id.setter
    def steering_policy_id(self, steering_policy_id):
        """
        Sets the steering_policy_id of this CreateSteeringPolicyAttachmentDetails.
        The OCID of the attached steering policy.


        :param steering_policy_id: The steering_policy_id of this CreateSteeringPolicyAttachmentDetails.
        :type: str
        """
        self._steering_policy_id = steering_policy_id

    @property
    def zone_id(self):
        """
        **[Required]** Gets the zone_id of this CreateSteeringPolicyAttachmentDetails.
        The OCID of the attached zone.


        :return: The zone_id of this CreateSteeringPolicyAttachmentDetails.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this CreateSteeringPolicyAttachmentDetails.
        The OCID of the attached zone.


        :param zone_id: The zone_id of this CreateSteeringPolicyAttachmentDetails.
        :type: str
        """
        self._zone_id = zone_id

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this CreateSteeringPolicyAttachmentDetails.
        The attached domain within the attached zone.


        :return: The domain_name of this CreateSteeringPolicyAttachmentDetails.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this CreateSteeringPolicyAttachmentDetails.
        The attached domain within the attached zone.


        :param domain_name: The domain_name of this CreateSteeringPolicyAttachmentDetails.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSteeringPolicyAttachmentDetails.
        A user-friendly name for the steering policy attachment.
        Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :return: The display_name of this CreateSteeringPolicyAttachmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSteeringPolicyAttachmentDetails.
        A user-friendly name for the steering policy attachment.
        Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateSteeringPolicyAttachmentDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
