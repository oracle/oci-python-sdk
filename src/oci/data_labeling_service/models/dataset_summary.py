# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatasetSummary(object):
    """
    A dataset summary is the representation returned in list views.  It is usually a subset of the full dataset entity and should not contain any potentially sensitive information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatasetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatasetSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatasetSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatasetSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DatasetSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatasetSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatasetSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatasetSummary.
        :type lifecycle_details: str

        :param annotation_format:
            The value to assign to the annotation_format property of this DatasetSummary.
        :type annotation_format: str

        :param dataset_format_details:
            The value to assign to the dataset_format_details property of this DatasetSummary.
        :type dataset_format_details: oci.data_labeling_service.models.DatasetFormatDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatasetSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatasetSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DatasetSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'annotation_format': 'str',
            'dataset_format_details': 'DatasetFormatDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'annotation_format': 'annotationFormat',
            'dataset_format_details': 'datasetFormatDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._annotation_format = None
        self._dataset_format_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatasetSummary.
        The OCID of the Dataset


        :return: The id of this DatasetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatasetSummary.
        The OCID of the Dataset


        :param id: The id of this DatasetSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this DatasetSummary.
        A user-friendly display name for the resource.


        :return: The display_name of this DatasetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatasetSummary.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this DatasetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatasetSummary.
        Compartment Identifier


        :return: The compartment_id of this DatasetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatasetSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this DatasetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DatasetSummary.
        The time the the Dataset was created. An RFC3339 formatted datetime string


        :return: The time_created of this DatasetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatasetSummary.
        The time the the Dataset was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DatasetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DatasetSummary.
        The date and time the resource was last updated, in the timestamp format defined by RFC3339.


        :return: The time_updated of this DatasetSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatasetSummary.
        The date and time the resource was last updated, in the timestamp format defined by RFC3339.


        :param time_updated: The time_updated of this DatasetSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DatasetSummary.
        The state of a Dataset.


        :return: The lifecycle_state of this DatasetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatasetSummary.
        The state of a Dataset.


        :param lifecycle_state: The lifecycle_state of this DatasetSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatasetSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DatasetSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatasetSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DatasetSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def annotation_format(self):
        """
        **[Required]** Gets the annotation_format of this DatasetSummary.
        The annotation format name required for labeling records.


        :return: The annotation_format of this DatasetSummary.
        :rtype: str
        """
        return self._annotation_format

    @annotation_format.setter
    def annotation_format(self, annotation_format):
        """
        Sets the annotation_format of this DatasetSummary.
        The annotation format name required for labeling records.


        :param annotation_format: The annotation_format of this DatasetSummary.
        :type: str
        """
        self._annotation_format = annotation_format

    @property
    def dataset_format_details(self):
        """
        **[Required]** Gets the dataset_format_details of this DatasetSummary.

        :return: The dataset_format_details of this DatasetSummary.
        :rtype: oci.data_labeling_service.models.DatasetFormatDetails
        """
        return self._dataset_format_details

    @dataset_format_details.setter
    def dataset_format_details(self, dataset_format_details):
        """
        Sets the dataset_format_details of this DatasetSummary.

        :param dataset_format_details: The dataset_format_details of this DatasetSummary.
        :type: oci.data_labeling_service.models.DatasetFormatDetails
        """
        self._dataset_format_details = dataset_format_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatasetSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatasetSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatasetSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatasetSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatasetSummary.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatasetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatasetSummary.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatasetSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatasetSummary.
        The usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DatasetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatasetSummary.
        The usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DatasetSummary.
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
