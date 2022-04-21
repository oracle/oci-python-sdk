# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAccessPolicyDetails(object):
    """
    The information about a new access policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAccessPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateAccessPolicyDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateAccessPolicyDetails.
        :type description: str

        :param mesh_id:
            The value to assign to the mesh_id property of this CreateAccessPolicyDetails.
        :type mesh_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAccessPolicyDetails.
        :type compartment_id: str

        :param rules:
            The value to assign to the rules property of this CreateAccessPolicyDetails.
        :type rules: list[oci.service_mesh.models.AccessPolicyRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAccessPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAccessPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'mesh_id': 'str',
            'compartment_id': 'str',
            'rules': 'list[AccessPolicyRule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'mesh_id': 'meshId',
            'compartment_id': 'compartmentId',
            'rules': 'rules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._mesh_id = None
        self._compartment_id = None
        self._rules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateAccessPolicyDetails.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this CreateAccessPolicyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAccessPolicyDetails.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this CreateAccessPolicyDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateAccessPolicyDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this CreateAccessPolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateAccessPolicyDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this CreateAccessPolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def mesh_id(self):
        """
        **[Required]** Gets the mesh_id of this CreateAccessPolicyDetails.
        The OCID of the service mesh in which this access policy is created.


        :return: The mesh_id of this CreateAccessPolicyDetails.
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """
        Sets the mesh_id of this CreateAccessPolicyDetails.
        The OCID of the service mesh in which this access policy is created.


        :param mesh_id: The mesh_id of this CreateAccessPolicyDetails.
        :type: str
        """
        self._mesh_id = mesh_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAccessPolicyDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAccessPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAccessPolicyDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAccessPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def rules(self):
        """
        Gets the rules of this CreateAccessPolicyDetails.
        List of applicable rules


        :return: The rules of this CreateAccessPolicyDetails.
        :rtype: list[oci.service_mesh.models.AccessPolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this CreateAccessPolicyDetails.
        List of applicable rules


        :param rules: The rules of this CreateAccessPolicyDetails.
        :type: list[oci.service_mesh.models.AccessPolicyRule]
        """
        self._rules = rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAccessPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAccessPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAccessPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAccessPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAccessPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAccessPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAccessPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAccessPolicyDetails.
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
