# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCloudExadataInfrastructureDetails(object):
    """
    Updates the cloud Exadata infrastructure. Applies to Exadata Cloud Service instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCloudExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateCloudExadataInfrastructureDetails.
        :type display_name: str

        :param maintenance_window:
            The value to assign to the maintenance_window property of this UpdateCloudExadataInfrastructureDetails.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param compute_count:
            The value to assign to the compute_count property of this UpdateCloudExadataInfrastructureDetails.
        :type compute_count: int

        :param storage_count:
            The value to assign to the storage_count property of this UpdateCloudExadataInfrastructureDetails.
        :type storage_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCloudExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCloudExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param customer_contacts:
            The value to assign to the customer_contacts property of this UpdateCloudExadataInfrastructureDetails.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        """
        self.swagger_types = {
            'display_name': 'str',
            'maintenance_window': 'MaintenanceWindow',
            'compute_count': 'int',
            'storage_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'customer_contacts': 'list[CustomerContact]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'maintenance_window': 'maintenanceWindow',
            'compute_count': 'computeCount',
            'storage_count': 'storageCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'customer_contacts': 'customerContacts'
        }

        self._display_name = None
        self._maintenance_window = None
        self._compute_count = None
        self._storage_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._customer_contacts = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCloudExadataInfrastructureDetails.
        The user-friendly name for the cloud Exadata infrastructure. The name does not need to be unique.


        :return: The display_name of this UpdateCloudExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCloudExadataInfrastructureDetails.
        The user-friendly name for the cloud Exadata infrastructure. The name does not need to be unique.


        :param display_name: The display_name of this UpdateCloudExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this UpdateCloudExadataInfrastructureDetails.

        :return: The maintenance_window of this UpdateCloudExadataInfrastructureDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this UpdateCloudExadataInfrastructureDetails.

        :param maintenance_window: The maintenance_window of this UpdateCloudExadataInfrastructureDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def compute_count(self):
        """
        Gets the compute_count of this UpdateCloudExadataInfrastructureDetails.
        The number of compute servers for the cloud Exadata infrastructure.


        :return: The compute_count of this UpdateCloudExadataInfrastructureDetails.
        :rtype: int
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this UpdateCloudExadataInfrastructureDetails.
        The number of compute servers for the cloud Exadata infrastructure.


        :param compute_count: The compute_count of this UpdateCloudExadataInfrastructureDetails.
        :type: int
        """
        self._compute_count = compute_count

    @property
    def storage_count(self):
        """
        Gets the storage_count of this UpdateCloudExadataInfrastructureDetails.
        The number of storage servers for the cloud Exadata infrastructure.


        :return: The storage_count of this UpdateCloudExadataInfrastructureDetails.
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        """
        Sets the storage_count of this UpdateCloudExadataInfrastructureDetails.
        The number of storage servers for the cloud Exadata infrastructure.


        :param storage_count: The storage_count of this UpdateCloudExadataInfrastructureDetails.
        :type: int
        """
        self._storage_count = storage_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCloudExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCloudExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCloudExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCloudExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCloudExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCloudExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCloudExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCloudExadataInfrastructureDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this UpdateCloudExadataInfrastructureDetails.
        Customer contacts. Setting this to an empty list removes all customer contact information (email addresses) for the specified OCI Database service resource.


        :return: The customer_contacts of this UpdateCloudExadataInfrastructureDetails.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this UpdateCloudExadataInfrastructureDetails.
        Customer contacts. Setting this to an empty list removes all customer contact information (email addresses) for the specified OCI Database service resource.


        :param customer_contacts: The customer_contacts of this UpdateCloudExadataInfrastructureDetails.
        :type: list[oci.database.models.CustomerContact]
        """
        self._customer_contacts = customer_contacts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
