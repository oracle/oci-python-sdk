# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchAutonomousExadataInfrastructureDetails(object):
    """
    Describes the input parameters to launch a new Autonomous Exadata Infrastructure.
    """

    #: A constant which can be used with the license_model property of a LaunchAutonomousExadataInfrastructureDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a LaunchAutonomousExadataInfrastructureDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchAutonomousExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LaunchAutonomousExadataInfrastructureDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LaunchAutonomousExadataInfrastructureDetails.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this LaunchAutonomousExadataInfrastructureDetails.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this LaunchAutonomousExadataInfrastructureDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this LaunchAutonomousExadataInfrastructureDetails.
        :type nsg_ids: list[str]

        :param shape:
            The value to assign to the shape property of this LaunchAutonomousExadataInfrastructureDetails.
        :type shape: str

        :param domain:
            The value to assign to the domain property of this LaunchAutonomousExadataInfrastructureDetails.
        :type domain: str

        :param license_model:
            The value to assign to the license_model property of this LaunchAutonomousExadataInfrastructureDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param maintenance_window_details:
            The value to assign to the maintenance_window_details property of this LaunchAutonomousExadataInfrastructureDetails.
        :type maintenance_window_details: oci.database.models.MaintenanceWindow

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LaunchAutonomousExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LaunchAutonomousExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'shape': 'str',
            'domain': 'str',
            'license_model': 'str',
            'maintenance_window_details': 'MaintenanceWindow',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'shape': 'shape',
            'domain': 'domain',
            'license_model': 'licenseModel',
            'maintenance_window_details': 'maintenanceWindowDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._availability_domain = None
        self._subnet_id = None
        self._nsg_ids = None
        self._shape = None
        self._domain = None
        self._license_model = None
        self._maintenance_window_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LaunchAutonomousExadataInfrastructureDetails.
        The `OCID`__ of the compartment the Autonomous Exadata Infrastructure belongs in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LaunchAutonomousExadataInfrastructureDetails.
        The `OCID`__ of the compartment the Autonomous Exadata Infrastructure belongs in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this LaunchAutonomousExadataInfrastructureDetails.
        The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.


        :return: The display_name of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchAutonomousExadataInfrastructureDetails.
        The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.


        :param display_name: The display_name of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this LaunchAutonomousExadataInfrastructureDetails.
        The availability domain where the Autonomous Exadata Infrastructure is located.


        :return: The availability_domain of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LaunchAutonomousExadataInfrastructureDetails.
        The availability domain where the Autonomous Exadata Infrastructure is located.


        :param availability_domain: The availability_domain of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this LaunchAutonomousExadataInfrastructureDetails.
        The `OCID`__ of the subnet the Autonomous Exadata Infrastructure is associated with.

        **Subnet Restrictions:**
        - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this LaunchAutonomousExadataInfrastructureDetails.
        The `OCID`__ of the subnet the Autonomous Exadata Infrastructure is associated with.

        **Subnet Restrictions:**
        - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this LaunchAutonomousExadataInfrastructureDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this LaunchAutonomousExadataInfrastructureDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this LaunchAutonomousExadataInfrastructureDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this LaunchAutonomousExadataInfrastructureDetails.
        The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores, memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.


        :return: The shape of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this LaunchAutonomousExadataInfrastructureDetails.
        The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores, memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.


        :param shape: The shape of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._shape = shape

    @property
    def domain(self):
        """
        Gets the domain of this LaunchAutonomousExadataInfrastructureDetails.
        A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN
        Resolver is enabled for the specified subnet, the domain name for the subnet is used
        (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.


        :return: The domain of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this LaunchAutonomousExadataInfrastructureDetails.
        A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN
        Resolver is enabled for the specified subnet, the domain name for the subnet is used
        (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.


        :param domain: The domain of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        self._domain = domain

    @property
    def license_model(self):
        """
        Gets the license_model of this LaunchAutonomousExadataInfrastructureDetails.
        The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this LaunchAutonomousExadataInfrastructureDetails.
        The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this LaunchAutonomousExadataInfrastructureDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    @property
    def maintenance_window_details(self):
        """
        Gets the maintenance_window_details of this LaunchAutonomousExadataInfrastructureDetails.

        :return: The maintenance_window_details of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window_details

    @maintenance_window_details.setter
    def maintenance_window_details(self, maintenance_window_details):
        """
        Sets the maintenance_window_details of this LaunchAutonomousExadataInfrastructureDetails.

        :param maintenance_window_details: The maintenance_window_details of this LaunchAutonomousExadataInfrastructureDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window_details = maintenance_window_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LaunchAutonomousExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LaunchAutonomousExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LaunchAutonomousExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LaunchAutonomousExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LaunchAutonomousExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LaunchAutonomousExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LaunchAutonomousExadataInfrastructureDetails.
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
