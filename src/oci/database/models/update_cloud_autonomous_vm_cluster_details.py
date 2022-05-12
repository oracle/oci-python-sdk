# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCloudAutonomousVmClusterDetails(object):
    """
    Details for updating the cloud Autonomous VM cluster.
    """

    #: A constant which can be used with the license_model property of a UpdateCloudAutonomousVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateCloudAutonomousVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCloudAutonomousVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateCloudAutonomousVmClusterDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateCloudAutonomousVmClusterDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this UpdateCloudAutonomousVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateCloudAutonomousVmClusterDetails.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCloudAutonomousVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCloudAutonomousVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._license_model = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateCloudAutonomousVmClusterDetails.
        User defined description of the cloud Autonomous VM cluster.


        :return: The description of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCloudAutonomousVmClusterDetails.
        User defined description of the cloud Autonomous VM cluster.


        :param description: The description of this UpdateCloudAutonomousVmClusterDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCloudAutonomousVmClusterDetails.
        The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.


        :return: The display_name of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCloudAutonomousVmClusterDetails.
        The user-friendly name for the cloud Autonomous VM cluster. The name does not need to be unique.


        :param display_name: The display_name of this UpdateCloudAutonomousVmClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateCloudAutonomousVmClusterDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateCloudAutonomousVmClusterDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param license_model: The license_model of this UpdateCloudAutonomousVmClusterDetails.
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
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateCloudAutonomousVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateCloudAutonomousVmClusterDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateCloudAutonomousVmClusterDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCloudAutonomousVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCloudAutonomousVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCloudAutonomousVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCloudAutonomousVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCloudAutonomousVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCloudAutonomousVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCloudAutonomousVmClusterDetails.
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
