# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOceInstanceDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the instance_license_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "NEW"
    INSTANCE_LICENSE_TYPE_NEW = "NEW"

    #: A constant which can be used with the instance_license_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "BYOL"
    INSTANCE_LICENSE_TYPE_BYOL = "BYOL"

    #: A constant which can be used with the instance_license_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "PREMIUM"
    INSTANCE_LICENSE_TYPE_PREMIUM = "PREMIUM"

    #: A constant which can be used with the instance_license_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "STARTER"
    INSTANCE_LICENSE_TYPE_STARTER = "STARTER"

    #: A constant which can be used with the instance_usage_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "PRIMARY"
    INSTANCE_USAGE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the instance_usage_type property of a UpdateOceInstanceDetails.
    #: This constant has a value of "NONPRIMARY"
    INSTANCE_USAGE_TYPE_NONPRIMARY = "NONPRIMARY"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOceInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOceInstanceDetails.
        :type description: str

        :param waf_primary_domain:
            The value to assign to the waf_primary_domain property of this UpdateOceInstanceDetails.
        :type waf_primary_domain: str

        :param instance_license_type:
            The value to assign to the instance_license_type property of this UpdateOceInstanceDetails.
            Allowed values for this property are: "NEW", "BYOL", "PREMIUM", "STARTER"
        :type instance_license_type: str

        :param instance_usage_type:
            The value to assign to the instance_usage_type property of this UpdateOceInstanceDetails.
            Allowed values for this property are: "PRIMARY", "NONPRIMARY"
        :type instance_usage_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOceInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOceInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'waf_primary_domain': 'str',
            'instance_license_type': 'str',
            'instance_usage_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'waf_primary_domain': 'wafPrimaryDomain',
            'instance_license_type': 'instanceLicenseType',
            'instance_usage_type': 'instanceUsageType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._waf_primary_domain = None
        self._instance_license_type = None
        self._instance_usage_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateOceInstanceDetails.
        OceInstance description


        :return: The description of this UpdateOceInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateOceInstanceDetails.
        OceInstance description


        :param description: The description of this UpdateOceInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def waf_primary_domain(self):
        """
        Gets the waf_primary_domain of this UpdateOceInstanceDetails.
        Web Application Firewall(WAF) primary domain


        :return: The waf_primary_domain of this UpdateOceInstanceDetails.
        :rtype: str
        """
        return self._waf_primary_domain

    @waf_primary_domain.setter
    def waf_primary_domain(self, waf_primary_domain):
        """
        Sets the waf_primary_domain of this UpdateOceInstanceDetails.
        Web Application Firewall(WAF) primary domain


        :param waf_primary_domain: The waf_primary_domain of this UpdateOceInstanceDetails.
        :type: str
        """
        self._waf_primary_domain = waf_primary_domain

    @property
    def instance_license_type(self):
        """
        Gets the instance_license_type of this UpdateOceInstanceDetails.
        Flag indicating whether the instance license is new cloud or bring your own license

        Allowed values for this property are: "NEW", "BYOL", "PREMIUM", "STARTER"


        :return: The instance_license_type of this UpdateOceInstanceDetails.
        :rtype: str
        """
        return self._instance_license_type

    @instance_license_type.setter
    def instance_license_type(self, instance_license_type):
        """
        Sets the instance_license_type of this UpdateOceInstanceDetails.
        Flag indicating whether the instance license is new cloud or bring your own license


        :param instance_license_type: The instance_license_type of this UpdateOceInstanceDetails.
        :type: str
        """
        allowed_values = ["NEW", "BYOL", "PREMIUM", "STARTER"]
        if not value_allowed_none_or_none_sentinel(instance_license_type, allowed_values):
            raise ValueError(
                "Invalid value for `instance_license_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._instance_license_type = instance_license_type

    @property
    def instance_usage_type(self):
        """
        Gets the instance_usage_type of this UpdateOceInstanceDetails.
        Instance type based on its usage

        Allowed values for this property are: "PRIMARY", "NONPRIMARY"


        :return: The instance_usage_type of this UpdateOceInstanceDetails.
        :rtype: str
        """
        return self._instance_usage_type

    @instance_usage_type.setter
    def instance_usage_type(self, instance_usage_type):
        """
        Sets the instance_usage_type of this UpdateOceInstanceDetails.
        Instance type based on its usage


        :param instance_usage_type: The instance_usage_type of this UpdateOceInstanceDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "NONPRIMARY"]
        if not value_allowed_none_or_none_sentinel(instance_usage_type, allowed_values):
            raise ValueError(
                "Invalid value for `instance_usage_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._instance_usage_type = instance_usage_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOceInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOceInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOceInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOceInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOceInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOceInstanceDetails.
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
