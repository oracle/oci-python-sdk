# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplianceExportJobDetails(object):
    """
    CreateApplianceExportJobDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplianceExportJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateApplianceExportJobDetails.
        :type compartment_id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CreateApplianceExportJobDetails.
        :type bucket_name: str

        :param display_name:
            The value to assign to the display_name property of this CreateApplianceExportJobDetails.
        :type display_name: str

        :param prefix:
            The value to assign to the prefix property of this CreateApplianceExportJobDetails.
        :type prefix: str

        :param range_start:
            The value to assign to the range_start property of this CreateApplianceExportJobDetails.
        :type range_start: str

        :param range_end:
            The value to assign to the range_end property of this CreateApplianceExportJobDetails.
        :type range_end: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this CreateApplianceExportJobDetails.
        :type customer_shipping_address: oci.dts.models.ShippingAddress

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateApplianceExportJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateApplianceExportJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'bucket_name': 'str',
            'display_name': 'str',
            'prefix': 'str',
            'range_start': 'str',
            'range_end': 'str',
            'customer_shipping_address': 'ShippingAddress',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'bucket_name': 'bucketName',
            'display_name': 'displayName',
            'prefix': 'prefix',
            'range_start': 'rangeStart',
            'range_end': 'rangeEnd',
            'customer_shipping_address': 'customerShippingAddress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._bucket_name = None
        self._display_name = None
        self._prefix = None
        self._range_start = None
        self._range_end = None
        self._customer_shipping_address = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateApplianceExportJobDetails.

        :return: The compartment_id of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateApplianceExportJobDetails.

        :param compartment_id: The compartment_id of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CreateApplianceExportJobDetails.

        :return: The bucket_name of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CreateApplianceExportJobDetails.

        :param bucket_name: The bucket_name of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateApplianceExportJobDetails.

        :return: The display_name of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateApplianceExportJobDetails.

        :param display_name: The display_name of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def prefix(self):
        """
        Gets the prefix of this CreateApplianceExportJobDetails.
        List of objects with names matching this prefix would be part of this export job.


        :return: The prefix of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CreateApplianceExportJobDetails.
        List of objects with names matching this prefix would be part of this export job.


        :param prefix: The prefix of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._prefix = prefix

    @property
    def range_start(self):
        """
        Gets the range_start of this CreateApplianceExportJobDetails.
        Object names returned by a list query must be greater or equal to this parameter.


        :return: The range_start of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """
        Sets the range_start of this CreateApplianceExportJobDetails.
        Object names returned by a list query must be greater or equal to this parameter.


        :param range_start: The range_start of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._range_start = range_start

    @property
    def range_end(self):
        """
        Gets the range_end of this CreateApplianceExportJobDetails.
        Object names returned by a list query must be strictly less than this parameter.


        :return: The range_end of this CreateApplianceExportJobDetails.
        :rtype: str
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """
        Sets the range_end of this CreateApplianceExportJobDetails.
        Object names returned by a list query must be strictly less than this parameter.


        :param range_end: The range_end of this CreateApplianceExportJobDetails.
        :type: str
        """
        self._range_end = range_end

    @property
    def customer_shipping_address(self):
        """
        **[Required]** Gets the customer_shipping_address of this CreateApplianceExportJobDetails.

        :return: The customer_shipping_address of this CreateApplianceExportJobDetails.
        :rtype: oci.dts.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this CreateApplianceExportJobDetails.

        :param customer_shipping_address: The customer_shipping_address of this CreateApplianceExportJobDetails.
        :type: oci.dts.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateApplianceExportJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateApplianceExportJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateApplianceExportJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateApplianceExportJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateApplianceExportJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateApplianceExportJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateApplianceExportJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateApplianceExportJobDetails.
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
