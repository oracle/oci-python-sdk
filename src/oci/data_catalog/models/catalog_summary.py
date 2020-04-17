# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CatalogSummary(object):
    """
    Summary of the data catalog.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CatalogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CatalogSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this CatalogSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CatalogSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this CatalogSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CatalogSummary.
        :type time_updated: datetime

        :param number_of_objects:
            The value to assign to the number_of_objects property of this CatalogSummary.
        :type number_of_objects: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CatalogSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CatalogSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CatalogSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CatalogSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'number_of_objects': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'number_of_objects': 'numberOfObjects',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._number_of_objects = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CatalogSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this CatalogSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CatalogSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this CatalogSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this CatalogSummary.
        Data catalog identifier, that can be renamed.


        :return: The display_name of this CatalogSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CatalogSummary.
        Data catalog identifier, that can be renamed.


        :param display_name: The display_name of this CatalogSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CatalogSummary.
        Compartment identifier.


        :return: The compartment_id of this CatalogSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CatalogSummary.
        Compartment identifier.


        :param compartment_id: The compartment_id of this CatalogSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this CatalogSummary.
        The time the data catalog was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CatalogSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CatalogSummary.
        The time the data catalog was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CatalogSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this CatalogSummary.
        The time the data catalog was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this CatalogSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CatalogSummary.
        The time the data catalog was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this CatalogSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def number_of_objects(self):
        """
        Gets the number_of_objects of this CatalogSummary.
        The number of high level objects added to the data catalog.


        :return: The number_of_objects of this CatalogSummary.
        :rtype: int
        """
        return self._number_of_objects

    @number_of_objects.setter
    def number_of_objects(self, number_of_objects):
        """
        Sets the number_of_objects of this CatalogSummary.
        The number of high level objects added to the data catalog.


        :param number_of_objects: The number_of_objects of this CatalogSummary.
        :type: int
        """
        self._number_of_objects = number_of_objects

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CatalogSummary.
        The current state of the data catalog resource.


        :return: The lifecycle_state of this CatalogSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CatalogSummary.
        The current state of the data catalog resource.


        :param lifecycle_state: The lifecycle_state of this CatalogSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CatalogSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this CatalogSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CatalogSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this CatalogSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CatalogSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CatalogSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CatalogSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CatalogSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CatalogSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CatalogSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CatalogSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CatalogSummary.
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
