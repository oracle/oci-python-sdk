# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeploymentDetails(object):
    """
    Information about a new deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDeploymentDetails.
        :type display_name: str

        :param gateway_id:
            The value to assign to the gateway_id property of this CreateDeploymentDetails.
        :type gateway_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDeploymentDetails.
        :type compartment_id: str

        :param path_prefix:
            The value to assign to the path_prefix property of this CreateDeploymentDetails.
        :type path_prefix: str

        :param specification:
            The value to assign to the specification property of this CreateDeploymentDetails.
        :type specification: oci.apigateway.models.ApiSpecification

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'gateway_id': 'str',
            'compartment_id': 'str',
            'path_prefix': 'str',
            'specification': 'ApiSpecification',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'gateway_id': 'gatewayId',
            'compartment_id': 'compartmentId',
            'path_prefix': 'pathPrefix',
            'specification': 'specification',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._gateway_id = None
        self._compartment_id = None
        self._path_prefix = None
        self._specification = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDeploymentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeploymentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateDeploymentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def gateway_id(self):
        """
        **[Required]** Gets the gateway_id of this CreateDeploymentDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The gateway_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this CreateDeploymentDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param gateway_id: The gateway_id of this CreateDeploymentDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDeploymentDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDeploymentDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDeploymentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def path_prefix(self):
        """
        **[Required]** Gets the path_prefix of this CreateDeploymentDetails.
        A path on which to deploy all routes contained in the API
        deployment specification. For more information, see
        `Deploying an API on an API Gateway by Creating an API
        Deployment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm


        :return: The path_prefix of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """
        Sets the path_prefix of this CreateDeploymentDetails.
        A path on which to deploy all routes contained in the API
        deployment specification. For more information, see
        `Deploying an API on an API Gateway by Creating an API
        Deployment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm


        :param path_prefix: The path_prefix of this CreateDeploymentDetails.
        :type: str
        """
        self._path_prefix = path_prefix

    @property
    def specification(self):
        """
        Gets the specification of this CreateDeploymentDetails.

        :return: The specification of this CreateDeploymentDetails.
        :rtype: oci.apigateway.models.ApiSpecification
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """
        Sets the specification of this CreateDeploymentDetails.

        :param specification: The specification of this CreateDeploymentDetails.
        :type: oci.apigateway.models.ApiSpecification
        """
        self._specification = specification

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeploymentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDeploymentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeploymentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDeploymentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDeploymentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDeploymentDetails.
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
