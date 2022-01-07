# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RevocationStatus(object):
    """
    The current revocation status of the entity.
    """

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "UNSPECIFIED"
    REVOCATION_REASON_UNSPECIFIED = "UNSPECIFIED"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "KEY_COMPROMISE"
    REVOCATION_REASON_KEY_COMPROMISE = "KEY_COMPROMISE"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "CA_COMPROMISE"
    REVOCATION_REASON_CA_COMPROMISE = "CA_COMPROMISE"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "AFFILIATION_CHANGED"
    REVOCATION_REASON_AFFILIATION_CHANGED = "AFFILIATION_CHANGED"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "SUPERSEDED"
    REVOCATION_REASON_SUPERSEDED = "SUPERSEDED"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "CESSATION_OF_OPERATION"
    REVOCATION_REASON_CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "PRIVILEGE_WITHDRAWN"
    REVOCATION_REASON_PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"

    #: A constant which can be used with the revocation_reason property of a RevocationStatus.
    #: This constant has a value of "AA_COMPROMISE"
    REVOCATION_REASON_AA_COMPROMISE = "AA_COMPROMISE"

    def __init__(self, **kwargs):
        """
        Initializes a new RevocationStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_of_revocation:
            The value to assign to the time_of_revocation property of this RevocationStatus.
        :type time_of_revocation: datetime

        :param revocation_reason:
            The value to assign to the revocation_reason property of this RevocationStatus.
            Allowed values for this property are: "UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "AFFILIATION_CHANGED", "SUPERSEDED", "CESSATION_OF_OPERATION", "PRIVILEGE_WITHDRAWN", "AA_COMPROMISE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type revocation_reason: str

        """
        self.swagger_types = {
            'time_of_revocation': 'datetime',
            'revocation_reason': 'str'
        }

        self.attribute_map = {
            'time_of_revocation': 'timeOfRevocation',
            'revocation_reason': 'revocationReason'
        }

        self._time_of_revocation = None
        self._revocation_reason = None

    @property
    def time_of_revocation(self):
        """
        **[Required]** Gets the time_of_revocation of this RevocationStatus.
        The time when the entity was revoked, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_revocation of this RevocationStatus.
        :rtype: datetime
        """
        return self._time_of_revocation

    @time_of_revocation.setter
    def time_of_revocation(self, time_of_revocation):
        """
        Sets the time_of_revocation of this RevocationStatus.
        The time when the entity was revoked, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_revocation: The time_of_revocation of this RevocationStatus.
        :type: datetime
        """
        self._time_of_revocation = time_of_revocation

    @property
    def revocation_reason(self):
        """
        **[Required]** Gets the revocation_reason of this RevocationStatus.
        The reason the certificate or certificate authority (CA) was revoked.

        Allowed values for this property are: "UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "AFFILIATION_CHANGED", "SUPERSEDED", "CESSATION_OF_OPERATION", "PRIVILEGE_WITHDRAWN", "AA_COMPROMISE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The revocation_reason of this RevocationStatus.
        :rtype: str
        """
        return self._revocation_reason

    @revocation_reason.setter
    def revocation_reason(self, revocation_reason):
        """
        Sets the revocation_reason of this RevocationStatus.
        The reason the certificate or certificate authority (CA) was revoked.


        :param revocation_reason: The revocation_reason of this RevocationStatus.
        :type: str
        """
        allowed_values = ["UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "AFFILIATION_CHANGED", "SUPERSEDED", "CESSATION_OF_OPERATION", "PRIVILEGE_WITHDRAWN", "AA_COMPROMISE"]
        if not value_allowed_none_or_none_sentinel(revocation_reason, allowed_values):
            revocation_reason = 'UNKNOWN_ENUM_VALUE'
        self._revocation_reason = revocation_reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
