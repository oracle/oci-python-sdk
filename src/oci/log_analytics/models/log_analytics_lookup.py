# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLookup(object):
    """
    LogAnalyticsLookup
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLookup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param active_edit_version:
            The value to assign to the active_edit_version property of this LogAnalyticsLookup.
        :type active_edit_version: int

        :param canonical_link:
            The value to assign to the canonical_link property of this LogAnalyticsLookup.
        :type canonical_link: str

        :param description:
            The value to assign to the description property of this LogAnalyticsLookup.
        :type description: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsLookup.
        :type edit_version: int

        :param fields:
            The value to assign to the fields property of this LogAnalyticsLookup.
        :type fields: list[LookupField]

        :param lookup_reference:
            The value to assign to the lookup_reference property of this LogAnalyticsLookup.
        :type lookup_reference: int

        :param name:
            The value to assign to the name property of this LogAnalyticsLookup.
        :type name: str

        :param is_built_in:
            The value to assign to the is_built_in property of this LogAnalyticsLookup.
        :type is_built_in: int

        :param is_hidden:
            The value to assign to the is_hidden property of this LogAnalyticsLookup.
        :type is_hidden: bool

        :param lookup_display_name:
            The value to assign to the lookup_display_name property of this LogAnalyticsLookup.
        :type lookup_display_name: str

        :param referring_sources:
            The value to assign to the referring_sources property of this LogAnalyticsLookup.
        :type referring_sources: AutoLookups

        :param status_summary:
            The value to assign to the status_summary property of this LogAnalyticsLookup.
        :type status_summary: StatusSummary

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsLookup.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'active_edit_version': 'int',
            'canonical_link': 'str',
            'description': 'str',
            'edit_version': 'int',
            'fields': 'list[LookupField]',
            'lookup_reference': 'int',
            'name': 'str',
            'is_built_in': 'int',
            'is_hidden': 'bool',
            'lookup_display_name': 'str',
            'referring_sources': 'AutoLookups',
            'status_summary': 'StatusSummary',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'active_edit_version': 'activeEditVersion',
            'canonical_link': 'canonicalLink',
            'description': 'description',
            'edit_version': 'editVersion',
            'fields': 'fields',
            'lookup_reference': 'lookupReference',
            'name': 'name',
            'is_built_in': 'isBuiltIn',
            'is_hidden': 'isHidden',
            'lookup_display_name': 'lookupDisplayName',
            'referring_sources': 'referringSources',
            'status_summary': 'statusSummary',
            'time_updated': 'timeUpdated'
        }

        self._active_edit_version = None
        self._canonical_link = None
        self._description = None
        self._edit_version = None
        self._fields = None
        self._lookup_reference = None
        self._name = None
        self._is_built_in = None
        self._is_hidden = None
        self._lookup_display_name = None
        self._referring_sources = None
        self._status_summary = None
        self._time_updated = None

    @property
    def active_edit_version(self):
        """
        Gets the active_edit_version of this LogAnalyticsLookup.
        active edit version


        :return: The active_edit_version of this LogAnalyticsLookup.
        :rtype: int
        """
        return self._active_edit_version

    @active_edit_version.setter
    def active_edit_version(self, active_edit_version):
        """
        Sets the active_edit_version of this LogAnalyticsLookup.
        active edit version


        :param active_edit_version: The active_edit_version of this LogAnalyticsLookup.
        :type: int
        """
        self._active_edit_version = active_edit_version

    @property
    def canonical_link(self):
        """
        Gets the canonical_link of this LogAnalyticsLookup.
        canonical link


        :return: The canonical_link of this LogAnalyticsLookup.
        :rtype: str
        """
        return self._canonical_link

    @canonical_link.setter
    def canonical_link(self, canonical_link):
        """
        Sets the canonical_link of this LogAnalyticsLookup.
        canonical link


        :param canonical_link: The canonical_link of this LogAnalyticsLookup.
        :type: str
        """
        self._canonical_link = canonical_link

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsLookup.
        description


        :return: The description of this LogAnalyticsLookup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsLookup.
        description


        :param description: The description of this LogAnalyticsLookup.
        :type: str
        """
        self._description = description

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsLookup.
        edit version


        :return: The edit_version of this LogAnalyticsLookup.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsLookup.
        edit version


        :param edit_version: The edit_version of this LogAnalyticsLookup.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def fields(self):
        """
        Gets the fields of this LogAnalyticsLookup.
        fields


        :return: The fields of this LogAnalyticsLookup.
        :rtype: list[LookupField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this LogAnalyticsLookup.
        fields


        :param fields: The fields of this LogAnalyticsLookup.
        :type: list[LookupField]
        """
        self._fields = fields

    @property
    def lookup_reference(self):
        """
        Gets the lookup_reference of this LogAnalyticsLookup.
        lookupReference


        :return: The lookup_reference of this LogAnalyticsLookup.
        :rtype: int
        """
        return self._lookup_reference

    @lookup_reference.setter
    def lookup_reference(self, lookup_reference):
        """
        Sets the lookup_reference of this LogAnalyticsLookup.
        lookupReference


        :param lookup_reference: The lookup_reference of this LogAnalyticsLookup.
        :type: int
        """
        self._lookup_reference = lookup_reference

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsLookup.
        iname


        :return: The name of this LogAnalyticsLookup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsLookup.
        iname


        :param name: The name of this LogAnalyticsLookup.
        :type: str
        """
        self._name = name

    @property
    def is_built_in(self):
        """
        Gets the is_built_in of this LogAnalyticsLookup.
        is built in


        :return: The is_built_in of this LogAnalyticsLookup.
        :rtype: int
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """
        Sets the is_built_in of this LogAnalyticsLookup.
        is built in


        :param is_built_in: The is_built_in of this LogAnalyticsLookup.
        :type: int
        """
        self._is_built_in = is_built_in

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this LogAnalyticsLookup.
        is hidden


        :return: The is_hidden of this LogAnalyticsLookup.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this LogAnalyticsLookup.
        is hidden


        :param is_hidden: The is_hidden of this LogAnalyticsLookup.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def lookup_display_name(self):
        """
        Gets the lookup_display_name of this LogAnalyticsLookup.
        name


        :return: The lookup_display_name of this LogAnalyticsLookup.
        :rtype: str
        """
        return self._lookup_display_name

    @lookup_display_name.setter
    def lookup_display_name(self, lookup_display_name):
        """
        Sets the lookup_display_name of this LogAnalyticsLookup.
        name


        :param lookup_display_name: The lookup_display_name of this LogAnalyticsLookup.
        :type: str
        """
        self._lookup_display_name = lookup_display_name

    @property
    def referring_sources(self):
        """
        Gets the referring_sources of this LogAnalyticsLookup.
        sources using


        :return: The referring_sources of this LogAnalyticsLookup.
        :rtype: AutoLookups
        """
        return self._referring_sources

    @referring_sources.setter
    def referring_sources(self, referring_sources):
        """
        Sets the referring_sources of this LogAnalyticsLookup.
        sources using


        :param referring_sources: The referring_sources of this LogAnalyticsLookup.
        :type: AutoLookups
        """
        self._referring_sources = referring_sources

    @property
    def status_summary(self):
        """
        Gets the status_summary of this LogAnalyticsLookup.
        status summary


        :return: The status_summary of this LogAnalyticsLookup.
        :rtype: StatusSummary
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """
        Sets the status_summary of this LogAnalyticsLookup.
        status summary


        :param status_summary: The status_summary of this LogAnalyticsLookup.
        :type: StatusSummary
        """
        self._status_summary = status_summary

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LogAnalyticsLookup.
        last updated date


        :return: The time_updated of this LogAnalyticsLookup.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsLookup.
        last updated date


        :param time_updated: The time_updated of this LogAnalyticsLookup.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
