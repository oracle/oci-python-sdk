# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretBundleContentDetails(object):
    """
    The contents of the secret.
    """

    #: A constant which can be used with the content_type property of a SecretBundleContentDetails.
    #: This constant has a value of "BASE64"
    CONTENT_TYPE_BASE64 = "BASE64"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretBundleContentDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.secrets.models.Base64SecretBundleContentDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this SecretBundleContentDetails.
            Allowed values for this property are: "BASE64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type content_type: str

        """
        self.swagger_types = {
            'content_type': 'str'
        }

        self.attribute_map = {
            'content_type': 'contentType'
        }

        self._content_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['contentType']

        if type == 'BASE64':
            return 'Base64SecretBundleContentDetails'
        else:
            return 'SecretBundleContentDetails'

    @property
    def content_type(self):
        """
        **[Required]** Gets the content_type of this SecretBundleContentDetails.
        The formatting type of the secret contents.

        Allowed values for this property are: "BASE64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The content_type of this SecretBundleContentDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this SecretBundleContentDetails.
        The formatting type of the secret contents.


        :param content_type: The content_type of this SecretBundleContentDetails.
        :type: str
        """
        allowed_values = ["BASE64"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            content_type = 'UNKNOWN_ENUM_VALUE'
        self._content_type = content_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
