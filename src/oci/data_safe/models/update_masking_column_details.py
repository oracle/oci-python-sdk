# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMaskingColumnDetails(object):
    """
    Details to update a masking column.
    """

    #: A constant which can be used with the object_type property of a UpdateMaskingColumnDetails.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a UpdateMaskingColumnDetails.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMaskingColumnDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_type:
            The value to assign to the object_type property of this UpdateMaskingColumnDetails.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW"
        :type object_type: str

        :param masking_column_group:
            The value to assign to the masking_column_group property of this UpdateMaskingColumnDetails.
        :type masking_column_group: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this UpdateMaskingColumnDetails.
        :type sensitive_type_id: str

        :param is_masking_enabled:
            The value to assign to the is_masking_enabled property of this UpdateMaskingColumnDetails.
        :type is_masking_enabled: bool

        :param masking_formats:
            The value to assign to the masking_formats property of this UpdateMaskingColumnDetails.
        :type masking_formats: list[oci.data_safe.models.MaskingFormat]

        """
        self.swagger_types = {
            'object_type': 'str',
            'masking_column_group': 'str',
            'sensitive_type_id': 'str',
            'is_masking_enabled': 'bool',
            'masking_formats': 'list[MaskingFormat]'
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'masking_column_group': 'maskingColumnGroup',
            'sensitive_type_id': 'sensitiveTypeId',
            'is_masking_enabled': 'isMaskingEnabled',
            'masking_formats': 'maskingFormats'
        }

        self._object_type = None
        self._masking_column_group = None
        self._sensitive_type_id = None
        self._is_masking_enabled = None
        self._masking_formats = None

    @property
    def object_type(self):
        """
        Gets the object_type of this UpdateMaskingColumnDetails.
        The type of the object that contains the database column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW"


        :return: The object_type of this UpdateMaskingColumnDetails.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this UpdateMaskingColumnDetails.
        The type of the object that contains the database column.


        :param object_type: The object_type of this UpdateMaskingColumnDetails.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            raise ValueError(
                "Invalid value for `object_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._object_type = object_type

    @property
    def masking_column_group(self):
        """
        Gets the masking_column_group of this UpdateMaskingColumnDetails.
        The group of the masking column. It's a masking group identifier and can be any
        string of acceptable length. All the columns in a group are masked together to
        ensure that the masked data across these columns continue to retain the same
        logical relationship. For more details, check
        <a href=https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037>Group Masking in the Data Safe documentation.</a>


        :return: The masking_column_group of this UpdateMaskingColumnDetails.
        :rtype: str
        """
        return self._masking_column_group

    @masking_column_group.setter
    def masking_column_group(self, masking_column_group):
        """
        Sets the masking_column_group of this UpdateMaskingColumnDetails.
        The group of the masking column. It's a masking group identifier and can be any
        string of acceptable length. All the columns in a group are masked together to
        ensure that the masked data across these columns continue to retain the same
        logical relationship. For more details, check
        <a href=https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037>Group Masking in the Data Safe documentation.</a>


        :param masking_column_group: The masking_column_group of this UpdateMaskingColumnDetails.
        :type: str
        """
        self._masking_column_group = masking_column_group

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this UpdateMaskingColumnDetails.
        The OCID of the sensitive type to be associated with the masking column. Note that there will be no change in
        assigned masking format when sensitive type is changed.


        :return: The sensitive_type_id of this UpdateMaskingColumnDetails.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this UpdateMaskingColumnDetails.
        The OCID of the sensitive type to be associated with the masking column. Note that there will be no change in
        assigned masking format when sensitive type is changed.


        :param sensitive_type_id: The sensitive_type_id of this UpdateMaskingColumnDetails.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def is_masking_enabled(self):
        """
        Gets the is_masking_enabled of this UpdateMaskingColumnDetails.
        Indicates if data masking is enabled for the masking column. Set it to false
        if you don't want to mask the column.


        :return: The is_masking_enabled of this UpdateMaskingColumnDetails.
        :rtype: bool
        """
        return self._is_masking_enabled

    @is_masking_enabled.setter
    def is_masking_enabled(self, is_masking_enabled):
        """
        Sets the is_masking_enabled of this UpdateMaskingColumnDetails.
        Indicates if data masking is enabled for the masking column. Set it to false
        if you don't want to mask the column.


        :param is_masking_enabled: The is_masking_enabled of this UpdateMaskingColumnDetails.
        :type: bool
        """
        self._is_masking_enabled = is_masking_enabled

    @property
    def masking_formats(self):
        """
        Gets the masking_formats of this UpdateMaskingColumnDetails.
        The masking formats to be assigned to the masking column. You can specify a
        condition as part of each masking format. It enables you to do
        <a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\">conditional masking</a>
        so that you can mask the column data values differently using different
        masking formats and the associated conditions. A masking format can have
        one or more format entries. The combined output of all the format entries is
        used for masking. It provides the flexibility to define a masking format that
        can generate different parts of a data value separately and then combine them
        to get the final data value for masking.


        :return: The masking_formats of this UpdateMaskingColumnDetails.
        :rtype: list[oci.data_safe.models.MaskingFormat]
        """
        return self._masking_formats

    @masking_formats.setter
    def masking_formats(self, masking_formats):
        """
        Sets the masking_formats of this UpdateMaskingColumnDetails.
        The masking formats to be assigned to the masking column. You can specify a
        condition as part of each masking format. It enables you to do
        <a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\">conditional masking</a>
        so that you can mask the column data values differently using different
        masking formats and the associated conditions. A masking format can have
        one or more format entries. The combined output of all the format entries is
        used for masking. It provides the flexibility to define a masking format that
        can generate different parts of a data value separately and then combine them
        to get the final data value for masking.


        :param masking_formats: The masking_formats of this UpdateMaskingColumnDetails.
        :type: list[oci.data_safe.models.MaskingFormat]
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
