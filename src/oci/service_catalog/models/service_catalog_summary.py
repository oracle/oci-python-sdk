# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceCatalogSummary(object):
    """
    The model for a summary of an Oracle Cloud Infrastructure service catalog.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceCatalogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceCatalogSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ServiceCatalogSummary.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ServiceCatalogSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ServiceCatalogSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this ServiceCatalogSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._lifecycle_state = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceCatalogSummary.
        The unique identifier for the Service catalog.


        :return: The id of this ServiceCatalogSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceCatalogSummary.
        The unique identifier for the Service catalog.


        :param id: The id of this ServiceCatalogSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ServiceCatalogSummary.
        The lifecycle state of the service catalog.


        :return: The lifecycle_state of this ServiceCatalogSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ServiceCatalogSummary.
        The lifecycle state of the service catalog.


        :param lifecycle_state: The lifecycle_state of this ServiceCatalogSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ServiceCatalogSummary.
        The Compartment id where the service catalog exists.


        :return: The compartment_id of this ServiceCatalogSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ServiceCatalogSummary.
        The Compartment id where the service catalog exists.


        :param compartment_id: The compartment_id of this ServiceCatalogSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ServiceCatalogSummary.
        The name of the service catalog.


        :return: The display_name of this ServiceCatalogSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ServiceCatalogSummary.
        The name of the service catalog.


        :param display_name: The display_name of this ServiceCatalogSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ServiceCatalogSummary.
        The date and time this service catalog was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ServiceCatalogSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ServiceCatalogSummary.
        The date and time this service catalog was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ServiceCatalogSummary.
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
