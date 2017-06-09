# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreatePolicyDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'description': 'str',
            'version_date': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'statements': 'statements',
            'description': 'description',
            'version_date': 'versionDate'
        }

        self._compartment_id = None
        self._name = None
        self._statements = None
        self._description = None
        self._version_date = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreatePolicyDetails.
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
        Gets the name of this CreatePolicyDetails.
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
        Gets the statements of this CreatePolicyDetails.
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
        Gets the description of this CreatePolicyDetails.
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
