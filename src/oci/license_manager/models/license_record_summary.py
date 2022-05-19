# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LicenseRecordSummary(object):
    """
    The license record summary.
    """

    #: A constant which can be used with the lifecycle_state property of a LicenseRecordSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LicenseRecordSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LicenseRecordSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the license_unit property of a LicenseRecordSummary.
    #: This constant has a value of "OCPU"
    LICENSE_UNIT_OCPU = "OCPU"

    #: A constant which can be used with the license_unit property of a LicenseRecordSummary.
    #: This constant has a value of "NAMED_USER_PLUS"
    LICENSE_UNIT_NAMED_USER_PLUS = "NAMED_USER_PLUS"

    #: A constant which can be used with the license_unit property of a LicenseRecordSummary.
    #: This constant has a value of "PROCESSORS"
    LICENSE_UNIT_PROCESSORS = "PROCESSORS"

    def __init__(self, **kwargs):
        """
        Initializes a new LicenseRecordSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LicenseRecordSummary.
        :type id: str

        :param product_license_id:
            The value to assign to the product_license_id property of this LicenseRecordSummary.
        :type product_license_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LicenseRecordSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LicenseRecordSummary.
        :type display_name: str

        :param product_id:
            The value to assign to the product_id property of this LicenseRecordSummary.
        :type product_id: str

        :param license_count:
            The value to assign to the license_count property of this LicenseRecordSummary.
        :type license_count: int

        :param expiration_date:
            The value to assign to the expiration_date property of this LicenseRecordSummary.
        :type expiration_date: datetime

        :param support_end_date:
            The value to assign to the support_end_date property of this LicenseRecordSummary.
        :type support_end_date: datetime

        :param is_unlimited:
            The value to assign to the is_unlimited property of this LicenseRecordSummary.
        :type is_unlimited: bool

        :param is_perpetual:
            The value to assign to the is_perpetual property of this LicenseRecordSummary.
        :type is_perpetual: bool

        :param time_created:
            The value to assign to the time_created property of this LicenseRecordSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LicenseRecordSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LicenseRecordSummary.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param license_unit:
            The value to assign to the license_unit property of this LicenseRecordSummary.
            Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_unit: str

        :param product_license:
            The value to assign to the product_license property of this LicenseRecordSummary.
        :type product_license: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LicenseRecordSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LicenseRecordSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this LicenseRecordSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'product_license_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'product_id': 'str',
            'license_count': 'int',
            'expiration_date': 'datetime',
            'support_end_date': 'datetime',
            'is_unlimited': 'bool',
            'is_perpetual': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'license_unit': 'str',
            'product_license': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'product_license_id': 'productLicenseId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'product_id': 'productId',
            'license_count': 'licenseCount',
            'expiration_date': 'expirationDate',
            'support_end_date': 'supportEndDate',
            'is_unlimited': 'isUnlimited',
            'is_perpetual': 'isPerpetual',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'license_unit': 'licenseUnit',
            'product_license': 'productLicense',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._product_license_id = None
        self._compartment_id = None
        self._display_name = None
        self._product_id = None
        self._license_count = None
        self._expiration_date = None
        self._support_end_date = None
        self._is_unlimited = None
        self._is_perpetual = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._license_unit = None
        self._product_license = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LicenseRecordSummary.
        The license record `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this LicenseRecordSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LicenseRecordSummary.
        The license record `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this LicenseRecordSummary.
        :type: str
        """
        self._id = id

    @property
    def product_license_id(self):
        """
        Gets the product_license_id of this LicenseRecordSummary.
        The product license `OCID`__ with which the license record is associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The product_license_id of this LicenseRecordSummary.
        :rtype: str
        """
        return self._product_license_id

    @product_license_id.setter
    def product_license_id(self, product_license_id):
        """
        Sets the product_license_id of this LicenseRecordSummary.
        The product license `OCID`__ with which the license record is associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param product_license_id: The product_license_id of this LicenseRecordSummary.
        :type: str
        """
        self._product_license_id = product_license_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LicenseRecordSummary.
        The compartment `OCID`__ where the license record is created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LicenseRecordSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LicenseRecordSummary.
        The compartment `OCID`__ where the license record is created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LicenseRecordSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LicenseRecordSummary.
        License record display name. Avoid entering confidential information.


        :return: The display_name of this LicenseRecordSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LicenseRecordSummary.
        License record display name. Avoid entering confidential information.


        :param display_name: The display_name of this LicenseRecordSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def product_id(self):
        """
        Gets the product_id of this LicenseRecordSummary.
        The license record product ID.


        :return: The product_id of this LicenseRecordSummary.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this LicenseRecordSummary.
        The license record product ID.


        :param product_id: The product_id of this LicenseRecordSummary.
        :type: str
        """
        self._product_id = product_id

    @property
    def license_count(self):
        """
        Gets the license_count of this LicenseRecordSummary.
        The number of license record units added by the user for the given license record.
        Default 1


        :return: The license_count of this LicenseRecordSummary.
        :rtype: int
        """
        return self._license_count

    @license_count.setter
    def license_count(self, license_count):
        """
        Sets the license_count of this LicenseRecordSummary.
        The number of license record units added by the user for the given license record.
        Default 1


        :param license_count: The license_count of this LicenseRecordSummary.
        :type: int
        """
        self._license_count = license_count

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this LicenseRecordSummary.
        The license record end date in `RFC 3339`__ format.
        date format.
        Example: `2018-09-12`

        __ https://tools.ietf.org/html/rfc3339


        :return: The expiration_date of this LicenseRecordSummary.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this LicenseRecordSummary.
        The license record end date in `RFC 3339`__ format.
        date format.
        Example: `2018-09-12`

        __ https://tools.ietf.org/html/rfc3339


        :param expiration_date: The expiration_date of this LicenseRecordSummary.
        :type: datetime
        """
        self._expiration_date = expiration_date

    @property
    def support_end_date(self):
        """
        Gets the support_end_date of this LicenseRecordSummary.
        The license record support end date in `RFC 3339`__ format.
        date format.
        Example: `2018-09-12`

        __ https://tools.ietf.org/html/rfc3339


        :return: The support_end_date of this LicenseRecordSummary.
        :rtype: datetime
        """
        return self._support_end_date

    @support_end_date.setter
    def support_end_date(self, support_end_date):
        """
        Sets the support_end_date of this LicenseRecordSummary.
        The license record support end date in `RFC 3339`__ format.
        date format.
        Example: `2018-09-12`

        __ https://tools.ietf.org/html/rfc3339


        :param support_end_date: The support_end_date of this LicenseRecordSummary.
        :type: datetime
        """
        self._support_end_date = support_end_date

    @property
    def is_unlimited(self):
        """
        **[Required]** Gets the is_unlimited of this LicenseRecordSummary.
        Specifies if the license count is unlimited.


        :return: The is_unlimited of this LicenseRecordSummary.
        :rtype: bool
        """
        return self._is_unlimited

    @is_unlimited.setter
    def is_unlimited(self, is_unlimited):
        """
        Sets the is_unlimited of this LicenseRecordSummary.
        Specifies if the license count is unlimited.


        :param is_unlimited: The is_unlimited of this LicenseRecordSummary.
        :type: bool
        """
        self._is_unlimited = is_unlimited

    @property
    def is_perpetual(self):
        """
        **[Required]** Gets the is_perpetual of this LicenseRecordSummary.
        Specifies if the license record term is perpertual.


        :return: The is_perpetual of this LicenseRecordSummary.
        :rtype: bool
        """
        return self._is_perpetual

    @is_perpetual.setter
    def is_perpetual(self, is_perpetual):
        """
        Sets the is_perpetual of this LicenseRecordSummary.
        Specifies if the license record term is perpertual.


        :param is_perpetual: The is_perpetual of this LicenseRecordSummary.
        :type: bool
        """
        self._is_perpetual = is_perpetual

    @property
    def time_created(self):
        """
        Gets the time_created of this LicenseRecordSummary.
        The time the license record was created. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this LicenseRecordSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LicenseRecordSummary.
        The time the license record was created. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this LicenseRecordSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LicenseRecordSummary.
        The time the license record was updated. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this LicenseRecordSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LicenseRecordSummary.
        The time the license record was updated. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this LicenseRecordSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LicenseRecordSummary.
        The current license record state.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LicenseRecordSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LicenseRecordSummary.
        The current license record state.


        :param lifecycle_state: The lifecycle_state of this LicenseRecordSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def license_unit(self):
        """
        Gets the license_unit of this LicenseRecordSummary.
        The product license unit.

        Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_unit of this LicenseRecordSummary.
        :rtype: str
        """
        return self._license_unit

    @license_unit.setter
    def license_unit(self, license_unit):
        """
        Sets the license_unit of this LicenseRecordSummary.
        The product license unit.


        :param license_unit: The license_unit of this LicenseRecordSummary.
        :type: str
        """
        allowed_values = ["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]
        if not value_allowed_none_or_none_sentinel(license_unit, allowed_values):
            license_unit = 'UNKNOWN_ENUM_VALUE'
        self._license_unit = license_unit

    @property
    def product_license(self):
        """
        Gets the product_license of this LicenseRecordSummary.
        The product license name with which the license record is associated.


        :return: The product_license of this LicenseRecordSummary.
        :rtype: str
        """
        return self._product_license

    @product_license.setter
    def product_license(self, product_license):
        """
        Sets the product_license of this LicenseRecordSummary.
        The product license name with which the license record is associated.


        :param product_license: The product_license of this LicenseRecordSummary.
        :type: str
        """
        self._product_license = product_license

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LicenseRecordSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LicenseRecordSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LicenseRecordSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LicenseRecordSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LicenseRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LicenseRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LicenseRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LicenseRecordSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this LicenseRecordSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this LicenseRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this LicenseRecordSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this LicenseRecordSummary.
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
