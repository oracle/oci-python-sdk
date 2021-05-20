# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EsxiHost(object):
    """
    An ESXi host is a node in an SDDC. At a minimum, each SDDC has 3 ESXi hosts
    that are used to implement a functioning VMware environment.

    In terms of implementation, an ESXi host is a Compute instance that
    is configured with the chosen bundle of VMware software.

    Notice that an `EsxiHost` object has its own OCID (`id`), and a separate
    attribute for the OCID of the Compute instance (`computeInstanceId`).
    """

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EsxiHost.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the current_sku property of a EsxiHost.
    #: This constant has a value of "HOUR"
    CURRENT_SKU_HOUR = "HOUR"

    #: A constant which can be used with the current_sku property of a EsxiHost.
    #: This constant has a value of "MONTH"
    CURRENT_SKU_MONTH = "MONTH"

    #: A constant which can be used with the current_sku property of a EsxiHost.
    #: This constant has a value of "ONE_YEAR"
    CURRENT_SKU_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the current_sku property of a EsxiHost.
    #: This constant has a value of "THREE_YEARS"
    CURRENT_SKU_THREE_YEARS = "THREE_YEARS"

    #: A constant which can be used with the next_sku property of a EsxiHost.
    #: This constant has a value of "HOUR"
    NEXT_SKU_HOUR = "HOUR"

    #: A constant which can be used with the next_sku property of a EsxiHost.
    #: This constant has a value of "MONTH"
    NEXT_SKU_MONTH = "MONTH"

    #: A constant which can be used with the next_sku property of a EsxiHost.
    #: This constant has a value of "ONE_YEAR"
    NEXT_SKU_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the next_sku property of a EsxiHost.
    #: This constant has a value of "THREE_YEARS"
    NEXT_SKU_THREE_YEARS = "THREE_YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new EsxiHost object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EsxiHost.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this EsxiHost.
        :type display_name: str

        :param sddc_id:
            The value to assign to the sddc_id property of this EsxiHost.
        :type sddc_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EsxiHost.
        :type compartment_id: str

        :param compute_instance_id:
            The value to assign to the compute_instance_id property of this EsxiHost.
        :type compute_instance_id: str

        :param time_created:
            The value to assign to the time_created property of this EsxiHost.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EsxiHost.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EsxiHost.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param current_sku:
            The value to assign to the current_sku property of this EsxiHost.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type current_sku: str

        :param next_sku:
            The value to assign to the next_sku property of this EsxiHost.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type next_sku: str

        :param billing_contract_end_date:
            The value to assign to the billing_contract_end_date property of this EsxiHost.
        :type billing_contract_end_date: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EsxiHost.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EsxiHost.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'sddc_id': 'str',
            'compartment_id': 'str',
            'compute_instance_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'current_sku': 'str',
            'next_sku': 'str',
            'billing_contract_end_date': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'sddc_id': 'sddcId',
            'compartment_id': 'compartmentId',
            'compute_instance_id': 'computeInstanceId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'current_sku': 'currentSku',
            'next_sku': 'nextSku',
            'billing_contract_end_date': 'billingContractEndDate',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._sddc_id = None
        self._compartment_id = None
        self._compute_instance_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._current_sku = None
        self._next_sku = None
        self._billing_contract_end_date = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EsxiHost.
        The `OCID`__ of the ESXi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this EsxiHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EsxiHost.
        The `OCID`__ of the ESXi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this EsxiHost.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this EsxiHost.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this EsxiHost.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EsxiHost.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this EsxiHost.
        :type: str
        """
        self._display_name = display_name

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this EsxiHost.
        The `OCID`__ of the SDDC that the
        ESXi host belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this EsxiHost.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this EsxiHost.
        The `OCID`__ of the SDDC that the
        ESXi host belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this EsxiHost.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this EsxiHost.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EsxiHost.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EsxiHost.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EsxiHost.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compute_instance_id(self):
        """
        Gets the compute_instance_id of this EsxiHost.
        In terms of implementation, an ESXi host is a Compute instance that
        is configured with the chosen bundle of VMware software. The `computeInstanceId`
        is the `OCID`__ of that Compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compute_instance_id of this EsxiHost.
        :rtype: str
        """
        return self._compute_instance_id

    @compute_instance_id.setter
    def compute_instance_id(self, compute_instance_id):
        """
        Sets the compute_instance_id of this EsxiHost.
        In terms of implementation, an ESXi host is a Compute instance that
        is configured with the chosen bundle of VMware software. The `computeInstanceId`
        is the `OCID`__ of that Compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compute_instance_id: The compute_instance_id of this EsxiHost.
        :type: str
        """
        self._compute_instance_id = compute_instance_id

    @property
    def time_created(self):
        """
        Gets the time_created of this EsxiHost.
        The date and time the ESXi host was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EsxiHost.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EsxiHost.
        The date and time the ESXi host was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EsxiHost.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EsxiHost.
        The date and time the ESXi host was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EsxiHost.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EsxiHost.
        The date and time the ESXi host was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EsxiHost.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EsxiHost.
        The current state of the ESXi host.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EsxiHost.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EsxiHost.
        The current state of the ESXi host.


        :param lifecycle_state: The lifecycle_state of this EsxiHost.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def current_sku(self):
        """
        **[Required]** Gets the current_sku of this EsxiHost.
        Billing option selected during SDDC creation.
        Oracle Cloud Infrastructure VMware Solution supports the following billing interval SKUs:
        HOUR, MONTH, ONE_YEAR, and THREE_YEARS.
        :func:`list_supported_skus`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The current_sku of this EsxiHost.
        :rtype: str
        """
        return self._current_sku

    @current_sku.setter
    def current_sku(self, current_sku):
        """
        Sets the current_sku of this EsxiHost.
        Billing option selected during SDDC creation.
        Oracle Cloud Infrastructure VMware Solution supports the following billing interval SKUs:
        HOUR, MONTH, ONE_YEAR, and THREE_YEARS.
        :func:`list_supported_skus`.


        :param current_sku: The current_sku of this EsxiHost.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(current_sku, allowed_values):
            current_sku = 'UNKNOWN_ENUM_VALUE'
        self._current_sku = current_sku

    @property
    def next_sku(self):
        """
        **[Required]** Gets the next_sku of this EsxiHost.
        Billing option to switch to once existing billing cycle ends.
        :func:`list_supported_skus`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The next_sku of this EsxiHost.
        :rtype: str
        """
        return self._next_sku

    @next_sku.setter
    def next_sku(self, next_sku):
        """
        Sets the next_sku of this EsxiHost.
        Billing option to switch to once existing billing cycle ends.
        :func:`list_supported_skus`.


        :param next_sku: The next_sku of this EsxiHost.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(next_sku, allowed_values):
            next_sku = 'UNKNOWN_ENUM_VALUE'
        self._next_sku = next_sku

    @property
    def billing_contract_end_date(self):
        """
        **[Required]** Gets the billing_contract_end_date of this EsxiHost.
        Current billing cycle end date. If nextSku is different from existing SKU, then we switch to newSKu
        after this contractEndDate
        Example: `2016-08-25T21:10:29.600Z`


        :return: The billing_contract_end_date of this EsxiHost.
        :rtype: datetime
        """
        return self._billing_contract_end_date

    @billing_contract_end_date.setter
    def billing_contract_end_date(self, billing_contract_end_date):
        """
        Sets the billing_contract_end_date of this EsxiHost.
        Current billing cycle end date. If nextSku is different from existing SKU, then we switch to newSKu
        after this contractEndDate
        Example: `2016-08-25T21:10:29.600Z`


        :param billing_contract_end_date: The billing_contract_end_date of this EsxiHost.
        :type: datetime
        """
        self._billing_contract_end_date = billing_contract_end_date

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this EsxiHost.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this EsxiHost.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EsxiHost.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this EsxiHost.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this EsxiHost.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this EsxiHost.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EsxiHost.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this EsxiHost.
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
