# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEsxiHostDetails(object):
    """
    Details of the ESXi host to add to the SDDC.
    """

    #: A constant which can be used with the current_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "HOUR"
    CURRENT_SKU_HOUR = "HOUR"

    #: A constant which can be used with the current_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "MONTH"
    CURRENT_SKU_MONTH = "MONTH"

    #: A constant which can be used with the current_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "ONE_YEAR"
    CURRENT_SKU_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the current_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "THREE_YEARS"
    CURRENT_SKU_THREE_YEARS = "THREE_YEARS"

    #: A constant which can be used with the next_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "HOUR"
    NEXT_SKU_HOUR = "HOUR"

    #: A constant which can be used with the next_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "MONTH"
    NEXT_SKU_MONTH = "MONTH"

    #: A constant which can be used with the next_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "ONE_YEAR"
    NEXT_SKU_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the next_sku property of a CreateEsxiHostDetails.
    #: This constant has a value of "THREE_YEARS"
    NEXT_SKU_THREE_YEARS = "THREE_YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEsxiHostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sddc_id:
            The value to assign to the sddc_id property of this CreateEsxiHostDetails.
        :type sddc_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateEsxiHostDetails.
        :type display_name: str

        :param current_sku:
            The value to assign to the current_sku property of this CreateEsxiHostDetails.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"
        :type current_sku: str

        :param next_sku:
            The value to assign to the next_sku property of this CreateEsxiHostDetails.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"
        :type next_sku: str

        :param compute_availability_domain:
            The value to assign to the compute_availability_domain property of this CreateEsxiHostDetails.
        :type compute_availability_domain: str

        :param failed_esxi_host_id:
            The value to assign to the failed_esxi_host_id property of this CreateEsxiHostDetails.
        :type failed_esxi_host_id: str

        :param host_shape_name:
            The value to assign to the host_shape_name property of this CreateEsxiHostDetails.
        :type host_shape_name: str

        :param host_ocpu_count:
            The value to assign to the host_ocpu_count property of this CreateEsxiHostDetails.
        :type host_ocpu_count: float

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this CreateEsxiHostDetails.
        :type capacity_reservation_id: str

        :param non_upgraded_esxi_host_id:
            The value to assign to the non_upgraded_esxi_host_id property of this CreateEsxiHostDetails.
        :type non_upgraded_esxi_host_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEsxiHostDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEsxiHostDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'sddc_id': 'str',
            'display_name': 'str',
            'current_sku': 'str',
            'next_sku': 'str',
            'compute_availability_domain': 'str',
            'failed_esxi_host_id': 'str',
            'host_shape_name': 'str',
            'host_ocpu_count': 'float',
            'capacity_reservation_id': 'str',
            'non_upgraded_esxi_host_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'sddc_id': 'sddcId',
            'display_name': 'displayName',
            'current_sku': 'currentSku',
            'next_sku': 'nextSku',
            'compute_availability_domain': 'computeAvailabilityDomain',
            'failed_esxi_host_id': 'failedEsxiHostId',
            'host_shape_name': 'hostShapeName',
            'host_ocpu_count': 'hostOcpuCount',
            'capacity_reservation_id': 'capacityReservationId',
            'non_upgraded_esxi_host_id': 'nonUpgradedEsxiHostId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._sddc_id = None
        self._display_name = None
        self._current_sku = None
        self._next_sku = None
        self._compute_availability_domain = None
        self._failed_esxi_host_id = None
        self._host_shape_name = None
        self._host_ocpu_count = None
        self._capacity_reservation_id = None
        self._non_upgraded_esxi_host_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this CreateEsxiHostDetails.
        The `OCID`__ of the SDDC to add the
        ESXi host to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this CreateEsxiHostDetails.
        The `OCID`__ of the SDDC to add the
        ESXi host to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this CreateEsxiHostDetails.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateEsxiHostDetails.
        A descriptive name for the ESXi host. It's changeable.
        Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

        If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used
        to name and incrementally number the ESXi host. For example, if you're creating the fourth
        ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display
        name is `MySDDC-4`.

        Avoid entering confidential information.


        :return: The display_name of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEsxiHostDetails.
        A descriptive name for the ESXi host. It's changeable.
        Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

        If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used
        to name and incrementally number the ESXi host. For example, if you're creating the fourth
        ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display
        name is `MySDDC-4`.

        Avoid entering confidential information.


        :param display_name: The display_name of this CreateEsxiHostDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def current_sku(self):
        """
        Gets the current_sku of this CreateEsxiHostDetails.
        The billing option currently used by the ESXi host.
        :func:`list_supported_skus`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"


        :return: The current_sku of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._current_sku

    @current_sku.setter
    def current_sku(self, current_sku):
        """
        Sets the current_sku of this CreateEsxiHostDetails.
        The billing option currently used by the ESXi host.
        :func:`list_supported_skus`.


        :param current_sku: The current_sku of this CreateEsxiHostDetails.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(current_sku, allowed_values):
            raise ValueError(
                "Invalid value for `current_sku`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._current_sku = current_sku

    @property
    def next_sku(self):
        """
        Gets the next_sku of this CreateEsxiHostDetails.
        The billing option to switch to after the existing billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
        :func:`list_supported_skus`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"


        :return: The next_sku of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._next_sku

    @next_sku.setter
    def next_sku(self, next_sku):
        """
        Sets the next_sku of this CreateEsxiHostDetails.
        The billing option to switch to after the existing billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
        :func:`list_supported_skus`.


        :param next_sku: The next_sku of this CreateEsxiHostDetails.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(next_sku, allowed_values):
            raise ValueError(
                "Invalid value for `next_sku`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._next_sku = next_sku

    @property
    def compute_availability_domain(self):
        """
        Gets the compute_availability_domain of this CreateEsxiHostDetails.
        The availability domain to create the ESXi host in.
        If keep empty, for AD-specific SDDC, new ESXi host will be created in the same availability domain;
        for multi-AD SDDC, new ESXi host will be auto assigned to the next availability domain following evenly distribution strategy.


        :return: The compute_availability_domain of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._compute_availability_domain

    @compute_availability_domain.setter
    def compute_availability_domain(self, compute_availability_domain):
        """
        Sets the compute_availability_domain of this CreateEsxiHostDetails.
        The availability domain to create the ESXi host in.
        If keep empty, for AD-specific SDDC, new ESXi host will be created in the same availability domain;
        for multi-AD SDDC, new ESXi host will be auto assigned to the next availability domain following evenly distribution strategy.


        :param compute_availability_domain: The compute_availability_domain of this CreateEsxiHostDetails.
        :type: str
        """
        self._compute_availability_domain = compute_availability_domain

    @property
    def failed_esxi_host_id(self):
        """
        Gets the failed_esxi_host_id of this CreateEsxiHostDetails.
        The `OCID`__ of the ESXi host that
        is failed. This is an optional parameter. If this parameter is specified, a new ESXi
        host will be created to replace the failed one, and the `failedEsxiHostId` field
        will be updated in the newly created Esxi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The failed_esxi_host_id of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._failed_esxi_host_id

    @failed_esxi_host_id.setter
    def failed_esxi_host_id(self, failed_esxi_host_id):
        """
        Sets the failed_esxi_host_id of this CreateEsxiHostDetails.
        The `OCID`__ of the ESXi host that
        is failed. This is an optional parameter. If this parameter is specified, a new ESXi
        host will be created to replace the failed one, and the `failedEsxiHostId` field
        will be updated in the newly created Esxi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param failed_esxi_host_id: The failed_esxi_host_id of this CreateEsxiHostDetails.
        :type: str
        """
        self._failed_esxi_host_id = failed_esxi_host_id

    @property
    def host_shape_name(self):
        """
        Gets the host_shape_name of this CreateEsxiHostDetails.
        The compute shape name of the ESXi host.
        :func:`list_supported_host_shapes`.


        :return: The host_shape_name of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._host_shape_name

    @host_shape_name.setter
    def host_shape_name(self, host_shape_name):
        """
        Sets the host_shape_name of this CreateEsxiHostDetails.
        The compute shape name of the ESXi host.
        :func:`list_supported_host_shapes`.


        :param host_shape_name: The host_shape_name of this CreateEsxiHostDetails.
        :type: str
        """
        self._host_shape_name = host_shape_name

    @property
    def host_ocpu_count(self):
        """
        Gets the host_ocpu_count of this CreateEsxiHostDetails.
        The OCPU count of the ESXi host.


        :return: The host_ocpu_count of this CreateEsxiHostDetails.
        :rtype: float
        """
        return self._host_ocpu_count

    @host_ocpu_count.setter
    def host_ocpu_count(self, host_ocpu_count):
        """
        Sets the host_ocpu_count of this CreateEsxiHostDetails.
        The OCPU count of the ESXi host.


        :param host_ocpu_count: The host_ocpu_count of this CreateEsxiHostDetails.
        :type: float
        """
        self._host_ocpu_count = host_ocpu_count

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this CreateEsxiHostDetails.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The capacity_reservation_id of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this CreateEsxiHostDetails.
        The `OCID`__ of the Capacity Reservation.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param capacity_reservation_id: The capacity_reservation_id of this CreateEsxiHostDetails.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

    @property
    def non_upgraded_esxi_host_id(self):
        """
        Gets the non_upgraded_esxi_host_id of this CreateEsxiHostDetails.
        The `OCID`__ of the ESXi host that
        will be upgraded. This is an optional parameter. If this parameter
        is specified, an ESXi host with new version will be created to replace the
        original one, and the `nonUpgradedEsxiHostId` field will be updated in the newly
        created Esxi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The non_upgraded_esxi_host_id of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._non_upgraded_esxi_host_id

    @non_upgraded_esxi_host_id.setter
    def non_upgraded_esxi_host_id(self, non_upgraded_esxi_host_id):
        """
        Sets the non_upgraded_esxi_host_id of this CreateEsxiHostDetails.
        The `OCID`__ of the ESXi host that
        will be upgraded. This is an optional parameter. If this parameter
        is specified, an ESXi host with new version will be created to replace the
        original one, and the `nonUpgradedEsxiHostId` field will be updated in the newly
        created Esxi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param non_upgraded_esxi_host_id: The non_upgraded_esxi_host_id of this CreateEsxiHostDetails.
        :type: str
        """
        self._non_upgraded_esxi_host_id = non_upgraded_esxi_host_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateEsxiHostDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateEsxiHostDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateEsxiHostDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateEsxiHostDetails.
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
