# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FormatsForSensitiveType(object):
    """
    A list of library masking formats compatible with an existing sensitive type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FormatsForSensitiveType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this FormatsForSensitiveType.
        :type sensitive_type_id: str

        :param masking_formats:
            The value to assign to the masking_formats property of this FormatsForSensitiveType.
        :type masking_formats: list[oci.data_safe.models.FormatSummary]

        """
        self.swagger_types = {
            'sensitive_type_id': 'str',
            'masking_formats': 'list[FormatSummary]'
        }

        self.attribute_map = {
            'sensitive_type_id': 'sensitiveTypeId',
            'masking_formats': 'maskingFormats'
        }

        self._sensitive_type_id = None
        self._masking_formats = None

    @property
    def sensitive_type_id(self):
        """
        **[Required]** Gets the sensitive_type_id of this FormatsForSensitiveType.
        The OCID of the sensitive type.


        :return: The sensitive_type_id of this FormatsForSensitiveType.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this FormatsForSensitiveType.
        The OCID of the sensitive type.


        :param sensitive_type_id: The sensitive_type_id of this FormatsForSensitiveType.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def masking_formats(self):
        """
        Gets the masking_formats of this FormatsForSensitiveType.
        An array of the library masking formats compatible with the sensitive type.


        :return: The masking_formats of this FormatsForSensitiveType.
        :rtype: list[oci.data_safe.models.FormatSummary]
        """
        return self._masking_formats

    @masking_formats.setter
    def masking_formats(self, masking_formats):
        """
        Sets the masking_formats of this FormatsForSensitiveType.
        An array of the library masking formats compatible with the sensitive type.


        :param masking_formats: The masking_formats of this FormatsForSensitiveType.
        :type: list[oci.data_safe.models.FormatSummary]
        """
        self._masking_formats = masking_formats

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
