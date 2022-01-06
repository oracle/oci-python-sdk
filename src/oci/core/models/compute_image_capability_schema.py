# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeImageCapabilitySchema(object):
    """
    Compute Image Capability Schema is a set of capabilities that filter the compute global capability schema
    version for an image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeImageCapabilitySchema object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeImageCapabilitySchema.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeImageCapabilitySchema.
        :type compartment_id: str

        :param compute_global_image_capability_schema_id:
            The value to assign to the compute_global_image_capability_schema_id property of this ComputeImageCapabilitySchema.
        :type compute_global_image_capability_schema_id: str

        :param compute_global_image_capability_schema_version_name:
            The value to assign to the compute_global_image_capability_schema_version_name property of this ComputeImageCapabilitySchema.
        :type compute_global_image_capability_schema_version_name: str

        :param image_id:
            The value to assign to the image_id property of this ComputeImageCapabilitySchema.
        :type image_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeImageCapabilitySchema.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ComputeImageCapabilitySchema.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeImageCapabilitySchema.
        :type freeform_tags: dict(str, str)

        :param schema_data:
            The value to assign to the schema_data property of this ComputeImageCapabilitySchema.
        :type schema_data: dict(str, ImageCapabilitySchemaDescriptor)

        :param time_created:
            The value to assign to the time_created property of this ComputeImageCapabilitySchema.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'compute_global_image_capability_schema_id': 'str',
            'compute_global_image_capability_schema_version_name': 'str',
            'image_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'schema_data': 'dict(str, ImageCapabilitySchemaDescriptor)',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'compute_global_image_capability_schema_id': 'computeGlobalImageCapabilitySchemaId',
            'compute_global_image_capability_schema_version_name': 'computeGlobalImageCapabilitySchemaVersionName',
            'image_id': 'imageId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'schema_data': 'schemaData',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._compute_global_image_capability_schema_id = None
        self._compute_global_image_capability_schema_version_name = None
        self._image_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._schema_data = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputeImageCapabilitySchema.
        The id of the compute global image capability schema version


        :return: The id of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeImageCapabilitySchema.
        The id of the compute global image capability schema version


        :param id: The id of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ComputeImageCapabilitySchema.
        The OCID of the compartment that contains the resource.


        :return: The compartment_id of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ComputeImageCapabilitySchema.
        The OCID of the compartment that contains the resource.


        :param compartment_id: The compartment_id of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compute_global_image_capability_schema_id(self):
        """
        **[Required]** Gets the compute_global_image_capability_schema_id of this ComputeImageCapabilitySchema.
        The ocid of the compute global image capability schema


        :return: The compute_global_image_capability_schema_id of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._compute_global_image_capability_schema_id

    @compute_global_image_capability_schema_id.setter
    def compute_global_image_capability_schema_id(self, compute_global_image_capability_schema_id):
        """
        Sets the compute_global_image_capability_schema_id of this ComputeImageCapabilitySchema.
        The ocid of the compute global image capability schema


        :param compute_global_image_capability_schema_id: The compute_global_image_capability_schema_id of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._compute_global_image_capability_schema_id = compute_global_image_capability_schema_id

    @property
    def compute_global_image_capability_schema_version_name(self):
        """
        **[Required]** Gets the compute_global_image_capability_schema_version_name of this ComputeImageCapabilitySchema.
        The name of the compute global image capability schema version


        :return: The compute_global_image_capability_schema_version_name of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._compute_global_image_capability_schema_version_name

    @compute_global_image_capability_schema_version_name.setter
    def compute_global_image_capability_schema_version_name(self, compute_global_image_capability_schema_version_name):
        """
        Sets the compute_global_image_capability_schema_version_name of this ComputeImageCapabilitySchema.
        The name of the compute global image capability schema version


        :param compute_global_image_capability_schema_version_name: The compute_global_image_capability_schema_version_name of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._compute_global_image_capability_schema_version_name = compute_global_image_capability_schema_version_name

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this ComputeImageCapabilitySchema.
        The OCID of the image associated with this compute image capability schema


        :return: The image_id of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ComputeImageCapabilitySchema.
        The OCID of the image associated with this compute image capability schema


        :param image_id: The image_id of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._image_id = image_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ComputeImageCapabilitySchema.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ComputeImageCapabilitySchema.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ComputeImageCapabilitySchema.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ComputeImageCapabilitySchema.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ComputeImageCapabilitySchema.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this ComputeImageCapabilitySchema.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeImageCapabilitySchema.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ComputeImageCapabilitySchema.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ComputeImageCapabilitySchema.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ComputeImageCapabilitySchema.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ComputeImageCapabilitySchema.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ComputeImageCapabilitySchema.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def schema_data(self):
        """
        **[Required]** Gets the schema_data of this ComputeImageCapabilitySchema.
        The map of each capability name to its ImageCapabilityDescriptor.


        :return: The schema_data of this ComputeImageCapabilitySchema.
        :rtype: dict(str, ImageCapabilitySchemaDescriptor)
        """
        return self._schema_data

    @schema_data.setter
    def schema_data(self, schema_data):
        """
        Sets the schema_data of this ComputeImageCapabilitySchema.
        The map of each capability name to its ImageCapabilityDescriptor.


        :param schema_data: The schema_data of this ComputeImageCapabilitySchema.
        :type: dict(str, ImageCapabilitySchemaDescriptor)
        """
        self._schema_data = schema_data

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeImageCapabilitySchema.
        The date and time the compute image capability schema was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeImageCapabilitySchema.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeImageCapabilitySchema.
        The date and time the compute image capability schema was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeImageCapabilitySchema.
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
