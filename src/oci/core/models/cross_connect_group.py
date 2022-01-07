# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnectGroup(object):
    """
    For use with Oracle Cloud Infrastructure FastConnect. A cross-connect group
    is a link aggregation group (LAG), which can contain one or more
    :class:`CrossConnect`. Customers who are colocated with
    Oracle in a FastConnect location create and use cross-connect groups. For more
    information, see `FastConnect Overview`__.

    **Note:** If you're a provider who is setting up a physical connection to Oracle so customers
    can use FastConnect over the connection, be aware that your connection is modeled the
    same way as a colocated customer's (with `CrossConnect` and `CrossConnectGroup` objects, and so on).

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "PROVISIONED"
    LIFECYCLE_STATE_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CrossConnectGroup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnectGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CrossConnectGroup.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CrossConnectGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CrossConnectGroup.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CrossConnectGroup.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this CrossConnectGroup.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CrossConnectGroup.
            Allowed values for this property are: "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this CrossConnectGroup.
        :type customer_reference_name: str

        :param time_created:
            The value to assign to the time_created property of this CrossConnectGroup.
        :type time_created: datetime

        :param macsec_properties:
            The value to assign to the macsec_properties property of this CrossConnectGroup.
        :type macsec_properties: oci.core.models.MacsecProperties

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'customer_reference_name': 'str',
            'time_created': 'datetime',
            'macsec_properties': 'MacsecProperties'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'customer_reference_name': 'customerReferenceName',
            'time_created': 'timeCreated',
            'macsec_properties': 'macsecProperties'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._customer_reference_name = None
        self._time_created = None
        self._macsec_properties = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CrossConnectGroup.
        The `OCID`__ of the compartment containing the cross-connect group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CrossConnectGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CrossConnectGroup.
        The `OCID`__ of the compartment containing the cross-connect group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CrossConnectGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CrossConnectGroup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CrossConnectGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CrossConnectGroup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CrossConnectGroup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CrossConnectGroup.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CrossConnectGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CrossConnectGroup.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CrossConnectGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CrossConnectGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CrossConnectGroup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CrossConnectGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CrossConnectGroup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        Gets the id of this CrossConnectGroup.
        The cross-connect group's Oracle ID (OCID).


        :return: The id of this CrossConnectGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossConnectGroup.
        The cross-connect group's Oracle ID (OCID).


        :param id: The id of this CrossConnectGroup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CrossConnectGroup.
        The cross-connect group's current state.

        Allowed values for this property are: "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CrossConnectGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CrossConnectGroup.
        The cross-connect group's current state.


        :param lifecycle_state: The lifecycle_state of this CrossConnectGroup.
        :type: str
        """
        allowed_values = ["PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this CrossConnectGroup.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :return: The customer_reference_name of this CrossConnectGroup.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this CrossConnectGroup.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :param customer_reference_name: The customer_reference_name of this CrossConnectGroup.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CrossConnectGroup.
        The date and time the cross-connect group was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CrossConnectGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CrossConnectGroup.
        The date and time the cross-connect group was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CrossConnectGroup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def macsec_properties(self):
        """
        Gets the macsec_properties of this CrossConnectGroup.

        :return: The macsec_properties of this CrossConnectGroup.
        :rtype: oci.core.models.MacsecProperties
        """
        return self._macsec_properties

    @macsec_properties.setter
    def macsec_properties(self, macsec_properties):
        """
        Sets the macsec_properties of this CrossConnectGroup.

        :param macsec_properties: The macsec_properties of this CrossConnectGroup.
        :type: oci.core.models.MacsecProperties
        """
        self._macsec_properties = macsec_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
