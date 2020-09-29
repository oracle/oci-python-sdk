# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGatewayDetails(object):
    """
    Information about the new gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateGatewayDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGatewayDetails.
        :type compartment_id: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this CreateGatewayDetails.
        :type endpoint_type: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateGatewayDetails.
        :type subnet_id: str

        :param certificate_id:
            The value to assign to the certificate_id property of this CreateGatewayDetails.
        :type certificate_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'endpoint_type': 'str',
            'subnet_id': 'str',
            'certificate_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'endpoint_type': 'endpointType',
            'subnet_id': 'subnetId',
            'certificate_id': 'certificateId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._endpoint_type = None
        self._subnet_id = None
        self._certificate_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateGatewayDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateGatewayDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateGatewayDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateGatewayDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def endpoint_type(self):
        """
        **[Required]** Gets the endpoint_type of this CreateGatewayDetails.
        Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
        accessible on a private IP address on the subnet.

        Example: `PUBLIC` or `PRIVATE`


        :return: The endpoint_type of this CreateGatewayDetails.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this CreateGatewayDetails.
        Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
        accessible on a private IP address on the subnet.

        Example: `PUBLIC` or `PRIVATE`


        :param endpoint_type: The endpoint_type of this CreateGatewayDetails.
        :type: str
        """
        self._endpoint_type = endpoint_type

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateGatewayDetails.
        The `OCID`__ of the subnet in which
        related resources are created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateGatewayDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateGatewayDetails.
        The `OCID`__ of the subnet in which
        related resources are created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateGatewayDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this CreateGatewayDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The certificate_id of this CreateGatewayDetails.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this CreateGatewayDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param certificate_id: The certificate_id of this CreateGatewayDetails.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateGatewayDetails.
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
