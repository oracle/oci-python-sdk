# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachment(object):
    """
    A link between a DRG and VCN. For more information, see
    `Overview of the Networking Service`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Network/Concepts/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "ATTACHED"
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "DETACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DrgAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DrgAttachment.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this DrgAttachment.
        :type drg_id: str

        :param id:
            The value to assign to the id property of this DrgAttachment.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrgAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param route_table_id:
            The value to assign to the route_table_id property of this DrgAttachment.
        :type route_table_id: str

        :param time_created:
            The value to assign to the time_created property of this DrgAttachment.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this DrgAttachment.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'route_table_id': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'route_table_id': 'routeTableId',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._lifecycle_state = None
        self._route_table_id = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrgAttachment.
        The OCID of the compartment containing the DRG attachment.


        :return: The compartment_id of this DrgAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrgAttachment.
        The OCID of the compartment containing the DRG attachment.


        :param compartment_id: The compartment_id of this DrgAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DrgAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DrgAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this DrgAttachment.
        The OCID of the DRG.


        :return: The drg_id of this DrgAttachment.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this DrgAttachment.
        The OCID of the DRG.


        :param drg_id: The drg_id of this DrgAttachment.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (OCID).


        :return: The id of this DrgAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (OCID).


        :param id: The id of this DrgAttachment.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DrgAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.


        :param lifecycle_state: The lifecycle_state of this DrgAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this DrgAttachment.
        The OCID of the route table the DRG attachment is using.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this DrgAttachment.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this DrgAttachment.
        The OCID of the route table the DRG attachment is using.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this DrgAttachment.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DrgAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DrgAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DrgAttachment.
        The OCID of the VCN.


        :return: The vcn_id of this DrgAttachment.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DrgAttachment.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this DrgAttachment.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
