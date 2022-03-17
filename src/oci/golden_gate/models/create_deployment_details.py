# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeploymentDetails(object):
    """
    The information about a new Deployment.
    """

    #: A constant which can be used with the license_model property of a CreateDeploymentDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateDeploymentDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the deployment_type property of a CreateDeploymentDetails.
    #: This constant has a value of "OGG"
    DEPLOYMENT_TYPE_OGG = "OGG"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDeploymentDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateDeploymentDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param description:
            The value to assign to the description property of this CreateDeploymentDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDeploymentDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param deployment_backup_id:
            The value to assign to the deployment_backup_id property of this CreateDeploymentDetails.
        :type deployment_backup_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDeploymentDetails.
        :type subnet_id: str

        :param fqdn:
            The value to assign to the fqdn property of this CreateDeploymentDetails.
        :type fqdn: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDeploymentDetails.
        :type nsg_ids: list[str]

        :param is_public:
            The value to assign to the is_public property of this CreateDeploymentDetails.
        :type is_public: bool

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateDeploymentDetails.
        :type cpu_core_count: int

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateDeploymentDetails.
        :type is_auto_scaling_enabled: bool

        :param deployment_type:
            The value to assign to the deployment_type property of this CreateDeploymentDetails.
            Allowed values for this property are: "OGG"
        :type deployment_type: str

        :param ogg_data:
            The value to assign to the ogg_data property of this CreateDeploymentDetails.
        :type ogg_data: oci.golden_gate.models.CreateOggDeploymentDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'license_model': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'deployment_backup_id': 'str',
            'subnet_id': 'str',
            'fqdn': 'str',
            'nsg_ids': 'list[str]',
            'is_public': 'bool',
            'cpu_core_count': 'int',
            'is_auto_scaling_enabled': 'bool',
            'deployment_type': 'str',
            'ogg_data': 'CreateOggDeploymentDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'deployment_backup_id': 'deploymentBackupId',
            'subnet_id': 'subnetId',
            'fqdn': 'fqdn',
            'nsg_ids': 'nsgIds',
            'is_public': 'isPublic',
            'cpu_core_count': 'cpuCoreCount',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'deployment_type': 'deploymentType',
            'ogg_data': 'oggData'
        }

        self._display_name = None
        self._license_model = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deployment_backup_id = None
        self._subnet_id = None
        self._fqdn = None
        self._nsg_ids = None
        self._is_public = None
        self._cpu_core_count = None
        self._is_auto_scaling_enabled = None
        self._deployment_type = None
        self._ogg_data = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDeploymentDetails.
        An object's Display Name.


        :return: The display_name of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeploymentDetails.
        An object's Display Name.


        :param display_name: The display_name of this CreateDeploymentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_model(self):
        """
        **[Required]** Gets the license_model of this CreateDeploymentDetails.
        The Oracle license model that applies to a Deployment.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateDeploymentDetails.
        The Oracle license model that applies to a Deployment.


        :param license_model: The license_model of this CreateDeploymentDetails.
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
    def description(self):
        """
        Gets the description of this CreateDeploymentDetails.
        Metadata about this specific object.


        :return: The description of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDeploymentDetails.
        Metadata about this specific object.


        :param description: The description of this CreateDeploymentDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDeploymentDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDeploymentDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDeploymentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeploymentDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDeploymentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeploymentDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDeploymentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeploymentDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDeploymentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeploymentDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDeploymentDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def deployment_backup_id(self):
        """
        Gets the deployment_backup_id of this CreateDeploymentDetails.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_backup_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._deployment_backup_id

    @deployment_backup_id.setter
    def deployment_backup_id(self, deployment_backup_id):
        """
        Sets the deployment_backup_id of this CreateDeploymentDetails.
        The `OCID`__ of the backup being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_backup_id: The deployment_backup_id of this CreateDeploymentDetails.
        :type: str
        """
        self._deployment_backup_id = deployment_backup_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateDeploymentDetails.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDeploymentDetails.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateDeploymentDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def fqdn(self):
        """
        Gets the fqdn of this CreateDeploymentDetails.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :return: The fqdn of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this CreateDeploymentDetails.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :param fqdn: The fqdn of this CreateDeploymentDetails.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDeploymentDetails.
        An array of `Network Security Group`__ OCIDs used to define network access for a deployment.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm


        :return: The nsg_ids of this CreateDeploymentDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDeploymentDetails.
        An array of `Network Security Group`__ OCIDs used to define network access for a deployment.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm


        :param nsg_ids: The nsg_ids of this CreateDeploymentDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def is_public(self):
        """
        Gets the is_public of this CreateDeploymentDetails.
        True if this object is publicly available.


        :return: The is_public of this CreateDeploymentDetails.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this CreateDeploymentDetails.
        True if this object is publicly available.


        :param is_public: The is_public of this CreateDeploymentDetails.
        :type: bool
        """
        self._is_public = is_public

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this CreateDeploymentDetails.
        The Minimum number of OCPUs to be made available for this Deployment.


        :return: The cpu_core_count of this CreateDeploymentDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateDeploymentDetails.
        The Minimum number of OCPUs to be made available for this Deployment.


        :param cpu_core_count: The cpu_core_count of this CreateDeploymentDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def is_auto_scaling_enabled(self):
        """
        **[Required]** Gets the is_auto_scaling_enabled of this CreateDeploymentDetails.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :return: The is_auto_scaling_enabled of this CreateDeploymentDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this CreateDeploymentDetails.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this CreateDeploymentDetails.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this CreateDeploymentDetails.
        The deployment type.

        Allowed values for this property are: "OGG"


        :return: The deployment_type of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this CreateDeploymentDetails.
        The deployment type.


        :param deployment_type: The deployment_type of this CreateDeploymentDetails.
        :type: str
        """
        allowed_values = ["OGG"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            raise ValueError(
                "Invalid value for `deployment_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._deployment_type = deployment_type

    @property
    def ogg_data(self):
        """
        Gets the ogg_data of this CreateDeploymentDetails.

        :return: The ogg_data of this CreateDeploymentDetails.
        :rtype: oci.golden_gate.models.CreateOggDeploymentDetails
        """
        return self._ogg_data

    @ogg_data.setter
    def ogg_data(self, ogg_data):
        """
        Sets the ogg_data of this CreateDeploymentDetails.

        :param ogg_data: The ogg_data of this CreateDeploymentDetails.
        :type: oci.golden_gate.models.CreateOggDeploymentDetails
        """
        self._ogg_data = ogg_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
