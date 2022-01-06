# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Validity(object):
    """
    An object that describes a period of time during which an entity is valid. If this is not provided when you create a certificate, the validity of the issuing CA is used.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Validity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_of_validity_not_before:
            The value to assign to the time_of_validity_not_before property of this Validity.
        :type time_of_validity_not_before: datetime

        :param time_of_validity_not_after:
            The value to assign to the time_of_validity_not_after property of this Validity.
        :type time_of_validity_not_after: datetime

        """
        self.swagger_types = {
            'time_of_validity_not_before': 'datetime',
            'time_of_validity_not_after': 'datetime'
        }

        self.attribute_map = {
            'time_of_validity_not_before': 'timeOfValidityNotBefore',
            'time_of_validity_not_after': 'timeOfValidityNotAfter'
        }

        self._time_of_validity_not_before = None
        self._time_of_validity_not_after = None

    @property
    def time_of_validity_not_before(self):
        """
        Gets the time_of_validity_not_before of this Validity.
        The date on which the certificate validity period begins, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_validity_not_before of this Validity.
        :rtype: datetime
        """
        return self._time_of_validity_not_before

    @time_of_validity_not_before.setter
    def time_of_validity_not_before(self, time_of_validity_not_before):
        """
        Sets the time_of_validity_not_before of this Validity.
        The date on which the certificate validity period begins, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_validity_not_before: The time_of_validity_not_before of this Validity.
        :type: datetime
        """
        self._time_of_validity_not_before = time_of_validity_not_before

    @property
    def time_of_validity_not_after(self):
        """
        **[Required]** Gets the time_of_validity_not_after of this Validity.
        The date on which the certificate validity period ends, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_validity_not_after of this Validity.
        :rtype: datetime
        """
        return self._time_of_validity_not_after

    @time_of_validity_not_after.setter
    def time_of_validity_not_after(self, time_of_validity_not_after):
        """
        Sets the time_of_validity_not_after of this Validity.
        The date on which the certificate validity period ends, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_validity_not_after: The time_of_validity_not_after of this Validity.
        :type: datetime
        """
        self._time_of_validity_not_after = time_of_validity_not_after

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
