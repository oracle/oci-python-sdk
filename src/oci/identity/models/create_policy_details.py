# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePolicyDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePolicyDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreatePolicyDetails.
        :type name: str

        :param statements:
            The value to assign to the statements property of this CreatePolicyDetails.
        :type statements: list[str]

        :param description:
            The value to assign to the description property of this CreatePolicyDetails.
        :type description: str

        :param version_date:
            The value to assign to the version_date property of this CreatePolicyDetails.
        :type version_date: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'description': 'str',
            'version_date': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'statements': 'statements',
            'description': 'description',
            'version_date': 'versionDate',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._name = None
        self._statements = None
        self._description = None
        self._version_date = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePolicyDetails.
        The OCID of the compartment containing the policy (either the tenancy or another compartment).


        :return: The compartment_id of this CreatePolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePolicyDetails.
        The OCID of the compartment containing the policy (either the tenancy or another compartment).


        :param compartment_id: The compartment_id of this CreatePolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreatePolicyDetails.
        The name you assign to the policy during creation. The name must be unique across all policies
        in the tenancy and cannot be changed.


        :return: The name of this CreatePolicyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePolicyDetails.
        The name you assign to the policy during creation. The name must be unique across all policies
        in the tenancy and cannot be changed.


        :param name: The name of this CreatePolicyDetails.
        :type: str
        """
        self._name = name

    @property
    def statements(self):
        """
        **[Required]** Gets the statements of this CreatePolicyDetails.
        An array of policy statements written in the policy language. See
        `How Policies Work`__ and
        `Common Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm


        :return: The statements of this CreatePolicyDetails.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this CreatePolicyDetails.
        An array of policy statements written in the policy language. See
        `How Policies Work`__ and
        `Common Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm


        :param statements: The statements of this CreatePolicyDetails.
        :type: list[str]
        """
        self._statements = statements

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreatePolicyDetails.
        The description you assign to the policy during creation. Does not have to be unique, and it's changeable.


        :return: The description of this CreatePolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePolicyDetails.
        The description you assign to the policy during creation. Does not have to be unique, and it's changeable.


        :param description: The description of this CreatePolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def version_date(self):
        """
        Gets the version_date of this CreatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :return: The version_date of this CreatePolicyDetails.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this CreatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :param version_date: The version_date of this CreatePolicyDetails.
        :type: datetime
        """
        self._version_date = version_date

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePolicyDetails.
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
