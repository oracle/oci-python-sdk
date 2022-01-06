# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableSummary(object):
    """
    Summary of the table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TableSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TableSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TableSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this TableSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this TableSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TableSummary.
        :type time_updated: datetime

        :param table_limits:
            The value to assign to the table_limits property of this TableSummary.
        :type table_limits: oci.nosql.models.TableLimits

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TableSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TableSummary.
        :type lifecycle_details: str

        :param is_auto_reclaimable:
            The value to assign to the is_auto_reclaimable property of this TableSummary.
        :type is_auto_reclaimable: bool

        :param time_of_expiration:
            The value to assign to the time_of_expiration property of this TableSummary.
        :type time_of_expiration: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TableSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TableSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TableSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'table_limits': 'TableLimits',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_auto_reclaimable': 'bool',
            'time_of_expiration': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'table_limits': 'tableLimits',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_auto_reclaimable': 'isAutoReclaimable',
            'time_of_expiration': 'timeOfExpiration',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._time_created = None
        self._time_updated = None
        self._table_limits = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_auto_reclaimable = None
        self._time_of_expiration = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TableSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this TableSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TableSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this TableSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TableSummary.
        Compartment Identifier.


        :return: The compartment_id of this TableSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TableSummary.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this TableSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this TableSummary.
        Human-friendly table name, also immutable.


        :return: The name of this TableSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TableSummary.
        Human-friendly table name, also immutable.


        :param name: The name of this TableSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        Gets the time_created of this TableSummary.
        The time the the table was created. An RFC3339 formatted
        datetime string.


        :return: The time_created of this TableSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TableSummary.
        The time the the table was created. An RFC3339 formatted
        datetime string.


        :param time_created: The time_created of this TableSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TableSummary.
        The time the the table's metadata was last updated. An
        RFC3339 formatted datetime string.


        :return: The time_updated of this TableSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TableSummary.
        The time the the table's metadata was last updated. An
        RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this TableSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def table_limits(self):
        """
        Gets the table_limits of this TableSummary.

        :return: The table_limits of this TableSummary.
        :rtype: oci.nosql.models.TableLimits
        """
        return self._table_limits

    @table_limits.setter
    def table_limits(self, table_limits):
        """
        Sets the table_limits of this TableSummary.

        :param table_limits: The table_limits of this TableSummary.
        :type: oci.nosql.models.TableLimits
        """
        self._table_limits = table_limits

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TableSummary.
        The state of a table.


        :return: The lifecycle_state of this TableSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TableSummary.
        The state of a table.


        :param lifecycle_state: The lifecycle_state of this TableSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TableSummary.
        A message describing the current state in more detail.


        :return: The lifecycle_details of this TableSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TableSummary.
        A message describing the current state in more detail.


        :param lifecycle_details: The lifecycle_details of this TableSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_auto_reclaimable(self):
        """
        Gets the is_auto_reclaimable of this TableSummary.
        True if this table can be reclaimed after an idle period.


        :return: The is_auto_reclaimable of this TableSummary.
        :rtype: bool
        """
        return self._is_auto_reclaimable

    @is_auto_reclaimable.setter
    def is_auto_reclaimable(self, is_auto_reclaimable):
        """
        Sets the is_auto_reclaimable of this TableSummary.
        True if this table can be reclaimed after an idle period.


        :param is_auto_reclaimable: The is_auto_reclaimable of this TableSummary.
        :type: bool
        """
        self._is_auto_reclaimable = is_auto_reclaimable

    @property
    def time_of_expiration(self):
        """
        Gets the time_of_expiration of this TableSummary.
        If lifecycleState is INACTIVE, indicates when
        this table will be automatically removed.
        An RFC3339 formatted datetime string.


        :return: The time_of_expiration of this TableSummary.
        :rtype: datetime
        """
        return self._time_of_expiration

    @time_of_expiration.setter
    def time_of_expiration(self, time_of_expiration):
        """
        Sets the time_of_expiration of this TableSummary.
        If lifecycleState is INACTIVE, indicates when
        this table will be automatically removed.
        An RFC3339 formatted datetime string.


        :param time_of_expiration: The time_of_expiration of this TableSummary.
        :type: datetime
        """
        self._time_of_expiration = time_of_expiration

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TableSummary.
        Simple key-value pair that is applied without any predefined
        name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this TableSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TableSummary.
        Simple key-value pair that is applied without any predefined
        name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this TableSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TableSummary.
        Defined tags for this resource. Each key is predefined and
        scoped to a namespace.  Example: `{\"foo-namespace\":
        {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this TableSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TableSummary.
        Defined tags for this resource. Each key is predefined and
        scoped to a namespace.  Example: `{\"foo-namespace\":
        {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this TableSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TableSummary.
        Read-only system tag. These predefined keys are scoped to
        namespaces.  At present the only supported namespace is
        `\"orcl-cloud\"`; and the only key in that namespace is
        `\"free-tier-retained\"`.
        Example: `{\"orcl-cloud\"\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this TableSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TableSummary.
        Read-only system tag. These predefined keys are scoped to
        namespaces.  At present the only supported namespace is
        `\"orcl-cloud\"`; and the only key in that namespace is
        `\"free-tier-retained\"`.
        Example: `{\"orcl-cloud\"\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this TableSummary.
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
