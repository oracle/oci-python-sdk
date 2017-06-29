# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdatePolicyDetails(object):

    def __init__(self):

        self.swagger_types = {
            'description': 'str',
            'statements': 'list[str]',
            'version_date': 'datetime'
        }

        self.attribute_map = {
            'description': 'description',
            'statements': 'statements',
            'version_date': 'versionDate'
        }

        self._description = None
        self._statements = None
        self._version_date = None

    @property
    def description(self):
        """
        Gets the description of this UpdatePolicyDetails.
        The description you assign to the policy. Does not have to be unique, and it's changeable.


        :return: The description of this UpdatePolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdatePolicyDetails.
        The description you assign to the policy. Does not have to be unique, and it's changeable.


        :param description: The description of this UpdatePolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def statements(self):
        """
        Gets the statements of this UpdatePolicyDetails.
        An array of policy statements written in the policy language. See
        `How Policies Work`__ and
        `Common Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm


        :return: The statements of this UpdatePolicyDetails.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this UpdatePolicyDetails.
        An array of policy statements written in the policy language. See
        `How Policies Work`__ and
        `Common Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm


        :param statements: The statements of this UpdatePolicyDetails.
        :type: list[str]
        """
        self._statements = statements

    @property
    def version_date(self):
        """
        Gets the version_date of this UpdatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :return: The version_date of this UpdatePolicyDetails.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this UpdatePolicyDetails.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :param version_date: The version_date of this UpdatePolicyDetails.
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
