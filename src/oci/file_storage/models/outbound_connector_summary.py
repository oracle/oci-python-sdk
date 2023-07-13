# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutboundConnectorSummary(object):
    """
    Summary information for an outbound connector.
    """

    #: A constant which can be used with the lifecycle_state property of a OutboundConnectorSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnectorSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnectorSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OutboundConnectorSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new OutboundConnectorSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.file_storage.models.LdapBindAccountSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this OutboundConnectorSummary.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OutboundConnectorSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this OutboundConnectorSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OutboundConnectorSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this OutboundConnectorSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this OutboundConnectorSummary.
        :type time_created: datetime

        :param connector_type:
            The value to assign to the connector_type property of this OutboundConnectorSummary.
        :type connector_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OutboundConnectorSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OutboundConnectorSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'connector_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'connector_type': 'connectorType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._id = None
        self._lifecycle_state = None
        self._display_name = None
        self._time_created = None
        self._connector_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'LDAPBIND':
            return 'LdapBindAccountSummary'
        else:
            return 'OutboundConnectorSummary'

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this OutboundConnectorSummary.
        The availability domain the outbound connector is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this OutboundConnectorSummary.
        The availability domain the outbound connector is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this OutboundConnectorSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OutboundConnectorSummary.
        The `OCID`__ of the compartment that contains the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OutboundConnectorSummary.
        The `OCID`__ of the compartment that contains the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OutboundConnectorSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OutboundConnectorSummary.
        The `OCID`__ of the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OutboundConnectorSummary.
        The `OCID`__ of the outbound connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this OutboundConnectorSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OutboundConnectorSummary.
        The current state of this outbound connector.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OutboundConnectorSummary.
        The current state of this outbound connector.


        :param lifecycle_state: The lifecycle_state of this OutboundConnectorSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OutboundConnectorSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My outbound connector`


        :return: The display_name of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OutboundConnectorSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My outbound connector`


        :param display_name: The display_name of this OutboundConnectorSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OutboundConnectorSummary.
        The date and time the outbound connector was created
        in `RFC 3339`__ timestamp format.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OutboundConnectorSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OutboundConnectorSummary.
        The date and time the outbound connector was created
        in `RFC 3339`__ timestamp format.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OutboundConnectorSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this OutboundConnectorSummary.
        The account type of this outbound connector.


        :return: The connector_type of this OutboundConnectorSummary.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this OutboundConnectorSummary.
        The account type of this outbound connector.


        :param connector_type: The connector_type of this OutboundConnectorSummary.
        :type: str
        """
        self._connector_type = connector_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OutboundConnectorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this OutboundConnectorSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OutboundConnectorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this OutboundConnectorSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OutboundConnectorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this OutboundConnectorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OutboundConnectorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this OutboundConnectorSummary.
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
