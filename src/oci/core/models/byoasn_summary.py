# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ByoasnSummary(object):
    """
    Information about a `Byoasn` resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ByoasnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param asn:
            The value to assign to the asn property of this ByoasnSummary.
        :type asn: int

        :param compartment_id:
            The value to assign to the compartment_id property of this ByoasnSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ByoasnSummary.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ByoasnSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ByoasnSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this ByoasnSummary.
        :type system_tags: dict(str, dict(str, object))

        :param id:
            The value to assign to the id property of this ByoasnSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ByoasnSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ByoasnSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'asn': 'int',
            'compartment_id': 'str',
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'asn': 'asn',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }
        self._asn = None
        self._compartment_id = None
        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def asn(self):
        """
        **[Required]** Gets the asn of this ByoasnSummary.
        The Autonomous System Number (ASN) you are importing to the Oracle cloud.


        :return: The asn of this ByoasnSummary.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """
        Sets the asn of this ByoasnSummary.
        The Autonomous System Number (ASN) you are importing to the Oracle cloud.


        :param asn: The asn of this ByoasnSummary.
        :type: int
        """
        self._asn = asn

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ByoasnSummary.
        The `OCID`__ of the compartment containing the `Byoasn` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ByoasnSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ByoasnSummary.
        The `OCID`__ of the compartment containing the `Byoasn` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ByoasnSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ByoasnSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ByoasnSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ByoasnSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ByoasnSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ByoasnSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ByoasnSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ByoasnSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ByoasnSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ByoasnSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ByoasnSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ByoasnSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ByoasnSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ByoasnSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The system_tags of this ByoasnSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ByoasnSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param system_tags: The system_tags of this ByoasnSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ByoasnSummary.
        The `OCID`__ of the `Byoasn` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ByoasnSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ByoasnSummary.
        The `OCID`__ of the `Byoasn` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ByoasnSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ByoasnSummary.
        The `Byoasn` resource's current state.


        :return: The lifecycle_state of this ByoasnSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ByoasnSummary.
        The `Byoasn` resource's current state.


        :param lifecycle_state: The lifecycle_state of this ByoasnSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this ByoasnSummary.
        The date and time the `Byoasn` resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ByoasnSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ByoasnSummary.
        The date and time the `Byoasn` resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ByoasnSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
