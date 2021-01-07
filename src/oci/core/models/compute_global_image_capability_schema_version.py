# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeGlobalImageCapabilitySchemaVersion(object):
    """
    Compute Global Image Capability Schema Version is a set of all possible capabilities for a collection of images.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeGlobalImageCapabilitySchemaVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ComputeGlobalImageCapabilitySchemaVersion.
        :type name: str

        :param compute_global_image_capability_schema_id:
            The value to assign to the compute_global_image_capability_schema_id property of this ComputeGlobalImageCapabilitySchemaVersion.
        :type compute_global_image_capability_schema_id: str

        :param display_name:
            The value to assign to the display_name property of this ComputeGlobalImageCapabilitySchemaVersion.
        :type display_name: str

        :param schema_data:
            The value to assign to the schema_data property of this ComputeGlobalImageCapabilitySchemaVersion.
        :type schema_data: dict(str, ImageCapabilitySchemaDescriptor)

        :param time_created:
            The value to assign to the time_created property of this ComputeGlobalImageCapabilitySchemaVersion.
        :type time_created: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'compute_global_image_capability_schema_id': 'str',
            'display_name': 'str',
            'schema_data': 'dict(str, ImageCapabilitySchemaDescriptor)',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'compute_global_image_capability_schema_id': 'computeGlobalImageCapabilitySchemaId',
            'display_name': 'displayName',
            'schema_data': 'schemaData',
            'time_created': 'timeCreated'
        }

        self._name = None
        self._compute_global_image_capability_schema_id = None
        self._display_name = None
        self._schema_data = None
        self._time_created = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ComputeGlobalImageCapabilitySchemaVersion.
        The name of the compute global image capability schema version


        :return: The name of this ComputeGlobalImageCapabilitySchemaVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComputeGlobalImageCapabilitySchemaVersion.
        The name of the compute global image capability schema version


        :param name: The name of this ComputeGlobalImageCapabilitySchemaVersion.
        :type: str
        """
        self._name = name

    @property
    def compute_global_image_capability_schema_id(self):
        """
        **[Required]** Gets the compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersion.
        The ocid of the compute global image capability schema


        :return: The compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersion.
        :rtype: str
        """
        return self._compute_global_image_capability_schema_id

    @compute_global_image_capability_schema_id.setter
    def compute_global_image_capability_schema_id(self, compute_global_image_capability_schema_id):
        """
        Sets the compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersion.
        The ocid of the compute global image capability schema


        :param compute_global_image_capability_schema_id: The compute_global_image_capability_schema_id of this ComputeGlobalImageCapabilitySchemaVersion.
        :type: str
        """
        self._compute_global_image_capability_schema_id = compute_global_image_capability_schema_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ComputeGlobalImageCapabilitySchemaVersion.
        A user-friendly name for the compute global image capability schema


        :return: The display_name of this ComputeGlobalImageCapabilitySchemaVersion.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeGlobalImageCapabilitySchemaVersion.
        A user-friendly name for the compute global image capability schema


        :param display_name: The display_name of this ComputeGlobalImageCapabilitySchemaVersion.
        :type: str
        """
        self._display_name = display_name

    @property
    def schema_data(self):
        """
        **[Required]** Gets the schema_data of this ComputeGlobalImageCapabilitySchemaVersion.
        The map of each capability name to its ImageCapabilityDescriptor.


        :return: The schema_data of this ComputeGlobalImageCapabilitySchemaVersion.
        :rtype: dict(str, ImageCapabilitySchemaDescriptor)
        """
        return self._schema_data

    @schema_data.setter
    def schema_data(self, schema_data):
        """
        Sets the schema_data of this ComputeGlobalImageCapabilitySchemaVersion.
        The map of each capability name to its ImageCapabilityDescriptor.


        :param schema_data: The schema_data of this ComputeGlobalImageCapabilitySchemaVersion.
        :type: dict(str, ImageCapabilitySchemaDescriptor)
        """
        self._schema_data = schema_data

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeGlobalImageCapabilitySchemaVersion.
        The date and time the compute global image capability schema version was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeGlobalImageCapabilitySchemaVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeGlobalImageCapabilitySchemaVersion.
        The date and time the compute global image capability schema version was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeGlobalImageCapabilitySchemaVersion.
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
