# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCpeDetails(object):
    """
    CreateCpeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCpeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCpeDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCpeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateCpeDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCpeDetails.
        :type freeform_tags: dict(str, str)

        :param ip_address:
            The value to assign to the ip_address property of this CreateCpeDetails.
        :type ip_address: str

        :param cpe_device_shape_id:
            The value to assign to the cpe_device_shape_id property of this CreateCpeDetails.
        :type cpe_device_shape_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'ip_address': 'str',
            'cpe_device_shape_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'ip_address': 'ipAddress',
            'cpe_device_shape_id': 'cpeDeviceShapeId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._ip_address = None
        self._cpe_device_shape_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.


        :return: The compartment_id of this CreateCpeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCpeDetails.
        The OCID of the compartment to contain the CPE.


        :param compartment_id: The compartment_id of this CreateCpeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCpeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCpeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCpeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCpeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateCpeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCpeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateCpeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCpeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCpeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCpeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCpeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premises router.

        Example: `203.0.113.2`


        :return: The ip_address of this CreateCpeDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateCpeDetails.
        The public IP address of the on-premises router.

        Example: `203.0.113.2`


        :param ip_address: The ip_address of this CreateCpeDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def cpe_device_shape_id(self):
        """
        Gets the cpe_device_shape_id of this CreateCpeDetails.
        The `OCID`__ of the CPE device type. You can provide
        a value if you want to later generate CPE device configuration content for IPSec connections
        that use this CPE. You can also call :func:`update_cpe` later to
        provide a value. For a list of possible values, see
        :func:`list_cpe_device_shapes`.

        For more information about generating CPE device configuration content, see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cpe_device_shape_id of this CreateCpeDetails.
        :rtype: str
        """
        return self._cpe_device_shape_id

    @cpe_device_shape_id.setter
    def cpe_device_shape_id(self, cpe_device_shape_id):
        """
        Sets the cpe_device_shape_id of this CreateCpeDetails.
        The `OCID`__ of the CPE device type. You can provide
        a value if you want to later generate CPE device configuration content for IPSec connections
        that use this CPE. You can also call :func:`update_cpe` later to
        provide a value. For a list of possible values, see
        :func:`list_cpe_device_shapes`.

        For more information about generating CPE device configuration content, see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cpe_device_shape_id: The cpe_device_shape_id of this CreateCpeDetails.
        :type: str
        """
        self._cpe_device_shape_id = cpe_device_shape_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
