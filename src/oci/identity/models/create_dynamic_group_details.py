# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDynamicGroupDetails(object):
    """
    Properties for creating a dynamic group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDynamicGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDynamicGroupDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateDynamicGroupDetails.
        :type name: str

        :param matching_rule:
            The value to assign to the matching_rule property of this CreateDynamicGroupDetails.
        :type matching_rule: str

        :param description:
            The value to assign to the description property of this CreateDynamicGroupDetails.
        :type description: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'matching_rule': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'matching_rule': 'matchingRule',
            'description': 'description'
        }

        self._compartment_id = None
        self._name = None
        self._matching_rule = None
        self._description = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDynamicGroupDetails.
        The OCID of the tenancy containing the group.


        :return: The compartment_id of this CreateDynamicGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDynamicGroupDetails.
        The OCID of the tenancy containing the group.


        :param compartment_id: The compartment_id of this CreateDynamicGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDynamicGroupDetails.
        The name you assign to the group during creation. The name must be unique across all groups
        in the tenancy and cannot be changed.


        :return: The name of this CreateDynamicGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDynamicGroupDetails.
        The name you assign to the group during creation. The name must be unique across all groups
        in the tenancy and cannot be changed.


        :param name: The name of this CreateDynamicGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def matching_rule(self):
        """
        **[Required]** Gets the matching_rule of this CreateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :return: The matching_rule of this CreateDynamicGroupDetails.
        :rtype: str
        """
        return self._matching_rule

    @matching_rule.setter
    def matching_rule(self, matching_rule):
        """
        Sets the matching_rule of this CreateDynamicGroupDetails.
        The matching rule to dynamically match an instance certificate to this dynamic group.
        For rule syntax, see `Managing Dynamic Groups`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm


        :param matching_rule: The matching_rule of this CreateDynamicGroupDetails.
        :type: str
        """
        self._matching_rule = matching_rule

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateDynamicGroupDetails.
        The description you assign to the group during creation. Does not have to be unique, and it's changeable.


        :return: The description of this CreateDynamicGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDynamicGroupDetails.
        The description you assign to the group during creation. Does not have to be unique, and it's changeable.


        :param description: The description of this CreateDynamicGroupDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
