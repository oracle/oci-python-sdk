# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceCatalog(object):
    """
    The model for an Oracle Cloud Infrastructure Service Catalog.
    """

    #: A constant which can be used with the lifecycle_state property of a ServiceCatalog.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ServiceCatalog.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceCatalog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceCatalog.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ServiceCatalog.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ServiceCatalog.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ServiceCatalog.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ServiceCatalog.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ServiceCatalog.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this ServiceCatalog.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ServiceCatalog.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceCatalog.
        The unique identifier for the Service catalog.


        :return: The id of this ServiceCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceCatalog.
        The unique identifier for the Service catalog.


        :param id: The id of this ServiceCatalog.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ServiceCatalog.
        The Compartment id where the service catalog exists


        :return: The compartment_id of this ServiceCatalog.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ServiceCatalog.
        The Compartment id where the service catalog exists


        :param compartment_id: The compartment_id of this ServiceCatalog.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ServiceCatalog.
        The name of the service catalog.


        :return: The display_name of this ServiceCatalog.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ServiceCatalog.
        The name of the service catalog.


        :param display_name: The display_name of this ServiceCatalog.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ServiceCatalog.
        The lifecycle state of the service catalog.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ServiceCatalog.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ServiceCatalog.
        The lifecycle state of the service catalog.


        :param lifecycle_state: The lifecycle_state of this ServiceCatalog.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ServiceCatalog.
        The date and time the service catalog was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-26T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ServiceCatalog.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ServiceCatalog.
        The date and time the service catalog was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-26T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ServiceCatalog.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ServiceCatalog.
        The date and time the service catalog was last modified, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-12-10T05:10:29.721Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ServiceCatalog.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ServiceCatalog.
        The date and time the service catalog was last modified, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-12-10T05:10:29.721Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ServiceCatalog.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ServiceCatalog.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ServiceCatalog.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ServiceCatalog.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ServiceCatalog.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ServiceCatalog.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ServiceCatalog.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ServiceCatalog.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ServiceCatalog.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
