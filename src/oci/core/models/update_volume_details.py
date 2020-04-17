# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVolumeDetails(object):
    """
    UpdateVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVolumeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVolumeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateVolumeDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVolumeDetails.
        :type freeform_tags: dict(str, str)

        :param vpus_per_gb:
            The value to assign to the vpus_per_gb property of this UpdateVolumeDetails.
        :type vpus_per_gb: int

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this UpdateVolumeDetails.
        :type size_in_gbs: int

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'vpus_per_gb': 'int',
            'size_in_gbs': 'int'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'vpus_per_gb': 'vpusPerGB',
            'size_in_gbs': 'sizeInGBs'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._vpus_per_gb = None
        self._size_in_gbs = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVolumeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVolumeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVolumeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVolumeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVolumeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVolumeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def vpus_per_gb(self):
        """
        Gets the vpus_per_gb of this UpdateVolumeDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :return: The vpus_per_gb of this UpdateVolumeDetails.
        :rtype: int
        """
        return self._vpus_per_gb

    @vpus_per_gb.setter
    def vpus_per_gb(self, vpus_per_gb):
        """
        Sets the vpus_per_gb of this UpdateVolumeDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Elastic Performance`__ for more information.

        Allowed values:

          * `0`: Represents Lower Cost option.

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

        __ https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumeelasticperformance.htm


        :param vpus_per_gb: The vpus_per_gb of this UpdateVolumeDetails.
        :type: int
        """
        self._vpus_per_gb = vpus_per_gb

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this UpdateVolumeDetails.
        The size to resize the volume to in GBs. Has to be larger than the current size.


        :return: The size_in_gbs of this UpdateVolumeDetails.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this UpdateVolumeDetails.
        The size to resize the volume to in GBs. Has to be larger than the current size.


        :param size_in_gbs: The size_in_gbs of this UpdateVolumeDetails.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
