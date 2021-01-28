# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cpe(object):
    """
    An object you create when setting up an IPSec VPN between your on-premises network
    and VCN. The `Cpe` is a virtual representation of your customer-premises equipment,
    which is the actual router on-premises at your site at your end of the IPSec VPN connection.
    For more information,
    see `Overview of the Networking Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Network/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Cpe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Cpe.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Cpe.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Cpe.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Cpe.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Cpe.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this Cpe.
        :type ip_address: str

        :param cpe_device_shape_id:
            The value to assign to the cpe_device_shape_id property of this Cpe.
        :type cpe_device_shape_id: str

        :param time_created:
            The value to assign to the time_created property of this Cpe.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ip_address': 'str',
            'cpe_device_shape_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ip_address': 'ipAddress',
            'cpe_device_shape_id': 'cpeDeviceShapeId',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._ip_address = None
        self._cpe_device_shape_id = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.


        :return: The compartment_id of this Cpe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.


        :param compartment_id: The compartment_id of this Cpe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Cpe.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Cpe.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Cpe.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Cpe.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Cpe.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Cpe.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Cpe.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Cpe.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Cpe.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Cpe.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Cpe.
        The CPE's Oracle ID (OCID).


        :return: The id of this Cpe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cpe.
        The CPE's Oracle ID (OCID).


        :param id: The id of this Cpe.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Cpe.
        The public IP address of the on-premises router.


        :return: The ip_address of this Cpe.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Cpe.
        The public IP address of the on-premises router.


        :param ip_address: The ip_address of this Cpe.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def cpe_device_shape_id(self):
        """
        Gets the cpe_device_shape_id of this Cpe.
        The `OCID`__ of the CPE's device type.
        The Networking service maintains a general list of CPE device types (for example,
        Cisco ASA). For each type, Oracle provides CPE configuration content that can help
        a network engineer configure the CPE. The OCID uniquely identifies the type of
        device. To get the OCIDs for the device types on the list, see
        :func:`list_cpe_device_shapes`.

        For information about how to generate CPE configuration content for a
        CPE device type, see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cpe_device_shape_id of this Cpe.
        :rtype: str
        """
        return self._cpe_device_shape_id

    @cpe_device_shape_id.setter
    def cpe_device_shape_id(self, cpe_device_shape_id):
        """
        Sets the cpe_device_shape_id of this Cpe.
        The `OCID`__ of the CPE's device type.
        The Networking service maintains a general list of CPE device types (for example,
        Cisco ASA). For each type, Oracle provides CPE configuration content that can help
        a network engineer configure the CPE. The OCID uniquely identifies the type of
        device. To get the OCIDs for the device types on the list, see
        :func:`list_cpe_device_shapes`.

        For information about how to generate CPE configuration content for a
        CPE device type, see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cpe_device_shape_id: The cpe_device_shape_id of this Cpe.
        :type: str
        """
        self._cpe_device_shape_id = cpe_device_shape_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Cpe.
        The date and time the CPE was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Cpe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Cpe.
        The date and time the CPE was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Cpe.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
