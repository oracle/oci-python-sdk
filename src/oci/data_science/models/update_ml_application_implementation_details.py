# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMlApplicationImplementationDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMlApplicationImplementationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_migration_destinations:
            The value to assign to the allowed_migration_destinations property of this UpdateMlApplicationImplementationDetails.
        :type allowed_migration_destinations: list[str]

        :param logging:
            The value to assign to the logging property of this UpdateMlApplicationImplementationDetails.
        :type logging: oci.data_science.models.ImplementationLogging

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMlApplicationImplementationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMlApplicationImplementationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'allowed_migration_destinations': 'list[str]',
            'logging': 'ImplementationLogging',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'allowed_migration_destinations': 'allowedMigrationDestinations',
            'logging': 'logging',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._allowed_migration_destinations = None
        self._logging = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def allowed_migration_destinations(self):
        """
        Gets the allowed_migration_destinations of this UpdateMlApplicationImplementationDetails.
        List of ML Application Implementation OCIDs for which migration from this implementation is allowed. Migration means that if consumers change implementation for their instances to implementation with OCID from this list, instance components will be updated in place otherwise new instance components are created based on the new implementation and old instance components are removed.


        :return: The allowed_migration_destinations of this UpdateMlApplicationImplementationDetails.
        :rtype: list[str]
        """
        return self._allowed_migration_destinations

    @allowed_migration_destinations.setter
    def allowed_migration_destinations(self, allowed_migration_destinations):
        """
        Sets the allowed_migration_destinations of this UpdateMlApplicationImplementationDetails.
        List of ML Application Implementation OCIDs for which migration from this implementation is allowed. Migration means that if consumers change implementation for their instances to implementation with OCID from this list, instance components will be updated in place otherwise new instance components are created based on the new implementation and old instance components are removed.


        :param allowed_migration_destinations: The allowed_migration_destinations of this UpdateMlApplicationImplementationDetails.
        :type: list[str]
        """
        self._allowed_migration_destinations = allowed_migration_destinations

    @property
    def logging(self):
        """
        Gets the logging of this UpdateMlApplicationImplementationDetails.

        :return: The logging of this UpdateMlApplicationImplementationDetails.
        :rtype: oci.data_science.models.ImplementationLogging
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """
        Sets the logging of this UpdateMlApplicationImplementationDetails.

        :param logging: The logging of this UpdateMlApplicationImplementationDetails.
        :type: oci.data_science.models.ImplementationLogging
        """
        self._logging = logging

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMlApplicationImplementationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateMlApplicationImplementationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMlApplicationImplementationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateMlApplicationImplementationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMlApplicationImplementationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateMlApplicationImplementationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMlApplicationImplementationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateMlApplicationImplementationDetails.
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
