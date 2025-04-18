# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220615


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGateway(object):
    """
    An ingress gateway allows resources that are outside of a mesh to communicate to resources that are inside the mesh. It sits on the edge of a service mesh receiving incoming HTTP/TCP connections to the mesh.
    """

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a IngressGateway.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGateway object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IngressGateway.
        :type id: str

        :param name:
            The value to assign to the name property of this IngressGateway.
        :type name: str

        :param description:
            The value to assign to the description property of this IngressGateway.
        :type description: str

        :param mesh_id:
            The value to assign to the mesh_id property of this IngressGateway.
        :type mesh_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IngressGateway.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this IngressGateway.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IngressGateway.
        :type time_updated: datetime

        :param hosts:
            The value to assign to the hosts property of this IngressGateway.
        :type hosts: list[oci.service_mesh.models.IngressGatewayHost]

        :param mtls:
            The value to assign to the mtls property of this IngressGateway.
        :type mtls: oci.service_mesh.models.IngressGatewayMutualTransportLayerSecurity

        :param access_logging:
            The value to assign to the access_logging property of this IngressGateway.
        :type access_logging: oci.service_mesh.models.AccessLoggingConfiguration

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IngressGateway.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this IngressGateway.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IngressGateway.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this IngressGateway.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this IngressGateway.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'mesh_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'hosts': 'list[IngressGatewayHost]',
            'mtls': 'IngressGatewayMutualTransportLayerSecurity',
            'access_logging': 'AccessLoggingConfiguration',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'mesh_id': 'meshId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'hosts': 'hosts',
            'mtls': 'mtls',
            'access_logging': 'accessLogging',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._name = None
        self._description = None
        self._mesh_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._hosts = None
        self._mtls = None
        self._access_logging = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IngressGateway.
        Unique identifier that is immutable on creation.


        :return: The id of this IngressGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IngressGateway.
        Unique identifier that is immutable on creation.


        :param id: The id of this IngressGateway.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IngressGateway.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this IngressGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IngressGateway.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this IngressGateway.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this IngressGateway.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this IngressGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IngressGateway.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this IngressGateway.
        :type: str
        """
        self._description = description

    @property
    def mesh_id(self):
        """
        **[Required]** Gets the mesh_id of this IngressGateway.
        The OCID of the service mesh in which this ingress gateway is created.


        :return: The mesh_id of this IngressGateway.
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """
        Sets the mesh_id of this IngressGateway.
        The OCID of the service mesh in which this ingress gateway is created.


        :param mesh_id: The mesh_id of this IngressGateway.
        :type: str
        """
        self._mesh_id = mesh_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IngressGateway.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this IngressGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IngressGateway.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this IngressGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this IngressGateway.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :return: The time_created of this IngressGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IngressGateway.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :param time_created: The time_created of this IngressGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this IngressGateway.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :return: The time_updated of this IngressGateway.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IngressGateway.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this IngressGateway.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def hosts(self):
        """
        Gets the hosts of this IngressGateway.
        Array of hostnames and their listener configuration that this gateway will bind to.


        :return: The hosts of this IngressGateway.
        :rtype: list[oci.service_mesh.models.IngressGatewayHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this IngressGateway.
        Array of hostnames and their listener configuration that this gateway will bind to.


        :param hosts: The hosts of this IngressGateway.
        :type: list[oci.service_mesh.models.IngressGatewayHost]
        """
        self._hosts = hosts

    @property
    def mtls(self):
        """
        Gets the mtls of this IngressGateway.

        :return: The mtls of this IngressGateway.
        :rtype: oci.service_mesh.models.IngressGatewayMutualTransportLayerSecurity
        """
        return self._mtls

    @mtls.setter
    def mtls(self, mtls):
        """
        Sets the mtls of this IngressGateway.

        :param mtls: The mtls of this IngressGateway.
        :type: oci.service_mesh.models.IngressGatewayMutualTransportLayerSecurity
        """
        self._mtls = mtls

    @property
    def access_logging(self):
        """
        Gets the access_logging of this IngressGateway.

        :return: The access_logging of this IngressGateway.
        :rtype: oci.service_mesh.models.AccessLoggingConfiguration
        """
        return self._access_logging

    @access_logging.setter
    def access_logging(self, access_logging):
        """
        Sets the access_logging of this IngressGateway.

        :param access_logging: The access_logging of this IngressGateway.
        :type: oci.service_mesh.models.AccessLoggingConfiguration
        """
        self._access_logging = access_logging

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this IngressGateway.
        The current state of the Resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IngressGateway.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IngressGateway.
        The current state of the Resource.


        :param lifecycle_state: The lifecycle_state of this IngressGateway.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this IngressGateway.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this IngressGateway.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this IngressGateway.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this IngressGateway.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IngressGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this IngressGateway.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IngressGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this IngressGateway.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IngressGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this IngressGateway.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IngressGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this IngressGateway.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this IngressGateway.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this IngressGateway.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this IngressGateway.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this IngressGateway.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
