# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCloudExadataInfrastructureDetails(object):
    """
    Request to create cloud Exadata infrastructure. Applies to Exadata Cloud Service instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCloudExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateCloudExadataInfrastructureDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCloudExadataInfrastructureDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCloudExadataInfrastructureDetails.
        :type display_name: str

        :param shape:
            The value to assign to the shape property of this CreateCloudExadataInfrastructureDetails.
        :type shape: str

        :param compute_count:
            The value to assign to the compute_count property of this CreateCloudExadataInfrastructureDetails.
        :type compute_count: int

        :param storage_count:
            The value to assign to the storage_count property of this CreateCloudExadataInfrastructureDetails.
        :type storage_count: int

        :param maintenance_window:
            The value to assign to the maintenance_window property of this CreateCloudExadataInfrastructureDetails.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCloudExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCloudExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param customer_contacts:
            The value to assign to the customer_contacts property of this CreateCloudExadataInfrastructureDetails.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'shape': 'str',
            'compute_count': 'int',
            'storage_count': 'int',
            'maintenance_window': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'customer_contacts': 'list[CustomerContact]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'shape': 'shape',
            'compute_count': 'computeCount',
            'storage_count': 'storageCount',
            'maintenance_window': 'maintenanceWindow',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'customer_contacts': 'customerContacts'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._shape = None
        self._compute_count = None
        self._storage_count = None
        self._maintenance_window = None
        self._freeform_tags = None
        self._defined_tags = None
        self._customer_contacts = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateCloudExadataInfrastructureDetails.
        The availability domain where the cloud Exadata infrastructure is located.


        :return: The availability_domain of this CreateCloudExadataInfrastructureDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateCloudExadataInfrastructureDetails.
        The availability domain where the cloud Exadata infrastructure is located.


        :param availability_domain: The availability_domain of this CreateCloudExadataInfrastructureDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCloudExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCloudExadataInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCloudExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCloudExadataInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateCloudExadataInfrastructureDetails.
        The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.


        :return: The display_name of this CreateCloudExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCloudExadataInfrastructureDetails.
        The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.


        :param display_name: The display_name of this CreateCloudExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateCloudExadataInfrastructureDetails.
        The shape of the cloud Exadata infrastructure resource.


        :return: The shape of this CreateCloudExadataInfrastructureDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateCloudExadataInfrastructureDetails.
        The shape of the cloud Exadata infrastructure resource.


        :param shape: The shape of this CreateCloudExadataInfrastructureDetails.
        :type: str
        """
        self._shape = shape

    @property
    def compute_count(self):
        """
        Gets the compute_count of this CreateCloudExadataInfrastructureDetails.
        The number of compute servers for the cloud Exadata infrastructure.


        :return: The compute_count of this CreateCloudExadataInfrastructureDetails.
        :rtype: int
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this CreateCloudExadataInfrastructureDetails.
        The number of compute servers for the cloud Exadata infrastructure.


        :param compute_count: The compute_count of this CreateCloudExadataInfrastructureDetails.
        :type: int
        """
        self._compute_count = compute_count

    @property
    def storage_count(self):
        """
        Gets the storage_count of this CreateCloudExadataInfrastructureDetails.
        The number of storage servers for the cloud Exadata infrastructure.


        :return: The storage_count of this CreateCloudExadataInfrastructureDetails.
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        """
        Sets the storage_count of this CreateCloudExadataInfrastructureDetails.
        The number of storage servers for the cloud Exadata infrastructure.


        :param storage_count: The storage_count of this CreateCloudExadataInfrastructureDetails.
        :type: int
        """
        self._storage_count = storage_count

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this CreateCloudExadataInfrastructureDetails.

        :return: The maintenance_window of this CreateCloudExadataInfrastructureDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this CreateCloudExadataInfrastructureDetails.

        :param maintenance_window: The maintenance_window of this CreateCloudExadataInfrastructureDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCloudExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCloudExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCloudExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCloudExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCloudExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCloudExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCloudExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCloudExadataInfrastructureDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this CreateCloudExadataInfrastructureDetails.
        Customer contacts.


        :return: The customer_contacts of this CreateCloudExadataInfrastructureDetails.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this CreateCloudExadataInfrastructureDetails.
        Customer contacts.


        :param customer_contacts: The customer_contacts of this CreateCloudExadataInfrastructureDetails.
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
