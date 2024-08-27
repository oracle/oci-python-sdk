# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HsmCluster(object):
    """
    Dedicated KMS-HSM Cluster Management
    """

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "INITIALIZATION_REQUIRED"
    LIFECYCLE_STATE_INITIALIZATION_REQUIRED = "INITIALIZATION_REQUIRED"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "INITIALIZING"
    LIFECYCLE_STATE_INITIALIZING = "INITIALIZING"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "ACTIVATION_REQUIRED"
    LIFECYCLE_STATE_ACTIVATION_REQUIRED = "ACTIVATION_REQUIRED"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "PENDING_DELETION"
    LIFECYCLE_STATE_PENDING_DELETION = "PENDING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "SCHEDULING_DELETION"
    LIFECYCLE_STATE_SCHEDULING_DELETION = "SCHEDULING_DELETION"

    #: A constant which can be used with the lifecycle_state property of a HsmCluster.
    #: This constant has a value of "CANCELLING_DELETION"
    LIFECYCLE_STATE_CANCELLING_DELETION = "CANCELLING_DELETION"

    def __init__(self, **kwargs):
        """
        Initializes a new HsmCluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HsmCluster.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HsmCluster.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this HsmCluster.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this HsmCluster.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HsmCluster.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HsmCluster.
            Allowed values for this property are: "CREATING", "INITIALIZATION_REQUIRED", "INITIALIZING", "ACTIVATION_REQUIRED", "ACTIVATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param dns_name:
            The value to assign to the dns_name property of this HsmCluster.
        :type dns_name: str

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this HsmCluster.
        :type time_of_deletion: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this HsmCluster.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HsmCluster.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'dns_name': 'str',
            'time_of_deletion': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'dns_name': 'dnsName',
            'time_of_deletion': 'timeOfDeletion',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._dns_name = None
        self._time_of_deletion = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HsmCluster.
        The OCID of the HSMCluster resource.


        :return: The id of this HsmCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HsmCluster.
        The OCID of the HSMCluster resource.


        :param id: The id of this HsmCluster.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HsmCluster.
        The OCID of the compartment that contains this HSMCluster resource.


        :return: The compartment_id of this HsmCluster.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HsmCluster.
        The OCID of the compartment that contains this HSMCluster resource.


        :param compartment_id: The compartment_id of this HsmCluster.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this HsmCluster.
        A user-friendly display name for the HSMCluster resource. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this HsmCluster.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this HsmCluster.
        A user-friendly display name for the HSMCluster resource. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this HsmCluster.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this HsmCluster.
        The date and time this HSM resource was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2023-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this HsmCluster.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HsmCluster.
        The date and time this HSM resource was created, expressed in `RFC 3339`__ timestamp format.

        Example: `2023-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this HsmCluster.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this HsmCluster.
        The date and time this HSM resource was updated, expressed in `RFC 3339`__ timestamp format.

        Example: `2023-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this HsmCluster.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HsmCluster.
        The date and time this HSM resource was updated, expressed in `RFC 3339`__ timestamp format.

        Example: `2023-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this HsmCluster.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this HsmCluster.
        The HSMCluster's current state.

        Example: `ACTIVE`

        Allowed values for this property are: "CREATING", "INITIALIZATION_REQUIRED", "INITIALIZING", "ACTIVATION_REQUIRED", "ACTIVATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this HsmCluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HsmCluster.
        The HSMCluster's current state.

        Example: `ACTIVE`


        :param lifecycle_state: The lifecycle_state of this HsmCluster.
        :type: str
        """
        allowed_values = ["CREATING", "INITIALIZATION_REQUIRED", "INITIALIZING", "ACTIVATION_REQUIRED", "ACTIVATING", "ACTIVE", "DELETING", "DELETED", "PENDING_DELETION", "SCHEDULING_DELETION", "CANCELLING_DELETION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def dns_name(self):
        """
        **[Required]** Gets the dns_name of this HsmCluster.
        DNS name for the HSM Cluster -- this will contain information about the region as well.


        :return: The dns_name of this HsmCluster.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """
        Sets the dns_name of this HsmCluster.
        DNS name for the HSM Cluster -- this will contain information about the region as well.


        :param dns_name: The dns_name of this HsmCluster.
        :type: str
        """
        self._dns_name = dns_name

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this HsmCluster.
        An optional property indicating when to delete the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this HsmCluster.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this HsmCluster.
        An optional property indicating when to delete the key, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this HsmCluster.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this HsmCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this HsmCluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this HsmCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this HsmCluster.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this HsmCluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this HsmCluster.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this HsmCluster.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this HsmCluster.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
