# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Erratum(object):
    """
    Details about the erratum.
    """

    #: A constant which can be used with the advisory_type property of a Erratum.
    #: This constant has a value of "SECURITY"
    ADVISORY_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the advisory_type property of a Erratum.
    #: This constant has a value of "BUG"
    ADVISORY_TYPE_BUG = "BUG"

    #: A constant which can be used with the advisory_type property of a Erratum.
    #: This constant has a value of "ENHANCEMENT"
    ADVISORY_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the advisory_type property of a Erratum.
    #: This constant has a value of "OTHER"
    ADVISORY_TYPE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new Erratum object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Erratum.
        :type name: str

        :param id:
            The value to assign to the id property of this Erratum.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Erratum.
        :type compartment_id: str

        :param synopsis:
            The value to assign to the synopsis property of this Erratum.
        :type synopsis: str

        :param issued:
            The value to assign to the issued property of this Erratum.
        :type issued: str

        :param description:
            The value to assign to the description property of this Erratum.
        :type description: str

        :param updated:
            The value to assign to the updated property of this Erratum.
        :type updated: str

        :param advisory_type:
            The value to assign to the advisory_type property of this Erratum.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type advisory_type: str

        :param _from:
            The value to assign to the _from property of this Erratum.
        :type _from: str

        :param solution:
            The value to assign to the solution property of this Erratum.
        :type solution: str

        :param references:
            The value to assign to the references property of this Erratum.
        :type references: str

        :param affected_instances:
            The value to assign to the affected_instances property of this Erratum.
        :type affected_instances: list[oci.os_management.models.Id]

        :param related_cves:
            The value to assign to the related_cves property of this Erratum.
        :type related_cves: list[str]

        :param software_sources:
            The value to assign to the software_sources property of this Erratum.
        :type software_sources: list[oci.os_management.models.Id]

        :param packages:
            The value to assign to the packages property of this Erratum.
        :type packages: list[oci.os_management.models.SoftwarePackageSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'synopsis': 'str',
            'issued': 'str',
            'description': 'str',
            'updated': 'str',
            'advisory_type': 'str',
            '_from': 'str',
            'solution': 'str',
            'references': 'str',
            'affected_instances': 'list[Id]',
            'related_cves': 'list[str]',
            'software_sources': 'list[Id]',
            'packages': 'list[SoftwarePackageSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'synopsis': 'synopsis',
            'issued': 'issued',
            'description': 'description',
            'updated': 'updated',
            'advisory_type': 'advisoryType',
            '_from': 'from',
            'solution': 'solution',
            'references': 'references',
            'affected_instances': 'affectedInstances',
            'related_cves': 'relatedCves',
            'software_sources': 'softwareSources',
            'packages': 'packages'
        }

        self._name = None
        self._id = None
        self._compartment_id = None
        self._synopsis = None
        self._issued = None
        self._description = None
        self._updated = None
        self._advisory_type = None
        self.__from = None
        self._solution = None
        self._references = None
        self._affected_instances = None
        self._related_cves = None
        self._software_sources = None
        self._packages = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Erratum.
        Advisory name


        :return: The name of this Erratum.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Erratum.
        Advisory name


        :param name: The name of this Erratum.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Erratum.
        OCID for the Erratum.


        :return: The id of this Erratum.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Erratum.
        OCID for the Erratum.


        :param id: The id of this Erratum.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Erratum.
        OCID for the Compartment.


        :return: The compartment_id of this Erratum.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Erratum.
        OCID for the Compartment.


        :param compartment_id: The compartment_id of this Erratum.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def synopsis(self):
        """
        Gets the synopsis of this Erratum.
        Summary description of the erratum.


        :return: The synopsis of this Erratum.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """
        Sets the synopsis of this Erratum.
        Summary description of the erratum.


        :param synopsis: The synopsis of this Erratum.
        :type: str
        """
        self._synopsis = synopsis

    @property
    def issued(self):
        """
        Gets the issued of this Erratum.
        date the erratum was issued


        :return: The issued of this Erratum.
        :rtype: str
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """
        Sets the issued of this Erratum.
        date the erratum was issued


        :param issued: The issued of this Erratum.
        :type: str
        """
        self._issued = issued

    @property
    def description(self):
        """
        Gets the description of this Erratum.
        Details describing the erratum.


        :return: The description of this Erratum.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Erratum.
        Details describing the erratum.


        :param description: The description of this Erratum.
        :type: str
        """
        self._description = description

    @property
    def updated(self):
        """
        Gets the updated of this Erratum.
        most recent date the erratum was updated


        :return: The updated of this Erratum.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Erratum.
        most recent date the erratum was updated


        :param updated: The updated of this Erratum.
        :type: str
        """
        self._updated = updated

    @property
    def advisory_type(self):
        """
        Gets the advisory_type of this Erratum.
        Type of the erratum.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The advisory_type of this Erratum.
        :rtype: str
        """
        return self._advisory_type

    @advisory_type.setter
    def advisory_type(self, advisory_type):
        """
        Sets the advisory_type of this Erratum.
        Type of the erratum.


        :param advisory_type: The advisory_type of this Erratum.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(advisory_type, allowed_values):
            advisory_type = 'UNKNOWN_ENUM_VALUE'
        self._advisory_type = advisory_type

    @property
    def _from(self):
        """
        Gets the _from of this Erratum.
        Information specifying from where the erratum was release.


        :return: The _from of this Erratum.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this Erratum.
        Information specifying from where the erratum was release.


        :param _from: The _from of this Erratum.
        :type: str
        """
        self.__from = _from

    @property
    def solution(self):
        """
        Gets the solution of this Erratum.
        Information describing how the erratum can be resolved.


        :return: The solution of this Erratum.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """
        Sets the solution of this Erratum.
        Information describing how the erratum can be resolved.


        :param solution: The solution of this Erratum.
        :type: str
        """
        self._solution = solution

    @property
    def references(self):
        """
        Gets the references of this Erratum.
        Information describing how to find more information about the erratum.


        :return: The references of this Erratum.
        :rtype: str
        """
        return self._references

    @references.setter
    def references(self, references):
        """
        Sets the references of this Erratum.
        Information describing how to find more information about the erratum.


        :param references: The references of this Erratum.
        :type: str
        """
        self._references = references

    @property
    def affected_instances(self):
        """
        Gets the affected_instances of this Erratum.
        list of managed instances  to this erratum


        :return: The affected_instances of this Erratum.
        :rtype: list[oci.os_management.models.Id]
        """
        return self._affected_instances

    @affected_instances.setter
    def affected_instances(self, affected_instances):
        """
        Sets the affected_instances of this Erratum.
        list of managed instances  to this erratum


        :param affected_instances: The affected_instances of this Erratum.
        :type: list[oci.os_management.models.Id]
        """
        self._affected_instances = affected_instances

    @property
    def related_cves(self):
        """
        Gets the related_cves of this Erratum.
        list of CVEs applicable to this erratum


        :return: The related_cves of this Erratum.
        :rtype: list[str]
        """
        return self._related_cves

    @related_cves.setter
    def related_cves(self, related_cves):
        """
        Sets the related_cves of this Erratum.
        list of CVEs applicable to this erratum


        :param related_cves: The related_cves of this Erratum.
        :type: list[str]
        """
        self._related_cves = related_cves

    @property
    def software_sources(self):
        """
        Gets the software_sources of this Erratum.
        list of Software Sources


        :return: The software_sources of this Erratum.
        :rtype: list[oci.os_management.models.Id]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this Erratum.
        list of Software Sources


        :param software_sources: The software_sources of this Erratum.
        :type: list[oci.os_management.models.Id]
        """
        self._software_sources = software_sources

    @property
    def packages(self):
        """
        Gets the packages of this Erratum.
        list of Packages affected by this erratum


        :return: The packages of this Erratum.
        :rtype: list[oci.os_management.models.SoftwarePackageSummary]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this Erratum.
        list of Packages affected by this erratum


        :param packages: The packages of this Erratum.
        :type: list[oci.os_management.models.SoftwarePackageSummary]
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
