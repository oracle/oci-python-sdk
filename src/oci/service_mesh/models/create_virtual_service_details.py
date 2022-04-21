# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVirtualServiceDetails(object):
    """
    The information about the new VirtualService.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVirtualServiceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mesh_id:
            The value to assign to the mesh_id property of this CreateVirtualServiceDetails.
        :type mesh_id: str

        :param name:
            The value to assign to the name property of this CreateVirtualServiceDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateVirtualServiceDetails.
        :type description: str

        :param default_routing_policy:
            The value to assign to the default_routing_policy property of this CreateVirtualServiceDetails.
        :type default_routing_policy: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy

        :param hosts:
            The value to assign to the hosts property of this CreateVirtualServiceDetails.
        :type hosts: list[str]

        :param mtls:
            The value to assign to the mtls property of this CreateVirtualServiceDetails.
        :type mtls: oci.service_mesh.models.CreateMutualTransportLayerSecurityDetails

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVirtualServiceDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVirtualServiceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVirtualServiceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'mesh_id': 'str',
            'name': 'str',
            'description': 'str',
            'default_routing_policy': 'DefaultVirtualServiceRoutingPolicy',
            'hosts': 'list[str]',
            'mtls': 'CreateMutualTransportLayerSecurityDetails',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'mesh_id': 'meshId',
            'name': 'name',
            'description': 'description',
            'default_routing_policy': 'defaultRoutingPolicy',
            'hosts': 'hosts',
            'mtls': 'mtls',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._mesh_id = None
        self._name = None
        self._description = None
        self._default_routing_policy = None
        self._hosts = None
        self._mtls = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def mesh_id(self):
        """
        **[Required]** Gets the mesh_id of this CreateVirtualServiceDetails.
        The OCID of the service mesh in which this virtual service is created.


        :return: The mesh_id of this CreateVirtualServiceDetails.
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """
        Sets the mesh_id of this CreateVirtualServiceDetails.
        The OCID of the service mesh in which this virtual service is created.


        :param mesh_id: The mesh_id of this CreateVirtualServiceDetails.
        :type: str
        """
        self._mesh_id = mesh_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateVirtualServiceDetails.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this CreateVirtualServiceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateVirtualServiceDetails.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this CreateVirtualServiceDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateVirtualServiceDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this CreateVirtualServiceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateVirtualServiceDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this CreateVirtualServiceDetails.
        :type: str
        """
        self._description = description

    @property
    def default_routing_policy(self):
        """
        Gets the default_routing_policy of this CreateVirtualServiceDetails.

        :return: The default_routing_policy of this CreateVirtualServiceDetails.
        :rtype: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy
        """
        return self._default_routing_policy

    @default_routing_policy.setter
    def default_routing_policy(self, default_routing_policy):
        """
        Sets the default_routing_policy of this CreateVirtualServiceDetails.

        :param default_routing_policy: The default_routing_policy of this CreateVirtualServiceDetails.
        :type: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy
        """
        self._default_routing_policy = default_routing_policy

    @property
    def hosts(self):
        """
        Gets the hosts of this CreateVirtualServiceDetails.
        The DNS hostnames of the virtual service that is used by its callers.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".
        Can be omitted if the virtual service will only have TCP virtual deployments.


        :return: The hosts of this CreateVirtualServiceDetails.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this CreateVirtualServiceDetails.
        The DNS hostnames of the virtual service that is used by its callers.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".
        Can be omitted if the virtual service will only have TCP virtual deployments.


        :param hosts: The hosts of this CreateVirtualServiceDetails.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def mtls(self):
        """
        Gets the mtls of this CreateVirtualServiceDetails.

        :return: The mtls of this CreateVirtualServiceDetails.
        :rtype: oci.service_mesh.models.CreateMutualTransportLayerSecurityDetails
        """
        return self._mtls

    @mtls.setter
    def mtls(self, mtls):
        """
        Sets the mtls of this CreateVirtualServiceDetails.

        :param mtls: The mtls of this CreateVirtualServiceDetails.
        :type: oci.service_mesh.models.CreateMutualTransportLayerSecurityDetails
        """
        self._mtls = mtls

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVirtualServiceDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateVirtualServiceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVirtualServiceDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateVirtualServiceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVirtualServiceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateVirtualServiceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVirtualServiceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateVirtualServiceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVirtualServiceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateVirtualServiceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVirtualServiceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateVirtualServiceDetails.
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
