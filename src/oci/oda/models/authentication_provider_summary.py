# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationProviderSummary(object):
    """
    Summary of the Authentication Provider.
    """

    #: A constant which can be used with the grant_type property of a AuthenticationProviderSummary.
    #: This constant has a value of "CLIENT_CREDENTIALS"
    GRANT_TYPE_CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"

    #: A constant which can be used with the grant_type property of a AuthenticationProviderSummary.
    #: This constant has a value of "AUTHORIZATION_CODE"
    GRANT_TYPE_AUTHORIZATION_CODE = "AUTHORIZATION_CODE"

    #: A constant which can be used with the identity_provider property of a AuthenticationProviderSummary.
    #: This constant has a value of "GENERIC"
    IDENTITY_PROVIDER_GENERIC = "GENERIC"

    #: A constant which can be used with the identity_provider property of a AuthenticationProviderSummary.
    #: This constant has a value of "OAM"
    IDENTITY_PROVIDER_OAM = "OAM"

    #: A constant which can be used with the identity_provider property of a AuthenticationProviderSummary.
    #: This constant has a value of "GOOGLE"
    IDENTITY_PROVIDER_GOOGLE = "GOOGLE"

    #: A constant which can be used with the identity_provider property of a AuthenticationProviderSummary.
    #: This constant has a value of "MICROSOFT"
    IDENTITY_PROVIDER_MICROSOFT = "MICROSOFT"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AuthenticationProviderSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationProviderSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AuthenticationProviderSummary.
        :type id: str

        :param grant_type:
            The value to assign to the grant_type property of this AuthenticationProviderSummary.
            Allowed values for this property are: "CLIENT_CREDENTIALS", "AUTHORIZATION_CODE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type grant_type: str

        :param identity_provider:
            The value to assign to the identity_provider property of this AuthenticationProviderSummary.
            Allowed values for this property are: "GENERIC", "OAM", "GOOGLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type identity_provider: str

        :param name:
            The value to assign to the name property of this AuthenticationProviderSummary.
        :type name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AuthenticationProviderSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AuthenticationProviderSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AuthenticationProviderSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AuthenticationProviderSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AuthenticationProviderSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'grant_type': 'str',
            'identity_provider': 'str',
            'name': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'grant_type': 'grantType',
            'identity_provider': 'identityProvider',
            'name': 'name',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._grant_type = None
        self._identity_provider = None
        self._name = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuthenticationProviderSummary.
        Unique immutable identifier that was assigned when the Authentication Provider was created.


        :return: The id of this AuthenticationProviderSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthenticationProviderSummary.
        Unique immutable identifier that was assigned when the Authentication Provider was created.


        :param id: The id of this AuthenticationProviderSummary.
        :type: str
        """
        self._id = id

    @property
    def grant_type(self):
        """
        **[Required]** Gets the grant_type of this AuthenticationProviderSummary.
        The grant type for the Authentication Provider.

        Allowed values for this property are: "CLIENT_CREDENTIALS", "AUTHORIZATION_CODE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The grant_type of this AuthenticationProviderSummary.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """
        Sets the grant_type of this AuthenticationProviderSummary.
        The grant type for the Authentication Provider.


        :param grant_type: The grant_type of this AuthenticationProviderSummary.
        :type: str
        """
        allowed_values = ["CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"]
        if not value_allowed_none_or_none_sentinel(grant_type, allowed_values):
            grant_type = 'UNKNOWN_ENUM_VALUE'
        self._grant_type = grant_type

    @property
    def identity_provider(self):
        """
        **[Required]** Gets the identity_provider of this AuthenticationProviderSummary.
        Which type of Identity Provider (IDP) you are using.

        Allowed values for this property are: "GENERIC", "OAM", "GOOGLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The identity_provider of this AuthenticationProviderSummary.
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """
        Sets the identity_provider of this AuthenticationProviderSummary.
        Which type of Identity Provider (IDP) you are using.


        :param identity_provider: The identity_provider of this AuthenticationProviderSummary.
        :type: str
        """
        allowed_values = ["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(identity_provider, allowed_values):
            identity_provider = 'UNKNOWN_ENUM_VALUE'
        self._identity_provider = identity_provider

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AuthenticationProviderSummary.
        A name to identify the Authentication Provider.


        :return: The name of this AuthenticationProviderSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthenticationProviderSummary.
        A name to identify the Authentication Provider.


        :param name: The name of this AuthenticationProviderSummary.
        :type: str
        """
        self._name = name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AuthenticationProviderSummary.
        The Authentication Provider's current state.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AuthenticationProviderSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AuthenticationProviderSummary.
        The Authentication Provider's current state.


        :param lifecycle_state: The lifecycle_state of this AuthenticationProviderSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AuthenticationProviderSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this AuthenticationProviderSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AuthenticationProviderSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this AuthenticationProviderSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AuthenticationProviderSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this AuthenticationProviderSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AuthenticationProviderSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this AuthenticationProviderSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AuthenticationProviderSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AuthenticationProviderSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AuthenticationProviderSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AuthenticationProviderSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AuthenticationProviderSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AuthenticationProviderSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AuthenticationProviderSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AuthenticationProviderSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
