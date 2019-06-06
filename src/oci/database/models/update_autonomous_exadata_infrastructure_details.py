# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousExadataInfrastructureDetails(object):
    """
    Describes the modification parameters for the Autonomous Exadata Infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAutonomousExadataInfrastructureDetails.
        :type display_name: str

        :param maintenance_window_details:
            The value to assign to the maintenance_window_details property of this UpdateAutonomousExadataInfrastructureDetails.
        :type maintenance_window_details: MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutonomousExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutonomousExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'maintenance_window_details': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'maintenance_window_details': 'maintenanceWindowDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._maintenance_window_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutonomousExadataInfrastructureDetails.
        The display name is a user-friendly name for the Autonomous Exadata Infrastructure. The display name does not have to be unique.


        :return: The display_name of this UpdateAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutonomousExadataInfrastructureDetails.
        The display name is a user-friendly name for the Autonomous Exadata Infrastructure. The display name does not have to be unique.


        :param display_name: The display_name of this UpdateAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def maintenance_window_details(self):
        """
        Gets the maintenance_window_details of this UpdateAutonomousExadataInfrastructureDetails.

        :return: The maintenance_window_details of this UpdateAutonomousExadataInfrastructureDetails.
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window_details

    @maintenance_window_details.setter
    def maintenance_window_details(self, maintenance_window_details):
        """
        Sets the maintenance_window_details of this UpdateAutonomousExadataInfrastructureDetails.

        :param maintenance_window_details: The maintenance_window_details of this UpdateAutonomousExadataInfrastructureDetails.
        :type: MaintenanceWindow
        """
        self._maintenance_window_details = maintenance_window_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAutonomousExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAutonomousExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAutonomousExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAutonomousExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAutonomousExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAutonomousExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAutonomousExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutonomousExadataInfrastructureDetails.
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
