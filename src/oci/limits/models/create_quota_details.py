# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateQuotaDetails(object):
    """
    Request object for create quota operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateQuotaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateQuotaDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateQuotaDetails.
        :type description: str

        :param name:
            The value to assign to the name property of this CreateQuotaDetails.
        :type name: str

        :param statements:
            The value to assign to the statements property of this CreateQuotaDetails.
        :type statements: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateQuotaDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateQuotaDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'description': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'description': 'description',
            'name': 'name',
            'statements': 'statements',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._description = None
        self._name = None
        self._statements = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateQuotaDetails.
        The OCID of the compartment containing the resource this quota applies to.


        :return: The compartment_id of this CreateQuotaDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateQuotaDetails.
        The OCID of the compartment containing the resource this quota applies to.


        :param compartment_id: The compartment_id of this CreateQuotaDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateQuotaDetails.
        The description you assign to the quota.


        :return: The description of this CreateQuotaDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateQuotaDetails.
        The description you assign to the quota.


        :param description: The description of this CreateQuotaDetails.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateQuotaDetails.
        The name you assign to the quota during creation. The name must be unique across all quotas
        in the tenancy and cannot be changed.


        :return: The name of this CreateQuotaDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateQuotaDetails.
        The name you assign to the quota during creation. The name must be unique across all quotas
        in the tenancy and cannot be changed.


        :param name: The name of this CreateQuotaDetails.
        :type: str
        """
        self._name = name

    @property
    def statements(self):
        """
        **[Required]** Gets the statements of this CreateQuotaDetails.
        An array of quota statements written in the declarative quota statement language.


        :return: The statements of this CreateQuotaDetails.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this CreateQuotaDetails.
        An array of quota statements written in the declarative quota statement language.


        :param statements: The statements of this CreateQuotaDetails.
        :type: list[str]
        """
        self._statements = statements

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateQuotaDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateQuotaDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateQuotaDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateQuotaDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateQuotaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateQuotaDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateQuotaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateQuotaDetails.
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
