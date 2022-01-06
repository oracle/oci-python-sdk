# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .secret_bundle_content_details import SecretBundleContentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Base64SecretBundleContentDetails(SecretBundleContentDetails):
    """
    The contents of the secret.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Base64SecretBundleContentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.secrets.models.Base64SecretBundleContentDetails.content_type` attribute
        of this class is ``BASE64`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this Base64SecretBundleContentDetails.
            Allowed values for this property are: "BASE64"
        :type content_type: str

        :param content:
            The value to assign to the content property of this Base64SecretBundleContentDetails.
        :type content: str

        """
        self.swagger_types = {
            'content_type': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'content': 'content'
        }

        self._content_type = None
        self._content = None
        self._content_type = 'BASE64'

    @property
    def content(self):
        """
        Gets the content of this Base64SecretBundleContentDetails.
        The base64-encoded content of the secret.


        :return: The content of this Base64SecretBundleContentDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Base64SecretBundleContentDetails.
        The base64-encoded content of the secret.


        :param content: The content of this Base64SecretBundleContentDetails.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
