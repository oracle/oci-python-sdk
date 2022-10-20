# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrPlanDetails(object):
    """
    The details for creating a DR Plan.
    """

    #: A constant which can be used with the type property of a CreateDrPlanDetails.
    #: This constant has a value of "SWITCHOVER"
    TYPE_SWITCHOVER = "SWITCHOVER"

    #: A constant which can be used with the type property of a CreateDrPlanDetails.
    #: This constant has a value of "FAILOVER"
    TYPE_FAILOVER = "FAILOVER"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrPlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDrPlanDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this CreateDrPlanDetails.
            Allowed values for this property are: "SWITCHOVER", "FAILOVER"
        :type type: str

        :param dr_protection_group_id:
            The value to assign to the dr_protection_group_id property of this CreateDrPlanDetails.
        :type dr_protection_group_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDrPlanDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDrPlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'type': 'str',
            'dr_protection_group_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'type': 'type',
            'dr_protection_group_id': 'drProtectionGroupId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._type = None
        self._dr_protection_group_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDrPlanDetails.
        The display name of the DR Plan being created.

        Example: `EBS Switchover PHX to IAD`


        :return: The display_name of this CreateDrPlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrPlanDetails.
        The display name of the DR Plan being created.

        Example: `EBS Switchover PHX to IAD`


        :param display_name: The display_name of this CreateDrPlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateDrPlanDetails.
        The type of DR Plan to be created.

        Allowed values for this property are: "SWITCHOVER", "FAILOVER"


        :return: The type of this CreateDrPlanDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateDrPlanDetails.
        The type of DR Plan to be created.


        :param type: The type of this CreateDrPlanDetails.
        :type: str
        """
        allowed_values = ["SWITCHOVER", "FAILOVER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def dr_protection_group_id(self):
        """
        **[Required]** Gets the dr_protection_group_id of this CreateDrPlanDetails.
        The OCID of the DR Protection Group to which this DR Plan belongs.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :return: The dr_protection_group_id of this CreateDrPlanDetails.
        :rtype: str
        """
        return self._dr_protection_group_id

    @dr_protection_group_id.setter
    def dr_protection_group_id(self, dr_protection_group_id):
        """
        Sets the dr_protection_group_id of this CreateDrPlanDetails.
        The OCID of the DR Protection Group to which this DR Plan belongs.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :param dr_protection_group_id: The dr_protection_group_id of this CreateDrPlanDetails.
        :type: str
        """
        self._dr_protection_group_id = dr_protection_group_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDrPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this CreateDrPlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDrPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this CreateDrPlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDrPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this CreateDrPlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDrPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this CreateDrPlanDetails.
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
