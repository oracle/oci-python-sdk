# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVmClusterDetails(object):
    """
    Details for updating the VM cluster.
    """

    #: A constant which can be used with the license_model property of a UpdateVmClusterDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateVmClusterDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVmClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateVmClusterDetails.
        :type cpu_core_count: int

        :param license_model:
            The value to assign to the license_model property of this UpdateVmClusterDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this UpdateVmClusterDetails.
        :type ssh_public_keys: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVmClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVmClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'license_model': 'str',
            'ssh_public_keys': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'license_model': 'licenseModel',
            'ssh_public_keys': 'sshPublicKeys',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._cpu_core_count = None
        self._license_model = None
        self._ssh_public_keys = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateVmClusterDetails.
        The number of CPU cores to enable for the VM cluster.


        :return: The cpu_core_count of this UpdateVmClusterDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateVmClusterDetails.
        The number of CPU cores to enable for the VM cluster.


        :param cpu_core_count: The cpu_core_count of this UpdateVmClusterDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def license_model(self):
        """
        Gets the license_model of this UpdateVmClusterDetails.
        The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateVmClusterDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateVmClusterDetails.
        The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this UpdateVmClusterDetails.
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
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this UpdateVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :return: The ssh_public_keys of this UpdateVmClusterDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this UpdateVmClusterDetails.
        The public key portion of one or more key pairs used for SSH access to the VM cluster.


        :param ssh_public_keys: The ssh_public_keys of this UpdateVmClusterDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateVmClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVmClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateVmClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateVmClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVmClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateVmClusterDetails.
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
