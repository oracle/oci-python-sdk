# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCrossConnectDetails(object):
    """
    CreateCrossConnectDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCrossConnectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCrossConnectDetails.
        :type compartment_id: str

        :param cross_connect_group_id:
            The value to assign to the cross_connect_group_id property of this CreateCrossConnectDetails.
        :type cross_connect_group_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCrossConnectDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateCrossConnectDetails.
        :type display_name: str

        :param far_cross_connect_or_cross_connect_group_id:
            The value to assign to the far_cross_connect_or_cross_connect_group_id property of this CreateCrossConnectDetails.
        :type far_cross_connect_or_cross_connect_group_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCrossConnectDetails.
        :type freeform_tags: dict(str, str)

        :param location_name:
            The value to assign to the location_name property of this CreateCrossConnectDetails.
        :type location_name: str

        :param near_cross_connect_or_cross_connect_group_id:
            The value to assign to the near_cross_connect_or_cross_connect_group_id property of this CreateCrossConnectDetails.
        :type near_cross_connect_or_cross_connect_group_id: str

        :param port_speed_shape_name:
            The value to assign to the port_speed_shape_name property of this CreateCrossConnectDetails.
        :type port_speed_shape_name: str

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this CreateCrossConnectDetails.
        :type customer_reference_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cross_connect_group_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'far_cross_connect_or_cross_connect_group_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'location_name': 'str',
            'near_cross_connect_or_cross_connect_group_id': 'str',
            'port_speed_shape_name': 'str',
            'customer_reference_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cross_connect_group_id': 'crossConnectGroupId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'far_cross_connect_or_cross_connect_group_id': 'farCrossConnectOrCrossConnectGroupId',
            'freeform_tags': 'freeformTags',
            'location_name': 'locationName',
            'near_cross_connect_or_cross_connect_group_id': 'nearCrossConnectOrCrossConnectGroupId',
            'port_speed_shape_name': 'portSpeedShapeName',
            'customer_reference_name': 'customerReferenceName'
        }

        self._compartment_id = None
        self._cross_connect_group_id = None
        self._defined_tags = None
        self._display_name = None
        self._far_cross_connect_or_cross_connect_group_id = None
        self._freeform_tags = None
        self._location_name = None
        self._near_cross_connect_or_cross_connect_group_id = None
        self._port_speed_shape_name = None
        self._customer_reference_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCrossConnectDetails.
        The OCID of the compartment to contain the cross-connect.


        :return: The compartment_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCrossConnectDetails.
        The OCID of the compartment to contain the cross-connect.


        :param compartment_id: The compartment_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_group_id(self):
        """
        Gets the cross_connect_group_id of this CreateCrossConnectDetails.
        The OCID of the cross-connect group to put this cross-connect in.


        :return: The cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._cross_connect_group_id

    @cross_connect_group_id.setter
    def cross_connect_group_id(self, cross_connect_group_id):
        """
        Sets the cross_connect_group_id of this CreateCrossConnectDetails.
        The OCID of the cross-connect group to put this cross-connect in.


        :param cross_connect_group_id: The cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._cross_connect_group_id = cross_connect_group_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCrossConnectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCrossConnectDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCrossConnectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCrossConnectDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def far_cross_connect_or_cross_connect_group_id(self):
        """
        Gets the far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on a different router (for the
        purposes of redundancy), provide the OCID of that existing cross-connect or
        cross-connect group.


        :return: The far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._far_cross_connect_or_cross_connect_group_id

    @far_cross_connect_or_cross_connect_group_id.setter
    def far_cross_connect_or_cross_connect_group_id(self, far_cross_connect_or_cross_connect_group_id):
        """
        Sets the far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on a different router (for the
        purposes of redundancy), provide the OCID of that existing cross-connect or
        cross-connect group.


        :param far_cross_connect_or_cross_connect_group_id: The far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._far_cross_connect_or_cross_connect_group_id = far_cross_connect_or_cross_connect_group_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCrossConnectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCrossConnectDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCrossConnectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCrossConnectDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def location_name(self):
        """
        **[Required]** Gets the location_name of this CreateCrossConnectDetails.
        The name of the FastConnect location where this cross-connect will be installed.
        To get a list of the available locations, see
        :func:`list_cross_connect_locations`.

        Example: `CyrusOne, Chandler, AZ`


        :return: The location_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this CreateCrossConnectDetails.
        The name of the FastConnect location where this cross-connect will be installed.
        To get a list of the available locations, see
        :func:`list_cross_connect_locations`.

        Example: `CyrusOne, Chandler, AZ`


        :param location_name: The location_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._location_name = location_name

    @property
    def near_cross_connect_or_cross_connect_group_id(self):
        """
        Gets the near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on the same router, provide the
        OCID of that existing cross-connect or cross-connect group.


        :return: The near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._near_cross_connect_or_cross_connect_group_id

    @near_cross_connect_or_cross_connect_group_id.setter
    def near_cross_connect_or_cross_connect_group_id(self, near_cross_connect_or_cross_connect_group_id):
        """
        Sets the near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on the same router, provide the
        OCID of that existing cross-connect or cross-connect group.


        :param near_cross_connect_or_cross_connect_group_id: The near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._near_cross_connect_or_cross_connect_group_id = near_cross_connect_or_cross_connect_group_id

    @property
    def port_speed_shape_name(self):
        """
        **[Required]** Gets the port_speed_shape_name of this CreateCrossConnectDetails.
        The port speed for this cross-connect. To get a list of the available port speeds, see
        :func:`list_crossconnect_port_speed_shapes`.

        Example: `10 Gbps`


        :return: The port_speed_shape_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._port_speed_shape_name

    @port_speed_shape_name.setter
    def port_speed_shape_name(self, port_speed_shape_name):
        """
        Sets the port_speed_shape_name of this CreateCrossConnectDetails.
        The port speed for this cross-connect. To get a list of the available port speeds, see
        :func:`list_crossconnect_port_speed_shapes`.

        Example: `10 Gbps`


        :param port_speed_shape_name: The port_speed_shape_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._port_speed_shape_name = port_speed_shape_name

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this CreateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        uses.


        :return: The customer_reference_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this CreateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        uses.


        :param customer_reference_name: The customer_reference_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
