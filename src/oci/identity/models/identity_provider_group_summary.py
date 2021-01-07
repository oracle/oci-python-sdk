# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityProviderGroupSummary(object):
    """
    A group created in an identity provider that can be mapped to a group in OCI
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityProviderGroupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IdentityProviderGroupSummary.
        :type id: str

        :param identity_provider_id:
            The value to assign to the identity_provider_id property of this IdentityProviderGroupSummary.
        :type identity_provider_id: str

        :param display_name:
            The value to assign to the display_name property of this IdentityProviderGroupSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this IdentityProviderGroupSummary.
        :type name: str

        :param external_identifier:
            The value to assign to the external_identifier property of this IdentityProviderGroupSummary.
        :type external_identifier: str

        :param time_created:
            The value to assign to the time_created property of this IdentityProviderGroupSummary.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this IdentityProviderGroupSummary.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'identity_provider_id': 'str',
            'display_name': 'str',
            'name': 'str',
            'external_identifier': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'identity_provider_id': 'identityProviderId',
            'display_name': 'displayName',
            'name': 'name',
            'external_identifier': 'externalIdentifier',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified'
        }

        self._id = None
        self._identity_provider_id = None
        self._display_name = None
        self._name = None
        self._external_identifier = None
        self._time_created = None
        self._time_modified = None

    @property
    def id(self):
        """
        Gets the id of this IdentityProviderGroupSummary.
        The OCID of the `IdentityProviderGroup`.


        :return: The id of this IdentityProviderGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdentityProviderGroupSummary.
        The OCID of the `IdentityProviderGroup`.


        :param id: The id of this IdentityProviderGroupSummary.
        :type: str
        """
        self._id = id

    @property
    def identity_provider_id(self):
        """
        Gets the identity_provider_id of this IdentityProviderGroupSummary.
        The OCID of the `IdentityProvider` this group belongs to.


        :return: The identity_provider_id of this IdentityProviderGroupSummary.
        :rtype: str
        """
        return self._identity_provider_id

    @identity_provider_id.setter
    def identity_provider_id(self, identity_provider_id):
        """
        Sets the identity_provider_id of this IdentityProviderGroupSummary.
        The OCID of the `IdentityProvider` this group belongs to.


        :param identity_provider_id: The identity_provider_id of this IdentityProviderGroupSummary.
        :type: str
        """
        self._identity_provider_id = identity_provider_id

    @property
    def display_name(self):
        """
        Gets the display_name of this IdentityProviderGroupSummary.
        Display name of the group


        :return: The display_name of this IdentityProviderGroupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IdentityProviderGroupSummary.
        Display name of the group


        :param display_name: The display_name of this IdentityProviderGroupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this IdentityProviderGroupSummary.
        Display name of the group


        :return: The name of this IdentityProviderGroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IdentityProviderGroupSummary.
        Display name of the group


        :param name: The name of this IdentityProviderGroupSummary.
        :type: str
        """
        self._name = name

    @property
    def external_identifier(self):
        """
        Gets the external_identifier of this IdentityProviderGroupSummary.
        Identifier of the group in the identity provider


        :return: The external_identifier of this IdentityProviderGroupSummary.
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """
        Sets the external_identifier of this IdentityProviderGroupSummary.
        Identifier of the group in the identity provider


        :param external_identifier: The external_identifier of this IdentityProviderGroupSummary.
        :type: str
        """
        self._external_identifier = external_identifier

    @property
    def time_created(self):
        """
        Gets the time_created of this IdentityProviderGroupSummary.
        Date and time the `IdentityProviderGroup` was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IdentityProviderGroupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IdentityProviderGroupSummary.
        Date and time the `IdentityProviderGroup` was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IdentityProviderGroupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this IdentityProviderGroupSummary.
        Date and time the `IdentityProviderGroup` was last modified, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_modified of this IdentityProviderGroupSummary.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this IdentityProviderGroupSummary.
        Date and time the `IdentityProviderGroup` was last modified, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_modified: The time_modified of this IdentityProviderGroupSummary.
        :type: datetime
        """
        self._time_modified = time_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
