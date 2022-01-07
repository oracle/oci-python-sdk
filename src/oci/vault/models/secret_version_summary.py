# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretVersionSummary(object):
    """
    The secret version summary object, which doesn't include the contents of the secret.
    """

    #: A constant which can be used with the content_type property of a SecretVersionSummary.
    #: This constant has a value of "BASE64"
    CONTENT_TYPE_BASE64 = "BASE64"

    #: A constant which can be used with the stages property of a SecretVersionSummary.
    #: This constant has a value of "CURRENT"
    STAGES_CURRENT = "CURRENT"

    #: A constant which can be used with the stages property of a SecretVersionSummary.
    #: This constant has a value of "PENDING"
    STAGES_PENDING = "PENDING"

    #: A constant which can be used with the stages property of a SecretVersionSummary.
    #: This constant has a value of "LATEST"
    STAGES_LATEST = "LATEST"

    #: A constant which can be used with the stages property of a SecretVersionSummary.
    #: This constant has a value of "PREVIOUS"
    STAGES_PREVIOUS = "PREVIOUS"

    #: A constant which can be used with the stages property of a SecretVersionSummary.
    #: This constant has a value of "DEPRECATED"
    STAGES_DEPRECATED = "DEPRECATED"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this SecretVersionSummary.
            Allowed values for this property are: "BASE64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type content_type: str

        :param name:
            The value to assign to the name property of this SecretVersionSummary.
        :type name: str

        :param secret_id:
            The value to assign to the secret_id property of this SecretVersionSummary.
        :type secret_id: str

        :param stages:
            The value to assign to the stages property of this SecretVersionSummary.
            Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stages: list[str]

        :param time_created:
            The value to assign to the time_created property of this SecretVersionSummary.
        :type time_created: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this SecretVersionSummary.
        :type time_of_deletion: datetime

        :param time_of_expiry:
            The value to assign to the time_of_expiry property of this SecretVersionSummary.
        :type time_of_expiry: datetime

        :param version_number:
            The value to assign to the version_number property of this SecretVersionSummary.
        :type version_number: int

        """
        self.swagger_types = {
            'content_type': 'str',
            'name': 'str',
            'secret_id': 'str',
            'stages': 'list[str]',
            'time_created': 'datetime',
            'time_of_deletion': 'datetime',
            'time_of_expiry': 'datetime',
            'version_number': 'int'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'name': 'name',
            'secret_id': 'secretId',
            'stages': 'stages',
            'time_created': 'timeCreated',
            'time_of_deletion': 'timeOfDeletion',
            'time_of_expiry': 'timeOfExpiry',
            'version_number': 'versionNumber'
        }

        self._content_type = None
        self._name = None
        self._secret_id = None
        self._stages = None
        self._time_created = None
        self._time_of_deletion = None
        self._time_of_expiry = None
        self._version_number = None

    @property
    def content_type(self):
        """
        Gets the content_type of this SecretVersionSummary.
        The content type of the secret version's secret contents.

        Allowed values for this property are: "BASE64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The content_type of this SecretVersionSummary.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this SecretVersionSummary.
        The content type of the secret version's secret contents.


        :param content_type: The content_type of this SecretVersionSummary.
        :type: str
        """
        allowed_values = ["BASE64"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            content_type = 'UNKNOWN_ENUM_VALUE'
        self._content_type = content_type

    @property
    def name(self):
        """
        Gets the name of this SecretVersionSummary.
        The name of the secret version. A name is unique across versions of a secret.


        :return: The name of this SecretVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecretVersionSummary.
        The name of the secret version. A name is unique across versions of a secret.


        :param name: The name of this SecretVersionSummary.
        :type: str
        """
        self._name = name

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this SecretVersionSummary.
        The OCID of the secret.


        :return: The secret_id of this SecretVersionSummary.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this SecretVersionSummary.
        The OCID of the secret.


        :param secret_id: The secret_id of this SecretVersionSummary.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def stages(self):
        """
        Gets the stages of this SecretVersionSummary.
        A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version
        marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated
        into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is
        always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked
        `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous
        one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.

        Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stages of this SecretVersionSummary.
        :rtype: list[str]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this SecretVersionSummary.
        A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version
        marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated
        into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is
        always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked
        `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous
        one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.


        :param stages: The stages of this SecretVersionSummary.
        :type: list[str]
        """
        allowed_values = ["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"]
        if stages:
            stages[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in stages]
        self._stages = stages

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SecretVersionSummary.
        A optional property indicating when the secret version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SecretVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecretVersionSummary.
        A optional property indicating when the secret version was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SecretVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this SecretVersionSummary.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this SecretVersionSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this SecretVersionSummary.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this SecretVersionSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def time_of_expiry(self):
        """
        Gets the time_of_expiry of this SecretVersionSummary.
        An optional property indicating when the secret version will expire, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_expiry of this SecretVersionSummary.
        :rtype: datetime
        """
        return self._time_of_expiry

    @time_of_expiry.setter
    def time_of_expiry(self, time_of_expiry):
        """
        Sets the time_of_expiry of this SecretVersionSummary.
        An optional property indicating when the secret version will expire, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_expiry: The time_of_expiry of this SecretVersionSummary.
        :type: datetime
        """
        self._time_of_expiry = time_of_expiry

    @property
    def version_number(self):
        """
        **[Required]** Gets the version_number of this SecretVersionSummary.
        The version number of the secret.


        :return: The version_number of this SecretVersionSummary.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this SecretVersionSummary.
        The version number of the secret.


        :param version_number: The version_number of this SecretVersionSummary.
        :type: int
        """
        self._version_number = version_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
