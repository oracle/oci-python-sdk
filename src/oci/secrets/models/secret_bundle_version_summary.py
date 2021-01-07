# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretBundleVersionSummary(object):
    """
    The properties of the secret bundle. (Secret bundle version summary objects do not include the actual contents of the secret.)
    """

    #: A constant which can be used with the stages property of a SecretBundleVersionSummary.
    #: This constant has a value of "CURRENT"
    STAGES_CURRENT = "CURRENT"

    #: A constant which can be used with the stages property of a SecretBundleVersionSummary.
    #: This constant has a value of "PENDING"
    STAGES_PENDING = "PENDING"

    #: A constant which can be used with the stages property of a SecretBundleVersionSummary.
    #: This constant has a value of "LATEST"
    STAGES_LATEST = "LATEST"

    #: A constant which can be used with the stages property of a SecretBundleVersionSummary.
    #: This constant has a value of "PREVIOUS"
    STAGES_PREVIOUS = "PREVIOUS"

    #: A constant which can be used with the stages property of a SecretBundleVersionSummary.
    #: This constant has a value of "DEPRECATED"
    STAGES_DEPRECATED = "DEPRECATED"

    def __init__(self, **kwargs):
        """
        Initializes a new SecretBundleVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_id:
            The value to assign to the secret_id property of this SecretBundleVersionSummary.
        :type secret_id: str

        :param time_created:
            The value to assign to the time_created property of this SecretBundleVersionSummary.
        :type time_created: datetime

        :param version_number:
            The value to assign to the version_number property of this SecretBundleVersionSummary.
        :type version_number: int

        :param version_name:
            The value to assign to the version_name property of this SecretBundleVersionSummary.
        :type version_name: str

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this SecretBundleVersionSummary.
        :type time_of_deletion: datetime

        :param time_of_expiry:
            The value to assign to the time_of_expiry property of this SecretBundleVersionSummary.
        :type time_of_expiry: datetime

        :param stages:
            The value to assign to the stages property of this SecretBundleVersionSummary.
            Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type stages: list[str]

        """
        self.swagger_types = {
            'secret_id': 'str',
            'time_created': 'datetime',
            'version_number': 'int',
            'version_name': 'str',
            'time_of_deletion': 'datetime',
            'time_of_expiry': 'datetime',
            'stages': 'list[str]'
        }

        self.attribute_map = {
            'secret_id': 'secretId',
            'time_created': 'timeCreated',
            'version_number': 'versionNumber',
            'version_name': 'versionName',
            'time_of_deletion': 'timeOfDeletion',
            'time_of_expiry': 'timeOfExpiry',
            'stages': 'stages'
        }

        self._secret_id = None
        self._time_created = None
        self._version_number = None
        self._version_name = None
        self._time_of_deletion = None
        self._time_of_expiry = None
        self._stages = None

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this SecretBundleVersionSummary.
        The OCID of the secret.


        :return: The secret_id of this SecretBundleVersionSummary.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this SecretBundleVersionSummary.
        The OCID of the secret.


        :param secret_id: The secret_id of this SecretBundleVersionSummary.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def time_created(self):
        """
        Gets the time_created of this SecretBundleVersionSummary.
        The time when the secret bundle was created.


        :return: The time_created of this SecretBundleVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecretBundleVersionSummary.
        The time when the secret bundle was created.


        :param time_created: The time_created of this SecretBundleVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version_number(self):
        """
        **[Required]** Gets the version_number of this SecretBundleVersionSummary.
        The version number of the secret.


        :return: The version_number of this SecretBundleVersionSummary.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """
        Sets the version_number of this SecretBundleVersionSummary.
        The version number of the secret.


        :param version_number: The version_number of this SecretBundleVersionSummary.
        :type: int
        """
        self._version_number = version_number

    @property
    def version_name(self):
        """
        Gets the version_name of this SecretBundleVersionSummary.
        The version name of the secret bundle, as provided when the secret was created or last rotated.


        :return: The version_name of this SecretBundleVersionSummary.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this SecretBundleVersionSummary.
        The version name of the secret bundle, as provided when the secret was created or last rotated.


        :param version_name: The version_name of this SecretBundleVersionSummary.
        :type: str
        """
        self._version_name = version_name

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this SecretBundleVersionSummary.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this SecretBundleVersionSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this SecretBundleVersionSummary.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this SecretBundleVersionSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def time_of_expiry(self):
        """
        Gets the time_of_expiry of this SecretBundleVersionSummary.
        An optional property indicating when the secret version will expire, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_expiry of this SecretBundleVersionSummary.
        :rtype: datetime
        """
        return self._time_of_expiry

    @time_of_expiry.setter
    def time_of_expiry(self, time_of_expiry):
        """
        Sets the time_of_expiry of this SecretBundleVersionSummary.
        An optional property indicating when the secret version will expire, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_expiry: The time_of_expiry of this SecretBundleVersionSummary.
        :type: datetime
        """
        self._time_of_expiry = time_of_expiry

    @property
    def stages(self):
        """
        Gets the stages of this SecretBundleVersionSummary.
        A list of possible rotation states for the secret bundle.

        Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The stages of this SecretBundleVersionSummary.
        :rtype: list[str]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this SecretBundleVersionSummary.
        A list of possible rotation states for the secret bundle.


        :param stages: The stages of this SecretBundleVersionSummary.
        :type: list[str]
        """
        allowed_values = ["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"]
        if stages:
            stages[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in stages]
        self._stages = stages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
