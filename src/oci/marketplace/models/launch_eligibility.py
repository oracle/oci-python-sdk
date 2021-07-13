# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchEligibility(object):
    """
    Tenant eligibility and other information for launching a PIC image
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchEligibility object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_id:
            The value to assign to the image_id property of this LaunchEligibility.
        :type image_id: str

        :param is_launch_allowed:
            The value to assign to the is_launch_allowed property of this LaunchEligibility.
        :type is_launch_allowed: bool

        :param meters:
            The value to assign to the meters property of this LaunchEligibility.
        :type meters: str

        """
        self.swagger_types = {
            'image_id': 'str',
            'is_launch_allowed': 'bool',
            'meters': 'str'
        }

        self.attribute_map = {
            'image_id': 'imageId',
            'is_launch_allowed': 'isLaunchAllowed',
            'meters': 'meters'
        }

        self._image_id = None
        self._is_launch_allowed = None
        self._meters = None

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this LaunchEligibility.
        PIC Image ID


        :return: The image_id of this LaunchEligibility.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this LaunchEligibility.
        PIC Image ID


        :param image_id: The image_id of this LaunchEligibility.
        :type: str
        """
        self._image_id = image_id

    @property
    def is_launch_allowed(self):
        """
        **[Required]** Gets the is_launch_allowed of this LaunchEligibility.
        Is the tenant permitted to launch the PIC image


        :return: The is_launch_allowed of this LaunchEligibility.
        :rtype: bool
        """
        return self._is_launch_allowed

    @is_launch_allowed.setter
    def is_launch_allowed(self, is_launch_allowed):
        """
        Sets the is_launch_allowed of this LaunchEligibility.
        Is the tenant permitted to launch the PIC image


        :param is_launch_allowed: The is_launch_allowed of this LaunchEligibility.
        :type: bool
        """
        self._is_launch_allowed = is_launch_allowed

    @property
    def meters(self):
        """
        Gets the meters of this LaunchEligibility.
        related meters for the PIC image


        :return: The meters of this LaunchEligibility.
        :rtype: str
        """
        return self._meters

    @meters.setter
    def meters(self, meters):
        """
        Sets the meters of this LaunchEligibility.
        related meters for the PIC image


        :param meters: The meters of this LaunchEligibility.
        :type: str
        """
        self._meters = meters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
