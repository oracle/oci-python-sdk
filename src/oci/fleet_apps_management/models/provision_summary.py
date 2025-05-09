# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProvisionSummary(object):
    """
    Summary information about a FamProvision.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProvisionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProvisionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ProvisionSummary.
        :type display_name: str

        :param provision_description:
            The value to assign to the provision_description property of this ProvisionSummary.
        :type provision_description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProvisionSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ProvisionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProvisionSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProvisionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ProvisionSummary.
        :type lifecycle_details: str

        :param package_catalog_item_id:
            The value to assign to the package_catalog_item_id property of this ProvisionSummary.
        :type package_catalog_item_id: str

        :param config_catalog_item_id:
            The value to assign to the config_catalog_item_id property of this ProvisionSummary.
        :type config_catalog_item_id: str

        :param package_catalog_item_display_name:
            The value to assign to the package_catalog_item_display_name property of this ProvisionSummary.
        :type package_catalog_item_display_name: str

        :param package_catalog_item_listing_id:
            The value to assign to the package_catalog_item_listing_id property of this ProvisionSummary.
        :type package_catalog_item_listing_id: str

        :param package_catalog_item_listing_version:
            The value to assign to the package_catalog_item_listing_version property of this ProvisionSummary.
        :type package_catalog_item_listing_version: str

        :param config_catalog_item_display_name:
            The value to assign to the config_catalog_item_display_name property of this ProvisionSummary.
        :type config_catalog_item_display_name: str

        :param config_catalog_item_listing_id:
            The value to assign to the config_catalog_item_listing_id property of this ProvisionSummary.
        :type config_catalog_item_listing_id: str

        :param config_catalog_item_listing_version:
            The value to assign to the config_catalog_item_listing_version property of this ProvisionSummary.
        :type config_catalog_item_listing_version: str

        :param stack_id:
            The value to assign to the stack_id property of this ProvisionSummary.
        :type stack_id: str

        :param fleet_id:
            The value to assign to the fleet_id property of this ProvisionSummary.
        :type fleet_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProvisionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ProvisionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ProvisionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'provision_description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'package_catalog_item_id': 'str',
            'config_catalog_item_id': 'str',
            'package_catalog_item_display_name': 'str',
            'package_catalog_item_listing_id': 'str',
            'package_catalog_item_listing_version': 'str',
            'config_catalog_item_display_name': 'str',
            'config_catalog_item_listing_id': 'str',
            'config_catalog_item_listing_version': 'str',
            'stack_id': 'str',
            'fleet_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'provision_description': 'provisionDescription',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'package_catalog_item_id': 'packageCatalogItemId',
            'config_catalog_item_id': 'configCatalogItemId',
            'package_catalog_item_display_name': 'packageCatalogItemDisplayName',
            'package_catalog_item_listing_id': 'packageCatalogItemListingId',
            'package_catalog_item_listing_version': 'packageCatalogItemListingVersion',
            'config_catalog_item_display_name': 'configCatalogItemDisplayName',
            'config_catalog_item_listing_id': 'configCatalogItemListingId',
            'config_catalog_item_listing_version': 'configCatalogItemListingVersion',
            'stack_id': 'stackId',
            'fleet_id': 'fleetId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._display_name = None
        self._provision_description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._package_catalog_item_id = None
        self._config_catalog_item_id = None
        self._package_catalog_item_display_name = None
        self._package_catalog_item_listing_id = None
        self._package_catalog_item_listing_version = None
        self._config_catalog_item_display_name = None
        self._config_catalog_item_listing_id = None
        self._config_catalog_item_listing_version = None
        self._stack_id = None
        self._fleet_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProvisionSummary.
        The `OCID`__ of the FamProvision.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ProvisionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProvisionSummary.
        The `OCID`__ of the FamProvision.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ProvisionSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ProvisionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this ProvisionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProvisionSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this ProvisionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def provision_description(self):
        """
        **[Required]** Gets the provision_description of this ProvisionSummary.
        A description of the provision.


        :return: The provision_description of this ProvisionSummary.
        :rtype: str
        """
        return self._provision_description

    @provision_description.setter
    def provision_description(self, provision_description):
        """
        Sets the provision_description of this ProvisionSummary.
        A description of the provision.


        :param provision_description: The provision_description of this ProvisionSummary.
        :type: str
        """
        self._provision_description = provision_description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProvisionSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ProvisionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProvisionSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ProvisionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ProvisionSummary.
        The date and time the FamProvision was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ProvisionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProvisionSummary.
        The date and time the FamProvision was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ProvisionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ProvisionSummary.
        The date and time the FamProvision was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ProvisionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProvisionSummary.
        The date and time the FamProvision was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ProvisionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ProvisionSummary.
        The current state of the FamProvision.


        :return: The lifecycle_state of this ProvisionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProvisionSummary.
        The current state of the FamProvision.


        :param lifecycle_state: The lifecycle_state of this ProvisionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ProvisionSummary.
        A message that describes the current state of the FamProvision in more detail. For example,
        can be used to provide actionable information for a resource in the Failed state.


        :return: The lifecycle_details of this ProvisionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ProvisionSummary.
        A message that describes the current state of the FamProvision in more detail. For example,
        can be used to provide actionable information for a resource in the Failed state.


        :param lifecycle_details: The lifecycle_details of this ProvisionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def package_catalog_item_id(self):
        """
        **[Required]** Gets the package_catalog_item_id of this ProvisionSummary.
        The `OCID`__ of the Catalog Item.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The package_catalog_item_id of this ProvisionSummary.
        :rtype: str
        """
        return self._package_catalog_item_id

    @package_catalog_item_id.setter
    def package_catalog_item_id(self, package_catalog_item_id):
        """
        Sets the package_catalog_item_id of this ProvisionSummary.
        The `OCID`__ of the Catalog Item.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param package_catalog_item_id: The package_catalog_item_id of this ProvisionSummary.
        :type: str
        """
        self._package_catalog_item_id = package_catalog_item_id

    @property
    def config_catalog_item_id(self):
        """
        **[Required]** Gets the config_catalog_item_id of this ProvisionSummary.
        A `OCID`__ of the Catalog Item to a file with key/value pairs to set up variables for createStack API.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The config_catalog_item_id of this ProvisionSummary.
        :rtype: str
        """
        return self._config_catalog_item_id

    @config_catalog_item_id.setter
    def config_catalog_item_id(self, config_catalog_item_id):
        """
        Sets the config_catalog_item_id of this ProvisionSummary.
        A `OCID`__ of the Catalog Item to a file with key/value pairs to set up variables for createStack API.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param config_catalog_item_id: The config_catalog_item_id of this ProvisionSummary.
        :type: str
        """
        self._config_catalog_item_id = config_catalog_item_id

    @property
    def package_catalog_item_display_name(self):
        """
        **[Required]** Gets the package_catalog_item_display_name of this ProvisionSummary.
        A display Name of the Catalog Item in the Catalog.


        :return: The package_catalog_item_display_name of this ProvisionSummary.
        :rtype: str
        """
        return self._package_catalog_item_display_name

    @package_catalog_item_display_name.setter
    def package_catalog_item_display_name(self, package_catalog_item_display_name):
        """
        Sets the package_catalog_item_display_name of this ProvisionSummary.
        A display Name of the Catalog Item in the Catalog.


        :param package_catalog_item_display_name: The package_catalog_item_display_name of this ProvisionSummary.
        :type: str
        """
        self._package_catalog_item_display_name = package_catalog_item_display_name

    @property
    def package_catalog_item_listing_id(self):
        """
        **[Required]** Gets the package_catalog_item_listing_id of this ProvisionSummary.
        A listing ID of the Catalog Item in the Catalog.


        :return: The package_catalog_item_listing_id of this ProvisionSummary.
        :rtype: str
        """
        return self._package_catalog_item_listing_id

    @package_catalog_item_listing_id.setter
    def package_catalog_item_listing_id(self, package_catalog_item_listing_id):
        """
        Sets the package_catalog_item_listing_id of this ProvisionSummary.
        A listing ID of the Catalog Item in the Catalog.


        :param package_catalog_item_listing_id: The package_catalog_item_listing_id of this ProvisionSummary.
        :type: str
        """
        self._package_catalog_item_listing_id = package_catalog_item_listing_id

    @property
    def package_catalog_item_listing_version(self):
        """
        **[Required]** Gets the package_catalog_item_listing_version of this ProvisionSummary.
        A listing version of the Catalog Item in the Catalog.


        :return: The package_catalog_item_listing_version of this ProvisionSummary.
        :rtype: str
        """
        return self._package_catalog_item_listing_version

    @package_catalog_item_listing_version.setter
    def package_catalog_item_listing_version(self, package_catalog_item_listing_version):
        """
        Sets the package_catalog_item_listing_version of this ProvisionSummary.
        A listing version of the Catalog Item in the Catalog.


        :param package_catalog_item_listing_version: The package_catalog_item_listing_version of this ProvisionSummary.
        :type: str
        """
        self._package_catalog_item_listing_version = package_catalog_item_listing_version

    @property
    def config_catalog_item_display_name(self):
        """
        **[Required]** Gets the config_catalog_item_display_name of this ProvisionSummary.
        A display Name of the Catalog Item in the Catalog.


        :return: The config_catalog_item_display_name of this ProvisionSummary.
        :rtype: str
        """
        return self._config_catalog_item_display_name

    @config_catalog_item_display_name.setter
    def config_catalog_item_display_name(self, config_catalog_item_display_name):
        """
        Sets the config_catalog_item_display_name of this ProvisionSummary.
        A display Name of the Catalog Item in the Catalog.


        :param config_catalog_item_display_name: The config_catalog_item_display_name of this ProvisionSummary.
        :type: str
        """
        self._config_catalog_item_display_name = config_catalog_item_display_name

    @property
    def config_catalog_item_listing_id(self):
        """
        **[Required]** Gets the config_catalog_item_listing_id of this ProvisionSummary.
        A listing ID of the Catalog Item in the Catalog.


        :return: The config_catalog_item_listing_id of this ProvisionSummary.
        :rtype: str
        """
        return self._config_catalog_item_listing_id

    @config_catalog_item_listing_id.setter
    def config_catalog_item_listing_id(self, config_catalog_item_listing_id):
        """
        Sets the config_catalog_item_listing_id of this ProvisionSummary.
        A listing ID of the Catalog Item in the Catalog.


        :param config_catalog_item_listing_id: The config_catalog_item_listing_id of this ProvisionSummary.
        :type: str
        """
        self._config_catalog_item_listing_id = config_catalog_item_listing_id

    @property
    def config_catalog_item_listing_version(self):
        """
        **[Required]** Gets the config_catalog_item_listing_version of this ProvisionSummary.
        A listing version of the Catalog Item in the Catalog.


        :return: The config_catalog_item_listing_version of this ProvisionSummary.
        :rtype: str
        """
        return self._config_catalog_item_listing_version

    @config_catalog_item_listing_version.setter
    def config_catalog_item_listing_version(self, config_catalog_item_listing_version):
        """
        Sets the config_catalog_item_listing_version of this ProvisionSummary.
        A listing version of the Catalog Item in the Catalog.


        :param config_catalog_item_listing_version: The config_catalog_item_listing_version of this ProvisionSummary.
        :type: str
        """
        self._config_catalog_item_listing_version = config_catalog_item_listing_version

    @property
    def stack_id(self):
        """
        **[Required]** Gets the stack_id of this ProvisionSummary.
        The `OCID`__ of the RMS Stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stack_id of this ProvisionSummary.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """
        Sets the stack_id of this ProvisionSummary.
        The `OCID`__ of the RMS Stack.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stack_id: The stack_id of this ProvisionSummary.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this ProvisionSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this ProvisionSummary.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this ProvisionSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this ProvisionSummary.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ProvisionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ProvisionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProvisionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ProvisionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ProvisionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ProvisionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProvisionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ProvisionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ProvisionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ProvisionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ProvisionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ProvisionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
