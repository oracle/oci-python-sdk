# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtRecoveryLocked(object):
    """
    A complex attribute that indicates an password recovery is locked (blocking new sessions)

    **Added In:** 19.1.4

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtRecoveryLocked object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param on:
            The value to assign to the on property of this UserExtRecoveryLocked.
        :type on: bool

        :param lock_date:
            The value to assign to the lock_date property of this UserExtRecoveryLocked.
        :type lock_date: str

        """
        self.swagger_types = {
            'on': 'bool',
            'lock_date': 'str'
        }

        self.attribute_map = {
            'on': 'on',
            'lock_date': 'lockDate'
        }

        self._on = None
        self._lock_date = None

    @property
    def on(self):
        """
        Gets the on of this UserExtRecoveryLocked.
        Indicates that the rev is locked

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The on of this UserExtRecoveryLocked.
        :rtype: bool
        """
        return self._on

    @on.setter
    def on(self, on):
        """
        Sets the on of this UserExtRecoveryLocked.
        Indicates that the rev is locked

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param on: The on of this UserExtRecoveryLocked.
        :type: bool
        """
        self._on = on

    @property
    def lock_date(self):
        """
        Gets the lock_date of this UserExtRecoveryLocked.
        The date and time that the current resource was locked

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The lock_date of this UserExtRecoveryLocked.
        :rtype: str
        """
        return self._lock_date

    @lock_date.setter
    def lock_date(self, lock_date):
        """
        Sets the lock_date of this UserExtRecoveryLocked.
        The date and time that the current resource was locked

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param lock_date: The lock_date of this UserExtRecoveryLocked.
        :type: str
        """
        self._lock_date = lock_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
