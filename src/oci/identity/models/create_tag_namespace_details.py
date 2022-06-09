# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTagNamespaceDetails(object):
    """
    CreateTagNamespaceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTagNamespaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTagNamespaceDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateTagNamespaceDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateTagNamespaceDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTagNamespaceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTagNamespaceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this CreateTagNamespaceDetails.
        :type locks: list[oci.identity.models.AddLockDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'locks': 'list[AddLockDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'locks': 'locks'
        }

        self._compartment_id = None
        self._name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._locks = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTagNamespaceDetails.
        The OCID of the tenancy containing the tag namespace.


        :return: The compartment_id of this CreateTagNamespaceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTagNamespaceDetails.
        The OCID of the tenancy containing the tag namespace.


        :param compartment_id: The compartment_id of this CreateTagNamespaceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateTagNamespaceDetails.
        The name you assign to the tag namespace during creation. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :return: The name of this CreateTagNamespaceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTagNamespaceDetails.
        The name you assign to the tag namespace during creation. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :param name: The name of this CreateTagNamespaceDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateTagNamespaceDetails.
        The description you assign to the tag namespace during creation.


        :return: The description of this CreateTagNamespaceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTagNamespaceDetails.
        The description you assign to the tag namespace during creation.


        :param description: The description of this CreateTagNamespaceDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTagNamespaceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateTagNamespaceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTagNamespaceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateTagNamespaceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTagNamespaceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateTagNamespaceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTagNamespaceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateTagNamespaceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def locks(self):
        """
        Gets the locks of this CreateTagNamespaceDetails.
        Locks associated with this resource.


        :return: The locks of this CreateTagNamespaceDetails.
        :rtype: list[oci.identity.models.AddLockDetails]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this CreateTagNamespaceDetails.
        Locks associated with this resource.


        :param locks: The locks of this CreateTagNamespaceDetails.
        :type: list[oci.identity.models.AddLockDetails]
        """
        self._locks = locks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
