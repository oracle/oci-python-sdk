# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceErratumSummary(object):
    """
    Provides summary information about an erratum associated with a managed instance.
    """

    #: A constant which can be used with the advisory_type property of a ManagedInstanceErratumSummary.
    #: This constant has a value of "SECURITY"
    ADVISORY_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the advisory_type property of a ManagedInstanceErratumSummary.
    #: This constant has a value of "BUGFIX"
    ADVISORY_TYPE_BUGFIX = "BUGFIX"

    #: A constant which can be used with the advisory_type property of a ManagedInstanceErratumSummary.
    #: This constant has a value of "ENHANCEMENT"
    ADVISORY_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the advisory_type property of a ManagedInstanceErratumSummary.
    #: This constant has a value of "OTHER"
    ADVISORY_TYPE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceErratumSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceErratumSummary.
        :type name: str

        :param advisory_type:
            The value to assign to the advisory_type property of this ManagedInstanceErratumSummary.
            Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type advisory_type: str

        :param time_issued:
            The value to assign to the time_issued property of this ManagedInstanceErratumSummary.
        :type time_issued: datetime

        :param synopsis:
            The value to assign to the synopsis property of this ManagedInstanceErratumSummary.
        :type synopsis: str

        :param related_cves:
            The value to assign to the related_cves property of this ManagedInstanceErratumSummary.
        :type related_cves: list[str]

        :param packages:
            The value to assign to the packages property of this ManagedInstanceErratumSummary.
        :type packages: list[oci.os_management_hub.models.PackageNameSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'advisory_type': 'str',
            'time_issued': 'datetime',
            'synopsis': 'str',
            'related_cves': 'list[str]',
            'packages': 'list[PackageNameSummary]'
        }
        self.attribute_map = {
            'name': 'name',
            'advisory_type': 'advisoryType',
            'time_issued': 'timeIssued',
            'synopsis': 'synopsis',
            'related_cves': 'relatedCves',
            'packages': 'packages'
        }
        self._name = None
        self._advisory_type = None
        self._time_issued = None
        self._synopsis = None
        self._related_cves = None
        self._packages = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceErratumSummary.
        The identifier of the erratum.


        :return: The name of this ManagedInstanceErratumSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceErratumSummary.
        The identifier of the erratum.


        :param name: The name of this ManagedInstanceErratumSummary.
        :type: str
        """
        self._name = name

    @property
    def advisory_type(self):
        """
        **[Required]** Gets the advisory_type of this ManagedInstanceErratumSummary.
        The advisory type of the erratum.

        Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The advisory_type of this ManagedInstanceErratumSummary.
        :rtype: str
        """
        return self._advisory_type

    @advisory_type.setter
    def advisory_type(self, advisory_type):
        """
        Sets the advisory_type of this ManagedInstanceErratumSummary.
        The advisory type of the erratum.


        :param advisory_type: The advisory_type of this ManagedInstanceErratumSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(advisory_type, allowed_values):
            advisory_type = 'UNKNOWN_ENUM_VALUE'
        self._advisory_type = advisory_type

    @property
    def time_issued(self):
        """
        Gets the time_issued of this ManagedInstanceErratumSummary.
        The date and time the package was issued by a providing erratum (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_issued of this ManagedInstanceErratumSummary.
        :rtype: datetime
        """
        return self._time_issued

    @time_issued.setter
    def time_issued(self, time_issued):
        """
        Sets the time_issued of this ManagedInstanceErratumSummary.
        The date and time the package was issued by a providing erratum (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_issued: The time_issued of this ManagedInstanceErratumSummary.
        :type: datetime
        """
        self._time_issued = time_issued

    @property
    def synopsis(self):
        """
        Gets the synopsis of this ManagedInstanceErratumSummary.
        A summary description of the erratum.


        :return: The synopsis of this ManagedInstanceErratumSummary.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """
        Sets the synopsis of this ManagedInstanceErratumSummary.
        A summary description of the erratum.


        :param synopsis: The synopsis of this ManagedInstanceErratumSummary.
        :type: str
        """
        self._synopsis = synopsis

    @property
    def related_cves(self):
        """
        Gets the related_cves of this ManagedInstanceErratumSummary.
        The list of CVEs applicable to this erratum.


        :return: The related_cves of this ManagedInstanceErratumSummary.
        :rtype: list[str]
        """
        return self._related_cves

    @related_cves.setter
    def related_cves(self, related_cves):
        """
        Sets the related_cves of this ManagedInstanceErratumSummary.
        The list of CVEs applicable to this erratum.


        :param related_cves: The related_cves of this ManagedInstanceErratumSummary.
        :type: list[str]
        """
        self._related_cves = related_cves

    @property
    def packages(self):
        """
        **[Required]** Gets the packages of this ManagedInstanceErratumSummary.
        The list of packages affected by this erratum.


        :return: The packages of this ManagedInstanceErratumSummary.
        :rtype: list[oci.os_management_hub.models.PackageNameSummary]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this ManagedInstanceErratumSummary.
        The list of packages affected by this erratum.


        :param packages: The packages of this ManagedInstanceErratumSummary.
        :type: list[oci.os_management_hub.models.PackageNameSummary]
        """
        self._packages = packages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
