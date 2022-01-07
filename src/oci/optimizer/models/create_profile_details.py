# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateProfileDetails(object):
    """
    Details for creating a profile.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateProfileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateProfileDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateProfileDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateProfileDetails.
        :type description: str

        :param aggregation_interval_in_days:
            The value to assign to the aggregation_interval_in_days property of this CreateProfileDetails.
        :type aggregation_interval_in_days: int

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateProfileDetails.
        :type freeform_tags: dict(str, str)

        :param levels_configuration:
            The value to assign to the levels_configuration property of this CreateProfileDetails.
        :type levels_configuration: oci.optimizer.models.LevelsConfiguration

        :param target_compartments:
            The value to assign to the target_compartments property of this CreateProfileDetails.
        :type target_compartments: oci.optimizer.models.TargetCompartments

        :param target_tags:
            The value to assign to the target_tags property of this CreateProfileDetails.
        :type target_tags: oci.optimizer.models.TargetTags

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'aggregation_interval_in_days': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'levels_configuration': 'LevelsConfiguration',
            'target_compartments': 'TargetCompartments',
            'target_tags': 'TargetTags'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'aggregation_interval_in_days': 'aggregationIntervalInDays',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'levels_configuration': 'levelsConfiguration',
            'target_compartments': 'targetCompartments',
            'target_tags': 'targetTags'
        }

        self._compartment_id = None
        self._name = None
        self._description = None
        self._aggregation_interval_in_days = None
        self._defined_tags = None
        self._freeform_tags = None
        self._levels_configuration = None
        self._target_compartments = None
        self._target_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateProfileDetails.
        The OCID of the tenancy. The tenancy is the root compartment.


        :return: The compartment_id of this CreateProfileDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateProfileDetails.
        The OCID of the tenancy. The tenancy is the root compartment.


        :param compartment_id: The compartment_id of this CreateProfileDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateProfileDetails.
        The name assigned to the profile. Avoid entering confidential information.


        :return: The name of this CreateProfileDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateProfileDetails.
        The name assigned to the profile. Avoid entering confidential information.


        :param name: The name of this CreateProfileDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateProfileDetails.
        Text describing the profile. Avoid entering confidential information.


        :return: The description of this CreateProfileDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateProfileDetails.
        Text describing the profile. Avoid entering confidential information.


        :param description: The description of this CreateProfileDetails.
        :type: str
        """
        self._description = description

    @property
    def aggregation_interval_in_days(self):
        """
        Gets the aggregation_interval_in_days of this CreateProfileDetails.
        The time period over which to collect data for the recommendations, measured in number of days.


        :return: The aggregation_interval_in_days of this CreateProfileDetails.
        :rtype: int
        """
        return self._aggregation_interval_in_days

    @aggregation_interval_in_days.setter
    def aggregation_interval_in_days(self, aggregation_interval_in_days):
        """
        Sets the aggregation_interval_in_days of this CreateProfileDetails.
        The time period over which to collect data for the recommendations, measured in number of days.


        :param aggregation_interval_in_days: The aggregation_interval_in_days of this CreateProfileDetails.
        :type: int
        """
        self._aggregation_interval_in_days = aggregation_interval_in_days

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateProfileDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateProfileDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateProfileDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateProfileDetails.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateProfileDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateProfileDetails.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateProfileDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def levels_configuration(self):
        """
        **[Required]** Gets the levels_configuration of this CreateProfileDetails.

        :return: The levels_configuration of this CreateProfileDetails.
        :rtype: oci.optimizer.models.LevelsConfiguration
        """
        return self._levels_configuration

    @levels_configuration.setter
    def levels_configuration(self, levels_configuration):
        """
        Sets the levels_configuration of this CreateProfileDetails.

        :param levels_configuration: The levels_configuration of this CreateProfileDetails.
        :type: oci.optimizer.models.LevelsConfiguration
        """
        self._levels_configuration = levels_configuration

    @property
    def target_compartments(self):
        """
        Gets the target_compartments of this CreateProfileDetails.

        :return: The target_compartments of this CreateProfileDetails.
        :rtype: oci.optimizer.models.TargetCompartments
        """
        return self._target_compartments

    @target_compartments.setter
    def target_compartments(self, target_compartments):
        """
        Sets the target_compartments of this CreateProfileDetails.

        :param target_compartments: The target_compartments of this CreateProfileDetails.
        :type: oci.optimizer.models.TargetCompartments
        """
        self._target_compartments = target_compartments

    @property
    def target_tags(self):
        """
        Gets the target_tags of this CreateProfileDetails.

        :return: The target_tags of this CreateProfileDetails.
        :rtype: oci.optimizer.models.TargetTags
        """
        return self._target_tags

    @target_tags.setter
    def target_tags(self, target_tags):
        """
        Sets the target_tags of this CreateProfileDetails.

        :param target_tags: The target_tags of this CreateProfileDetails.
        :type: oci.optimizer.models.TargetTags
        """
        self._target_tags = target_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
