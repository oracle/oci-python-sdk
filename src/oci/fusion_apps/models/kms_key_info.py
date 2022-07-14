# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KmsKeyInfo(object):
    """
    kmsKeyInfo
    """

    #: A constant which can be used with the scheduled_key_status property of a KmsKeyInfo.
    #: This constant has a value of "SCHEDULING"
    SCHEDULED_KEY_STATUS_SCHEDULING = "SCHEDULING"

    #: A constant which can be used with the scheduled_key_status property of a KmsKeyInfo.
    #: This constant has a value of "UPDATING"
    SCHEDULED_KEY_STATUS_UPDATING = "UPDATING"

    #: A constant which can be used with the scheduled_key_status property of a KmsKeyInfo.
    #: This constant has a value of "FAILED"
    SCHEDULED_KEY_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the scheduled_key_status property of a KmsKeyInfo.
    #: This constant has a value of "NONE"
    SCHEDULED_KEY_STATUS_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new KmsKeyInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param active_key_id:
            The value to assign to the active_key_id property of this KmsKeyInfo.
        :type active_key_id: str

        :param active_key_version:
            The value to assign to the active_key_version property of this KmsKeyInfo.
        :type active_key_version: str

        :param scheduled_key_id:
            The value to assign to the scheduled_key_id property of this KmsKeyInfo.
        :type scheduled_key_id: str

        :param scheduled_key_version:
            The value to assign to the scheduled_key_version property of this KmsKeyInfo.
        :type scheduled_key_version: str

        :param current_key_lifecycle_state:
            The value to assign to the current_key_lifecycle_state property of this KmsKeyInfo.
        :type current_key_lifecycle_state: str

        :param scheduled_lifecycle_state:
            The value to assign to the scheduled_lifecycle_state property of this KmsKeyInfo.
        :type scheduled_lifecycle_state: str

        :param scheduled_key_status:
            The value to assign to the scheduled_key_status property of this KmsKeyInfo.
            Allowed values for this property are: "SCHEDULING", "UPDATING", "FAILED", "NONE"
        :type scheduled_key_status: str

        """
        self.swagger_types = {
            'active_key_id': 'str',
            'active_key_version': 'str',
            'scheduled_key_id': 'str',
            'scheduled_key_version': 'str',
            'current_key_lifecycle_state': 'str',
            'scheduled_lifecycle_state': 'str',
            'scheduled_key_status': 'str'
        }

        self.attribute_map = {
            'active_key_id': 'activeKeyId',
            'active_key_version': 'activeKeyVersion',
            'scheduled_key_id': 'scheduledKeyId',
            'scheduled_key_version': 'scheduledKeyVersion',
            'current_key_lifecycle_state': 'currentKeyLifecycleState',
            'scheduled_lifecycle_state': 'scheduledLifecycleState',
            'scheduled_key_status': 'scheduledKeyStatus'
        }

        self._active_key_id = None
        self._active_key_version = None
        self._scheduled_key_id = None
        self._scheduled_key_version = None
        self._current_key_lifecycle_state = None
        self._scheduled_lifecycle_state = None
        self._scheduled_key_status = None

    @property
    def active_key_id(self):
        """
        Gets the active_key_id of this KmsKeyInfo.
        current BYOK keyId facp is using


        :return: The active_key_id of this KmsKeyInfo.
        :rtype: str
        """
        return self._active_key_id

    @active_key_id.setter
    def active_key_id(self, active_key_id):
        """
        Sets the active_key_id of this KmsKeyInfo.
        current BYOK keyId facp is using


        :param active_key_id: The active_key_id of this KmsKeyInfo.
        :type: str
        """
        self._active_key_id = active_key_id

    @property
    def active_key_version(self):
        """
        Gets the active_key_version of this KmsKeyInfo.
        current key version facp is using


        :return: The active_key_version of this KmsKeyInfo.
        :rtype: str
        """
        return self._active_key_version

    @active_key_version.setter
    def active_key_version(self, active_key_version):
        """
        Sets the active_key_version of this KmsKeyInfo.
        current key version facp is using


        :param active_key_version: The active_key_version of this KmsKeyInfo.
        :type: str
        """
        self._active_key_version = active_key_version

    @property
    def scheduled_key_id(self):
        """
        Gets the scheduled_key_id of this KmsKeyInfo.
        scheduled keyId to be updated


        :return: The scheduled_key_id of this KmsKeyInfo.
        :rtype: str
        """
        return self._scheduled_key_id

    @scheduled_key_id.setter
    def scheduled_key_id(self, scheduled_key_id):
        """
        Sets the scheduled_key_id of this KmsKeyInfo.
        scheduled keyId to be updated


        :param scheduled_key_id: The scheduled_key_id of this KmsKeyInfo.
        :type: str
        """
        self._scheduled_key_id = scheduled_key_id

    @property
    def scheduled_key_version(self):
        """
        Gets the scheduled_key_version of this KmsKeyInfo.
        scheduled key version to be updated.


        :return: The scheduled_key_version of this KmsKeyInfo.
        :rtype: str
        """
        return self._scheduled_key_version

    @scheduled_key_version.setter
    def scheduled_key_version(self, scheduled_key_version):
        """
        Sets the scheduled_key_version of this KmsKeyInfo.
        scheduled key version to be updated.


        :param scheduled_key_version: The scheduled_key_version of this KmsKeyInfo.
        :type: str
        """
        self._scheduled_key_version = scheduled_key_version

    @property
    def current_key_lifecycle_state(self):
        """
        Gets the current_key_lifecycle_state of this KmsKeyInfo.
        current key lifeCycleState


        :return: The current_key_lifecycle_state of this KmsKeyInfo.
        :rtype: str
        """
        return self._current_key_lifecycle_state

    @current_key_lifecycle_state.setter
    def current_key_lifecycle_state(self, current_key_lifecycle_state):
        """
        Sets the current_key_lifecycle_state of this KmsKeyInfo.
        current key lifeCycleState


        :param current_key_lifecycle_state: The current_key_lifecycle_state of this KmsKeyInfo.
        :type: str
        """
        self._current_key_lifecycle_state = current_key_lifecycle_state

    @property
    def scheduled_lifecycle_state(self):
        """
        Gets the scheduled_lifecycle_state of this KmsKeyInfo.
        scheduled key lifeCycle state to be updated.


        :return: The scheduled_lifecycle_state of this KmsKeyInfo.
        :rtype: str
        """
        return self._scheduled_lifecycle_state

    @scheduled_lifecycle_state.setter
    def scheduled_lifecycle_state(self, scheduled_lifecycle_state):
        """
        Sets the scheduled_lifecycle_state of this KmsKeyInfo.
        scheduled key lifeCycle state to be updated.


        :param scheduled_lifecycle_state: The scheduled_lifecycle_state of this KmsKeyInfo.
        :type: str
        """
        self._scheduled_lifecycle_state = scheduled_lifecycle_state

    @property
    def scheduled_key_status(self):
        """
        Gets the scheduled_key_status of this KmsKeyInfo.
        the scheduled key status

        Allowed values for this property are: "SCHEDULING", "UPDATING", "FAILED", "NONE"


        :return: The scheduled_key_status of this KmsKeyInfo.
        :rtype: str
        """
        return self._scheduled_key_status

    @scheduled_key_status.setter
    def scheduled_key_status(self, scheduled_key_status):
        """
        Sets the scheduled_key_status of this KmsKeyInfo.
        the scheduled key status


        :param scheduled_key_status: The scheduled_key_status of this KmsKeyInfo.
        :type: str
        """
        allowed_values = ["SCHEDULING", "UPDATING", "FAILED", "NONE"]
        if not value_allowed_none_or_none_sentinel(scheduled_key_status, allowed_values):
            raise ValueError(
                "Invalid value for `scheduled_key_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scheduled_key_status = scheduled_key_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
