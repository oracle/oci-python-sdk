# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ErratumSummary(object):
    """
    Important changes for software. This can include security advisories, bug fixes, or enhancements.
    """

    #: A constant which can be used with the advisory_type property of a ErratumSummary.
    #: This constant has a value of "SECURITY"
    ADVISORY_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the advisory_type property of a ErratumSummary.
    #: This constant has a value of "BUG"
    ADVISORY_TYPE_BUG = "BUG"

    #: A constant which can be used with the advisory_type property of a ErratumSummary.
    #: This constant has a value of "ENHANCEMENT"
    ADVISORY_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the advisory_type property of a ErratumSummary.
    #: This constant has a value of "OTHER"
    ADVISORY_TYPE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new ErratumSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ErratumSummary.
        :type name: str

        :param id:
            The value to assign to the id property of this ErratumSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ErratumSummary.
        :type compartment_id: str

        :param synopsis:
            The value to assign to the synopsis property of this ErratumSummary.
        :type synopsis: str

        :param issued:
            The value to assign to the issued property of this ErratumSummary.
        :type issued: str

        :param updated:
            The value to assign to the updated property of this ErratumSummary.
        :type updated: str

        :param advisory_type:
            The value to assign to the advisory_type property of this ErratumSummary.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER"
        :type advisory_type: str

        :param related_cves:
            The value to assign to the related_cves property of this ErratumSummary.
        :type related_cves: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'synopsis': 'str',
            'issued': 'str',
            'updated': 'str',
            'advisory_type': 'str',
            'related_cves': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'synopsis': 'synopsis',
            'issued': 'issued',
            'updated': 'updated',
            'advisory_type': 'advisoryType',
            'related_cves': 'relatedCves'
        }

        self._name = None
        self._id = None
        self._compartment_id = None
        self._synopsis = None
        self._issued = None
        self._updated = None
        self._advisory_type = None
        self._related_cves = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ErratumSummary.
        Advisory name


        :return: The name of this ErratumSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ErratumSummary.
        Advisory name


        :param name: The name of this ErratumSummary.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ErratumSummary.
        OCID for the Erratum.


        :return: The id of this ErratumSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ErratumSummary.
        OCID for the Erratum.


        :param id: The id of this ErratumSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ErratumSummary.
        OCID for the Compartment.


        :return: The compartment_id of this ErratumSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ErratumSummary.
        OCID for the Compartment.


        :param compartment_id: The compartment_id of this ErratumSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def synopsis(self):
        """
        Gets the synopsis of this ErratumSummary.
        Summary description of the erratum.


        :return: The synopsis of this ErratumSummary.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """
        Sets the synopsis of this ErratumSummary.
        Summary description of the erratum.


        :param synopsis: The synopsis of this ErratumSummary.
        :type: str
        """
        self._synopsis = synopsis

    @property
    def issued(self):
        """
        Gets the issued of this ErratumSummary.
        date the erratum was issued


        :return: The issued of this ErratumSummary.
        :rtype: str
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """
        Sets the issued of this ErratumSummary.
        date the erratum was issued


        :param issued: The issued of this ErratumSummary.
        :type: str
        """
        self._issued = issued

    @property
    def updated(self):
        """
        Gets the updated of this ErratumSummary.
        most recent date the erratum was updated


        :return: The updated of this ErratumSummary.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this ErratumSummary.
        most recent date the erratum was updated


        :param updated: The updated of this ErratumSummary.
        :type: str
        """
        self._updated = updated

    @property
    def advisory_type(self):
        """
        Gets the advisory_type of this ErratumSummary.
        Type of the erratum.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER"


        :return: The advisory_type of this ErratumSummary.
        :rtype: str
        """
        return self._advisory_type

    @advisory_type.setter
    def advisory_type(self, advisory_type):
        """
        Sets the advisory_type of this ErratumSummary.
        Type of the erratum.


        :param advisory_type: The advisory_type of this ErratumSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(advisory_type, allowed_values):
            raise ValueError(
                "Invalid value for `advisory_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._advisory_type = advisory_type

    @property
    def related_cves(self):
        """
        Gets the related_cves of this ErratumSummary.
        list of CVEs applicable to this erratum


        :return: The related_cves of this ErratumSummary.
        :rtype: list[str]
        """
        return self._related_cves

    @related_cves.setter
    def related_cves(self, related_cves):
        """
        Sets the related_cves of this ErratumSummary.
        list of CVEs applicable to this erratum


        :param related_cves: The related_cves of this ErratumSummary.
        :type: list[str]
        """
        self._related_cves = related_cves

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
