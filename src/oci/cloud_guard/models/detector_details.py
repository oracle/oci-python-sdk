# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectorDetails(object):
    """
    Detailed information for a detector.
    """

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new DetectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this DetectorDetails.
        :type is_enabled: bool

        :param risk_level:
            The value to assign to the risk_level property of this DetectorDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param configurations:
            The value to assign to the configurations property of this DetectorDetails.
        :type configurations: list[oci.cloud_guard.models.DetectorConfiguration]

        :param condition:
            The value to assign to the condition property of this DetectorDetails.
        :type condition: oci.cloud_guard.models.Condition

        :param labels:
            The value to assign to the labels property of this DetectorDetails.
        :type labels: list[str]

        :param is_configuration_allowed:
            The value to assign to the is_configuration_allowed property of this DetectorDetails.
        :type is_configuration_allowed: bool

        :param problem_threshold:
            The value to assign to the problem_threshold property of this DetectorDetails.
        :type problem_threshold: int

        :param target_types:
            The value to assign to the target_types property of this DetectorDetails.
        :type target_types: list[str]

        :param sighting_types:
            The value to assign to the sighting_types property of this DetectorDetails.
        :type sighting_types: list[oci.cloud_guard.models.SightingType]

        :param description:
            The value to assign to the description property of this DetectorDetails.
        :type description: str

        :param recommendation:
            The value to assign to the recommendation property of this DetectorDetails.
        :type recommendation: str

        :param data_source_id:
            The value to assign to the data_source_id property of this DetectorDetails.
        :type data_source_id: str

        :param entities_mappings:
            The value to assign to the entities_mappings property of this DetectorDetails.
        :type entities_mappings: list[oci.cloud_guard.models.EntitiesMapping]

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'risk_level': 'str',
            'configurations': 'list[DetectorConfiguration]',
            'condition': 'Condition',
            'labels': 'list[str]',
            'is_configuration_allowed': 'bool',
            'problem_threshold': 'int',
            'target_types': 'list[str]',
            'sighting_types': 'list[SightingType]',
            'description': 'str',
            'recommendation': 'str',
            'data_source_id': 'str',
            'entities_mappings': 'list[EntitiesMapping]'
        }
        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'risk_level': 'riskLevel',
            'configurations': 'configurations',
            'condition': 'condition',
            'labels': 'labels',
            'is_configuration_allowed': 'isConfigurationAllowed',
            'problem_threshold': 'problemThreshold',
            'target_types': 'targetTypes',
            'sighting_types': 'sightingTypes',
            'description': 'description',
            'recommendation': 'recommendation',
            'data_source_id': 'dataSourceId',
            'entities_mappings': 'entitiesMappings'
        }
        self._is_enabled = None
        self._risk_level = None
        self._configurations = None
        self._condition = None
        self._labels = None
        self._is_configuration_allowed = None
        self._problem_threshold = None
        self._target_types = None
        self._sighting_types = None
        self._description = None
        self._recommendation = None
        self._data_source_id = None
        self._entities_mappings = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this DetectorDetails.
        Enablement status for the rule


        :return: The is_enabled of this DetectorDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DetectorDetails.
        Enablement status for the rule


        :param is_enabled: The is_enabled of this DetectorDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def risk_level(self):
        """
        Gets the risk_level of this DetectorDetails.
        The risk level for the rule

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this DetectorDetails.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this DetectorDetails.
        The risk level for the rule


        :param risk_level: The risk_level of this DetectorDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def configurations(self):
        """
        Gets the configurations of this DetectorDetails.
        List of detector rule configurations


        :return: The configurations of this DetectorDetails.
        :rtype: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this DetectorDetails.
        List of detector rule configurations


        :param configurations: The configurations of this DetectorDetails.
        :type: list[oci.cloud_guard.models.DetectorConfiguration]
        """
        self._configurations = configurations

    @property
    def condition(self):
        """
        Gets the condition of this DetectorDetails.

        :return: The condition of this DetectorDetails.
        :rtype: oci.cloud_guard.models.Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this DetectorDetails.

        :param condition: The condition of this DetectorDetails.
        :type: oci.cloud_guard.models.Condition
        """
        self._condition = condition

    @property
    def labels(self):
        """
        Gets the labels of this DetectorDetails.
        User-defined labels for a detector rule


        :return: The labels of this DetectorDetails.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this DetectorDetails.
        User-defined labels for a detector rule


        :param labels: The labels of this DetectorDetails.
        :type: list[str]
        """
        self._labels = labels

    @property
    def is_configuration_allowed(self):
        """
        Gets the is_configuration_allowed of this DetectorDetails.
        Can the rule be configured?


        :return: The is_configuration_allowed of this DetectorDetails.
        :rtype: bool
        """
        return self._is_configuration_allowed

    @is_configuration_allowed.setter
    def is_configuration_allowed(self, is_configuration_allowed):
        """
        Sets the is_configuration_allowed of this DetectorDetails.
        Can the rule be configured?


        :param is_configuration_allowed: The is_configuration_allowed of this DetectorDetails.
        :type: bool
        """
        self._is_configuration_allowed = is_configuration_allowed

    @property
    def problem_threshold(self):
        """
        Gets the problem_threshold of this DetectorDetails.
        The point at which an elevated resource risk score creates a problem


        :return: The problem_threshold of this DetectorDetails.
        :rtype: int
        """
        return self._problem_threshold

    @problem_threshold.setter
    def problem_threshold(self, problem_threshold):
        """
        Sets the problem_threshold of this DetectorDetails.
        The point at which an elevated resource risk score creates a problem


        :param problem_threshold: The problem_threshold of this DetectorDetails.
        :type: int
        """
        self._problem_threshold = problem_threshold

    @property
    def target_types(self):
        """
        Gets the target_types of this DetectorDetails.
        List of target types for which the detector rule is applicable


        :return: The target_types of this DetectorDetails.
        :rtype: list[str]
        """
        return self._target_types

    @target_types.setter
    def target_types(self, target_types):
        """
        Sets the target_types of this DetectorDetails.
        List of target types for which the detector rule is applicable


        :param target_types: The target_types of this DetectorDetails.
        :type: list[str]
        """
        self._target_types = target_types

    @property
    def sighting_types(self):
        """
        Gets the sighting_types of this DetectorDetails.
        List of sighting types


        :return: The sighting_types of this DetectorDetails.
        :rtype: list[oci.cloud_guard.models.SightingType]
        """
        return self._sighting_types

    @sighting_types.setter
    def sighting_types(self, sighting_types):
        """
        Sets the sighting_types of this DetectorDetails.
        List of sighting types


        :param sighting_types: The sighting_types of this DetectorDetails.
        :type: list[oci.cloud_guard.models.SightingType]
        """
        self._sighting_types = sighting_types

    @property
    def description(self):
        """
        Gets the description of this DetectorDetails.
        Description for detector recipe detector rule


        :return: The description of this DetectorDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DetectorDetails.
        Description for detector recipe detector rule


        :param description: The description of this DetectorDetails.
        :type: str
        """
        self._description = description

    @property
    def recommendation(self):
        """
        Gets the recommendation of this DetectorDetails.
        Recommendation for detector recipe detector rule


        :return: The recommendation of this DetectorDetails.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """
        Sets the recommendation of this DetectorDetails.
        Recommendation for detector recipe detector rule


        :param recommendation: The recommendation of this DetectorDetails.
        :type: str
        """
        self._recommendation = recommendation

    @property
    def data_source_id(self):
        """
        Gets the data_source_id of this DetectorDetails.
        The ID of the attached data source


        :return: The data_source_id of this DetectorDetails.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """
        Sets the data_source_id of this DetectorDetails.
        The ID of the attached data source


        :param data_source_id: The data_source_id of this DetectorDetails.
        :type: str
        """
        self._data_source_id = data_source_id

    @property
    def entities_mappings(self):
        """
        Gets the entities_mappings of this DetectorDetails.
        Data source entities mapping for a detector rule


        :return: The entities_mappings of this DetectorDetails.
        :rtype: list[oci.cloud_guard.models.EntitiesMapping]
        """
        return self._entities_mappings

    @entities_mappings.setter
    def entities_mappings(self, entities_mappings):
        """
        Sets the entities_mappings of this DetectorDetails.
        Data source entities mapping for a detector rule


        :param entities_mappings: The entities_mappings of this DetectorDetails.
        :type: list[oci.cloud_guard.models.EntitiesMapping]
        """
        self._entities_mappings = entities_mappings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
