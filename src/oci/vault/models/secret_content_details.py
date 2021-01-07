# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretContentDetails(object):
    """
    The content of the secret and metadata to help identify it.
    """

    #: A constant which can be used with the content_type property of a SecretContentDetails.
    #: This constant has a value of "BASE64"
    CONTENT_TYPE_BASE64 = "BASE64"

    #: A constant which can be used with the stage property of a SecretContentDetails.
    #: This constant has a value of "CURRENT"
    STAGE_CURRENT = "CURRENT"

    #: A constant which can be used with the stage property of a SecretContentDetails.
    #: This constant has a value of "PENDING"
    STAGE_PENDING = "PENDING"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretContentDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vault.models.Base64SecretContentDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this SecretContentDetails.
            Allowed values for this property are: "BASE64"
        :type content_type: str

        :param name:
            The value to assign to the name property of this SecretContentDetails.
        :type name: str

        :param stage:
            The value to assign to the stage property of this SecretContentDetails.
            Allowed values for this property are: "CURRENT", "PENDING"
        :type stage: str

        """
        self.swagger_types = {
            'content_type': 'str',
            'name': 'str',
            'stage': 'str'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'name': 'name',
            'stage': 'stage'
        }

        self._content_type = None
        self._name = None
        self._stage = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['contentType']

        if type == 'BASE64':
            return 'Base64SecretContentDetails'
        else:
            return 'SecretContentDetails'

    @property
    def content_type(self):
        """
        **[Required]** Gets the content_type of this SecretContentDetails.
        The base64-encoded content of the secret.

        Allowed values for this property are: "BASE64"


        :return: The content_type of this SecretContentDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this SecretContentDetails.
        The base64-encoded content of the secret.


        :param content_type: The content_type of this SecretContentDetails.
        :type: str
        """
        allowed_values = ["BASE64"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            raise ValueError(
                "Invalid value for `content_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._content_type = content_type

    @property
    def name(self):
        """
        Gets the name of this SecretContentDetails.
        Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this SecretContentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecretContentDetails.
        Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this SecretContentDetails.
        :type: str
        """
        self._name = name

    @property
    def stage(self):
        """
        Gets the stage of this SecretContentDetails.
        The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version
        that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
        you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system.
        When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating
        a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.

        Allowed values for this property are: "CURRENT", "PENDING"


        :return: The stage of this SecretContentDetails.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """
        Sets the stage of this SecretContentDetails.
        The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version
        that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
        you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system.
        When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating
        a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.


        :param stage: The stage of this SecretContentDetails.
        :type: str
        """
        allowed_values = ["CURRENT", "PENDING"]
        if not value_allowed_none_or_none_sentinel(stage, allowed_values):
            raise ValueError(
                "Invalid value for `stage`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._stage = stage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
