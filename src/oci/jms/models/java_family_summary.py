# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaFamilySummary(object):
    """
    A summary of the Java release family information.
    """

    #: A constant which can be used with the support_type property of a JavaFamilySummary.
    #: This constant has a value of "LTS"
    SUPPORT_TYPE_LTS = "LTS"

    #: A constant which can be used with the support_type property of a JavaFamilySummary.
    #: This constant has a value of "NON_LTS"
    SUPPORT_TYPE_NON_LTS = "NON_LTS"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaFamilySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param family_version:
            The value to assign to the family_version property of this JavaFamilySummary.
        :type family_version: str

        :param display_name:
            The value to assign to the display_name property of this JavaFamilySummary.
        :type display_name: str

        :param support_type:
            The value to assign to the support_type property of this JavaFamilySummary.
            Allowed values for this property are: "LTS", "NON_LTS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type support_type: str

        :param end_of_support_life_date:
            The value to assign to the end_of_support_life_date property of this JavaFamilySummary.
        :type end_of_support_life_date: datetime

        :param doc_url:
            The value to assign to the doc_url property of this JavaFamilySummary.
        :type doc_url: str

        """
        self.swagger_types = {
            'family_version': 'str',
            'display_name': 'str',
            'support_type': 'str',
            'end_of_support_life_date': 'datetime',
            'doc_url': 'str'
        }

        self.attribute_map = {
            'family_version': 'familyVersion',
            'display_name': 'displayName',
            'support_type': 'supportType',
            'end_of_support_life_date': 'endOfSupportLifeDate',
            'doc_url': 'docUrl'
        }

        self._family_version = None
        self._display_name = None
        self._support_type = None
        self._end_of_support_life_date = None
        self._doc_url = None

    @property
    def family_version(self):
        """
        **[Required]** Gets the family_version of this JavaFamilySummary.
        The Java release family identifier.


        :return: The family_version of this JavaFamilySummary.
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """
        Sets the family_version of this JavaFamilySummary.
        The Java release family identifier.


        :param family_version: The family_version of this JavaFamilySummary.
        :type: str
        """
        self._family_version = family_version

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this JavaFamilySummary.
        The display name of the release family.


        :return: The display_name of this JavaFamilySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JavaFamilySummary.
        The display name of the release family.


        :param display_name: The display_name of this JavaFamilySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def support_type(self):
        """
        **[Required]** Gets the support_type of this JavaFamilySummary.
        This indicates the support category for the Java release family.

        Allowed values for this property are: "LTS", "NON_LTS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The support_type of this JavaFamilySummary.
        :rtype: str
        """
        return self._support_type

    @support_type.setter
    def support_type(self, support_type):
        """
        Sets the support_type of this JavaFamilySummary.
        This indicates the support category for the Java release family.


        :param support_type: The support_type of this JavaFamilySummary.
        :type: str
        """
        allowed_values = ["LTS", "NON_LTS"]
        if not value_allowed_none_or_none_sentinel(support_type, allowed_values):
            support_type = 'UNKNOWN_ENUM_VALUE'
        self._support_type = support_type

    @property
    def end_of_support_life_date(self):
        """
        **[Required]** Gets the end_of_support_life_date of this JavaFamilySummary.
        The End of Support Life (EOSL) date of the Java release family (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The end_of_support_life_date of this JavaFamilySummary.
        :rtype: datetime
        """
        return self._end_of_support_life_date

    @end_of_support_life_date.setter
    def end_of_support_life_date(self, end_of_support_life_date):
        """
        Sets the end_of_support_life_date of this JavaFamilySummary.
        The End of Support Life (EOSL) date of the Java release family (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param end_of_support_life_date: The end_of_support_life_date of this JavaFamilySummary.
        :type: datetime
        """
        self._end_of_support_life_date = end_of_support_life_date

    @property
    def doc_url(self):
        """
        **[Required]** Gets the doc_url of this JavaFamilySummary.
        Link to access the documentation for the release.


        :return: The doc_url of this JavaFamilySummary.
        :rtype: str
        """
        return self._doc_url

    @doc_url.setter
    def doc_url(self, doc_url):
        """
        Sets the doc_url of this JavaFamilySummary.
        Link to access the documentation for the release.


        :param doc_url: The doc_url of this JavaFamilySummary.
        :type: str
        """
        self._doc_url = doc_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
