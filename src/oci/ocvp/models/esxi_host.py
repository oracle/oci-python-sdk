# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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

        :param failed_esxi_host_id:
            The value to assign to the failed_esxi_host_id property of this EsxiHost.
        :type failed_esxi_host_id: str

        :param replacement_esxi_host_id:
            The value to assign to the replacement_esxi_host_id property of this EsxiHost.
        :type replacement_esxi_host_id: str

        :param grace_period_end_date:
            The value to assign to the grace_period_end_date property of this EsxiHost.
        :type grace_period_end_date: datetime

        :param vmware_software_version:
            The value to assign to the vmware_software_version property of this EsxiHost.
        :type vmware_software_version: str

        :param non_upgraded_esxi_host_id:
            The value to assign to the non_upgraded_esxi_host_id property of this EsxiHost.
        :type non_upgraded_esxi_host_id: str

        :param upgraded_replacement_esxi_host_id:
            The value to assign to the upgraded_replacement_esxi_host_id property of this EsxiHost.
        :type upgraded_replacement_esxi_host_id: str

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this EsxiHost.
        :type compute_availability_domain: str

        :param host_shape_name:
            The value to assign to the host_shape_name property of this EsxiHost.
        :type host_shape_name: str

        :param host_ocpu_count:
            The value to assign to the host_ocpu_count property of this EsxiHost.
        :type host_ocpu_count: float

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this EsxiHost.
        :type capacity_reservation_id: str

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
            'failed_esxi_host_id': 'str',
            'replacement_esxi_host_id': 'str',
            'grace_period_end_date': 'datetime',
            'vmware_software_version': 'str',
            'non_upgraded_esxi_host_id': 'str',
            'upgraded_replacement_esxi_host_id': 'str',
            'compute_availability_domain': 'str',
            'host_shape_name': 'str',
            'host_ocpu_count': 'float',
            'capacity_reservation_id': 'str',
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
            'failed_esxi_host_id': 'failedEsxiHostId',
            'replacement_esxi_host_id': 'replacementEsxiHostId',
            'grace_period_end_date': 'gracePeriodEndDate',
            'vmware_software_version': 'vmwareSoftwareVersion',
            'non_upgraded_esxi_host_id': 'nonUpgradedEsxiHostId',
            'upgraded_replacement_esxi_host_id': 'upgradedReplacementEsxiHostId',
            'compute_availability_domain': 'computeAvailabilityDomain',
            'host_shape_name': 'hostShapeName',
            'host_ocpu_count': 'hostOcpuCount',
            'capacity_reservation_id': 'capacityReservationId',
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
        self._failed_esxi_host_id = None
        self._replacement_esxi_host_id = None
        self._grace_period_end_date = None
        self._vmware_software_version = None
        self._non_upgraded_esxi_host_id = None
        self._upgraded_replacement_esxi_host_id = None
        self._compute_availability_domain = None
        self._host_shape_name = None
        self._host_ocpu_count = None
        self._capacity_reservation_id = None
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
        The billing option currently used by the ESXi host.
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
        The billing option currently used by the ESXi host.
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
        The billing option to switch to after the current billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
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
        The billing option to switch to after the current billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
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
        Current billing cycle end date. If the value in `currentSku` and `nextSku` are different, the value specified in `nextSku`
        becomes the new `currentSKU` when the `contractEndDate` is reached.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The billing_contract_end_date of this EsxiHost.
        :rtype: datetime
        """
        return self._billing_contract_end_date

    @billing_contract_end_date.setter
    def billing_contract_end_date(self, billing_contract_end_date):
        """
        Sets the billing_contract_end_date of this EsxiHost.
        Current billing cycle end date. If the value in `currentSku` and `nextSku` are different, the value specified in `nextSku`
        becomes the new `currentSKU` when the `contractEndDate` is reached.
        Example: `2016-08-25T21:10:29.600Z`


        :param billing_contract_end_date: The billing_contract_end_date of this EsxiHost.
        :type: datetime
        """
        self._billing_contract_end_date = billing_contract_end_date

    @property
    def failed_esxi_host_id(self):
        """
        Gets the failed_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that failed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The failed_esxi_host_id of this EsxiHost.
        :rtype: str
        """
        return self._failed_esxi_host_id

    @failed_esxi_host_id.setter
    def failed_esxi_host_id(self, failed_esxi_host_id):
        """
        Sets the failed_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that failed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param failed_esxi_host_id: The failed_esxi_host_id of this EsxiHost.
        :type: str
        """
        self._failed_esxi_host_id = failed_esxi_host_id

    @property
    def replacement_esxi_host_id(self):
        """
        Gets the replacement_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        is created to replace the failed host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The replacement_esxi_host_id of this EsxiHost.
        :rtype: str
        """
        return self._replacement_esxi_host_id

    @replacement_esxi_host_id.setter
    def replacement_esxi_host_id(self, replacement_esxi_host_id):
        """
        Sets the replacement_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        is created to replace the failed host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param replacement_esxi_host_id: The replacement_esxi_host_id of this EsxiHost.
        :type: str
        """
        self._replacement_esxi_host_id = replacement_esxi_host_id

    @property
    def grace_period_end_date(self):
        """
        Gets the grace_period_end_date of this EsxiHost.
        The date and time when the new esxi host should start billing cycle.
        `RFC3339`__.
        Example: `2021-07-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The grace_period_end_date of this EsxiHost.
        :rtype: datetime
        """
        return self._grace_period_end_date

    @grace_period_end_date.setter
    def grace_period_end_date(self, grace_period_end_date):
        """
        Sets the grace_period_end_date of this EsxiHost.
        The date and time when the new esxi host should start billing cycle.
        `RFC3339`__.
        Example: `2021-07-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param grace_period_end_date: The grace_period_end_date of this EsxiHost.
        :type: datetime
        """
        self._grace_period_end_date = grace_period_end_date

    @property
    def vmware_software_version(self):
        """
        **[Required]** Gets the vmware_software_version of this EsxiHost.
        The version of VMware software that the Oracle Cloud VMware Solution installed on the ESXi hosts.


        :return: The vmware_software_version of this EsxiHost.
        :rtype: str
        """
        return self._vmware_software_version

    @vmware_software_version.setter
    def vmware_software_version(self, vmware_software_version):
        """
        Sets the vmware_software_version of this EsxiHost.
        The version of VMware software that the Oracle Cloud VMware Solution installed on the ESXi hosts.


        :param vmware_software_version: The vmware_software_version of this EsxiHost.
        :type: str
        """
        self._vmware_software_version = vmware_software_version

    @property
    def non_upgraded_esxi_host_id(self):
        """
        Gets the non_upgraded_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        will be upgraded.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The non_upgraded_esxi_host_id of this EsxiHost.
        :rtype: str
        """
        return self._non_upgraded_esxi_host_id

    @non_upgraded_esxi_host_id.setter
    def non_upgraded_esxi_host_id(self, non_upgraded_esxi_host_id):
        """
        Sets the non_upgraded_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        will be upgraded.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param non_upgraded_esxi_host_id: The non_upgraded_esxi_host_id of this EsxiHost.
        :type: str
        """
        self._non_upgraded_esxi_host_id = non_upgraded_esxi_host_id

    @property
    def upgraded_replacement_esxi_host_id(self):
        """
        Gets the upgraded_replacement_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        is newly created to upgrade the original host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The upgraded_replacement_esxi_host_id of this EsxiHost.
        :rtype: str
        """
        return self._upgraded_replacement_esxi_host_id

    @upgraded_replacement_esxi_host_id.setter
    def upgraded_replacement_esxi_host_id(self, upgraded_replacement_esxi_host_id):
        """
        Sets the upgraded_replacement_esxi_host_id of this EsxiHost.
        The `OCID`__ of the ESXi host that
        is newly created to upgrade the original host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param upgraded_replacement_esxi_host_id: The upgraded_replacement_esxi_host_id of this EsxiHost.
        :type: str
        """
        self._upgraded_replacement_esxi_host_id = upgraded_replacement_esxi_host_id

    @property
    def compute_availability_domain(self):
        """
        **[Required]** Gets the compute_availability_domain of this EsxiHost.
        The availability domain of the ESXi host.


        :return: The compute_availability_domain of this EsxiHost.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this EsxiHost.
        The availability domain of the ESXi host.


        :param compute_availability_domain: The compute_availability_domain of this EsxiHost.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def host_shape_name(self):
        """
        **[Required]** Gets the host_shape_name of this EsxiHost.
        The compute shape name of the ESXi host.
        :func:`list_supported_host_shapes`.


        :return: The host_shape_name of this EsxiHost.
        :rtype: str
        """
        return self._host_shape_name

    @host_shape_name.setter
    def host_shape_name(self, host_shape_name):
        """
        Sets the host_shape_name of this EsxiHost.
        The compute shape name of the ESXi host.
        :func:`list_supported_host_shapes`.


        :param host_shape_name: The host_shape_name of this EsxiHost.
        :type: str
        """
        self._host_shape_name = host_shape_name

    @property
    def host_ocpu_count(self):
        """
        Gets the host_ocpu_count of this EsxiHost.
        The OCPU count of the ESXi host.


        :return: The host_ocpu_count of this EsxiHost.
        :rtype: float
        """
        return self._host_ocpu_count

    @host_ocpu_count.setter
    def host_ocpu_count(self, host_ocpu_count):
        """
        Sets the host_ocpu_count of this EsxiHost.
        The OCPU count of the ESXi host.


        :param host_ocpu_count: The host_ocpu_count of this EsxiHost.
        :type: float
        """
        self._host_ocpu_count = host_ocpu_count

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this EsxiHost.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The capacity_reservation_id of this EsxiHost.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this EsxiHost.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param capacity_reservation_id: The capacity_reservation_id of this EsxiHost.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

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
