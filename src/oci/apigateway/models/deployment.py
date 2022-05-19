# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Deployment(object):
    """
    A deployment deploys an API on a gateway. Avoid entering confidential information.
    For more information, see
    `API Gateway Concepts`__.

    __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Deployment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Deployment.
        :type id: str

        :param gateway_id:
            The value to assign to the gateway_id property of this Deployment.
        :type gateway_id: str

        :param display_name:
            The value to assign to the display_name property of this Deployment.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Deployment.
        :type compartment_id: str

        :param path_prefix:
            The value to assign to the path_prefix property of this Deployment.
        :type path_prefix: str

        :param endpoint:
            The value to assign to the endpoint property of this Deployment.
        :type endpoint: str

        :param specification:
            The value to assign to the specification property of this Deployment.
        :type specification: oci.apigateway.models.ApiSpecification

        :param time_created:
            The value to assign to the time_created property of this Deployment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Deployment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Deployment.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Deployment.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Deployment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Deployment.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'gateway_id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'path_prefix': 'str',
            'endpoint': 'str',
            'specification': 'ApiSpecification',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'gateway_id': 'gatewayId',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'path_prefix': 'pathPrefix',
            'endpoint': 'endpoint',
            'specification': 'specification',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._gateway_id = None
        self._display_name = None
        self._compartment_id = None
        self._path_prefix = None
        self._endpoint = None
        self._specification = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Deployment.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Deployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Deployment.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Deployment.
        :type: str
        """
        self._id = id

    @property
    def gateway_id(self):
        """
        **[Required]** Gets the gateway_id of this Deployment.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The gateway_id of this Deployment.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this Deployment.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param gateway_id: The gateway_id of this Deployment.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Deployment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this Deployment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Deployment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this Deployment.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Deployment.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Deployment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Deployment.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Deployment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def path_prefix(self):
        """
        **[Required]** Gets the path_prefix of this Deployment.
        A path on which to deploy all routes contained in the API
        deployment specification. For more information, see
        `Deploying an API on an API Gateway by Creating an API
        Deployment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm


        :return: The path_prefix of this Deployment.
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """
        Sets the path_prefix of this Deployment.
        A path on which to deploy all routes contained in the API
        deployment specification. For more information, see
        `Deploying an API on an API Gateway by Creating an API
        Deployment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm


        :param path_prefix: The path_prefix of this Deployment.
        :type: str
        """
        self._path_prefix = path_prefix

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this Deployment.
        The endpoint to access this deployment on the gateway.


        :return: The endpoint of this Deployment.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this Deployment.
        The endpoint to access this deployment on the gateway.


        :param endpoint: The endpoint of this Deployment.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def specification(self):
        """
        **[Required]** Gets the specification of this Deployment.

        :return: The specification of this Deployment.
        :rtype: oci.apigateway.models.ApiSpecification
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """
        Sets the specification of this Deployment.

        :param specification: The specification of this Deployment.
        :type: oci.apigateway.models.ApiSpecification
        """
        self._specification = specification

    @property
    def time_created(self):
        """
        Gets the time_created of this Deployment.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Deployment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Deployment.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Deployment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Deployment.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Deployment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Deployment.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Deployment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Deployment.
        The current state of the deployment.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Deployment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Deployment.
        The current state of the deployment.


        :param lifecycle_state: The lifecycle_state of this Deployment.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Deployment.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :return: The lifecycle_details of this Deployment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Deployment.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Deployment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Deployment.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Deployment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Deployment.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Deployment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Deployment.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Deployment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Deployment.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Deployment.
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
