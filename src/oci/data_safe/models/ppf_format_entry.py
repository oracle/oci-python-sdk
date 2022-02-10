# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PPFFormatEntry(FormatEntry):
    """
    The Post Processing Function masking format is a special masking option that
    enables you to use a custom function to further transform column values after
    they have been masked using some other masking formats. It takes the intermediate
    masked values as input and returns the final masked values. For example, you can
    use it for adding checksums or special encodings to the masked values.

    A post-processing function has the same signature as a user-defined function,
    but it passes in the masked values the masking engine generates, and returns
    the final masked values that should be used for masking. To learn more, check
    Post Processing Function in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PPFFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.PPFFormatEntry.type` attribute
        of this class is ``POST_PROCESSING_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PPFFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this PPFFormatEntry.
        :type description: str

        :param post_processing_function:
            The value to assign to the post_processing_function property of this PPFFormatEntry.
        :type post_processing_function: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'post_processing_function': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'post_processing_function': 'postProcessingFunction'
        }

        self._type = None
        self._description = None
        self._post_processing_function = None
        self._type = 'POST_PROCESSING_FUNCTION'

    @property
    def post_processing_function(self):
        """
        **[Required]** Gets the post_processing_function of this PPFFormatEntry.
        The post processing function in SCHEMA_NAME.PACKAGE_NAME.FUNCTION_NAME
        format. It can be a standalone or packaged function, so PACKAGE_NAME
        is optional.


        :return: The post_processing_function of this PPFFormatEntry.
        :rtype: str
        """
        return self._post_processing_function

    @post_processing_function.setter
    def post_processing_function(self, post_processing_function):
        """
        Sets the post_processing_function of this PPFFormatEntry.
        The post processing function in SCHEMA_NAME.PACKAGE_NAME.FUNCTION_NAME
        format. It can be a standalone or packaged function, so PACKAGE_NAME
        is optional.


        :param post_processing_function: The post_processing_function of this PPFFormatEntry.
        :type: str
        """
        self._post_processing_function = post_processing_function

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
