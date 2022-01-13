# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Dataset(object):
    """
    A dataset is a logical collection of records. The dataset contains all the information necessary to describe a record's source, format, type of annotations allowed on these records, and labels allowed on annotations.
    """

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Dataset.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Dataset object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Dataset.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Dataset.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Dataset.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this Dataset.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Dataset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Dataset.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Dataset.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Dataset.
        :type lifecycle_details: str

        :param annotation_format:
            The value to assign to the annotation_format property of this Dataset.
        :type annotation_format: str

        :param dataset_source_details:
            The value to assign to the dataset_source_details property of this Dataset.
        :type dataset_source_details: oci.data_labeling_service.models.DatasetSourceDetails

        :param dataset_format_details:
            The value to assign to the dataset_format_details property of this Dataset.
        :type dataset_format_details: oci.data_labeling_service.models.DatasetFormatDetails

        :param label_set:
            The value to assign to the label_set property of this Dataset.
        :type label_set: oci.data_labeling_service.models.LabelSet

        :param initial_record_generation_configuration:
            The value to assign to the initial_record_generation_configuration property of this Dataset.
        :type initial_record_generation_configuration: oci.data_labeling_service.models.InitialRecordGenerationConfiguration

        :param labeling_instructions:
            The value to assign to the labeling_instructions property of this Dataset.
        :type labeling_instructions: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Dataset.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Dataset.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Dataset.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'annotation_format': 'str',
            'dataset_source_details': 'DatasetSourceDetails',
            'dataset_format_details': 'DatasetFormatDetails',
            'label_set': 'LabelSet',
            'initial_record_generation_configuration': 'InitialRecordGenerationConfiguration',
            'labeling_instructions': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'annotation_format': 'annotationFormat',
            'dataset_source_details': 'datasetSourceDetails',
            'dataset_format_details': 'datasetFormatDetails',
            'label_set': 'labelSet',
            'initial_record_generation_configuration': 'initialRecordGenerationConfiguration',
            'labeling_instructions': 'labelingInstructions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._annotation_format = None
        self._dataset_source_details = None
        self._dataset_format_details = None
        self._label_set = None
        self._initial_record_generation_configuration = None
        self._labeling_instructions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Dataset.
        The OCID of the Dataset.


        :return: The id of this Dataset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Dataset.
        The OCID of the Dataset.


        :param id: The id of this Dataset.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Dataset.
        A user-friendly display name for the resource.


        :return: The display_name of this Dataset.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Dataset.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this Dataset.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Dataset.
        The OCID of the compartment of the resource.


        :return: The compartment_id of this Dataset.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Dataset.
        The OCID of the compartment of the resource.


        :param compartment_id: The compartment_id of this Dataset.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this Dataset.
        A user provided description of the dataset


        :return: The description of this Dataset.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Dataset.
        A user provided description of the dataset


        :param description: The description of this Dataset.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Dataset.
        The date and time the resource was created, in the timestamp format defined by RFC3339.


        :return: The time_created of this Dataset.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Dataset.
        The date and time the resource was created, in the timestamp format defined by RFC3339.


        :param time_created: The time_created of this Dataset.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Dataset.
        The date and time the resource was last updated, in the timestamp format defined by RFC3339.


        :return: The time_updated of this Dataset.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Dataset.
        The date and time the resource was last updated, in the timestamp format defined by RFC3339.


        :param time_updated: The time_updated of this Dataset.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Dataset.
        The state of a dataset.
        CREATING - The dataset is being created.  It will transition to ACTIVE when it is ready for labeling.
        ACTIVE   - The dataset is ready for labeling.
        UPDATING - The dataset is being updated.  It and its related resources may be unavailable for other updates until it returns to ACTIVE.
        NEEDS_ATTENTION - A dataset updation operation has failed due to validation or other errors and needs attention.
        DELETING - The dataset and its related resources are being deleted.
        DELETED  - The dataset has been deleted and is no longer available.
        FAILED   - The dataset has failed due to validation or other errors.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Dataset.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Dataset.
        The state of a dataset.
        CREATING - The dataset is being created.  It will transition to ACTIVE when it is ready for labeling.
        ACTIVE   - The dataset is ready for labeling.
        UPDATING - The dataset is being updated.  It and its related resources may be unavailable for other updates until it returns to ACTIVE.
        NEEDS_ATTENTION - A dataset updation operation has failed due to validation or other errors and needs attention.
        DELETING - The dataset and its related resources are being deleted.
        DELETED  - The dataset has been deleted and is no longer available.
        FAILED   - The dataset has failed due to validation or other errors.


        :param lifecycle_state: The lifecycle_state of this Dataset.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Dataset.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in FAILED or NEEDS_ATTENTION state.


        :return: The lifecycle_details of this Dataset.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Dataset.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in FAILED or NEEDS_ATTENTION state.


        :param lifecycle_details: The lifecycle_details of this Dataset.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def annotation_format(self):
        """
        **[Required]** Gets the annotation_format of this Dataset.
        The annotation format name required for labeling records.


        :return: The annotation_format of this Dataset.
        :rtype: str
        """
        return self._annotation_format

    @annotation_format.setter
    def annotation_format(self, annotation_format):
        """
        Sets the annotation_format of this Dataset.
        The annotation format name required for labeling records.


        :param annotation_format: The annotation_format of this Dataset.
        :type: str
        """
        self._annotation_format = annotation_format

    @property
    def dataset_source_details(self):
        """
        **[Required]** Gets the dataset_source_details of this Dataset.

        :return: The dataset_source_details of this Dataset.
        :rtype: oci.data_labeling_service.models.DatasetSourceDetails
        """
        return self._dataset_source_details

    @dataset_source_details.setter
    def dataset_source_details(self, dataset_source_details):
        """
        Sets the dataset_source_details of this Dataset.

        :param dataset_source_details: The dataset_source_details of this Dataset.
        :type: oci.data_labeling_service.models.DatasetSourceDetails
        """
        self._dataset_source_details = dataset_source_details

    @property
    def dataset_format_details(self):
        """
        **[Required]** Gets the dataset_format_details of this Dataset.

        :return: The dataset_format_details of this Dataset.
        :rtype: oci.data_labeling_service.models.DatasetFormatDetails
        """
        return self._dataset_format_details

    @dataset_format_details.setter
    def dataset_format_details(self, dataset_format_details):
        """
        Sets the dataset_format_details of this Dataset.

        :param dataset_format_details: The dataset_format_details of this Dataset.
        :type: oci.data_labeling_service.models.DatasetFormatDetails
        """
        self._dataset_format_details = dataset_format_details

    @property
    def label_set(self):
        """
        **[Required]** Gets the label_set of this Dataset.

        :return: The label_set of this Dataset.
        :rtype: oci.data_labeling_service.models.LabelSet
        """
        return self._label_set

    @label_set.setter
    def label_set(self, label_set):
        """
        Sets the label_set of this Dataset.

        :param label_set: The label_set of this Dataset.
        :type: oci.data_labeling_service.models.LabelSet
        """
        self._label_set = label_set

    @property
    def initial_record_generation_configuration(self):
        """
        Gets the initial_record_generation_configuration of this Dataset.

        :return: The initial_record_generation_configuration of this Dataset.
        :rtype: oci.data_labeling_service.models.InitialRecordGenerationConfiguration
        """
        return self._initial_record_generation_configuration

    @initial_record_generation_configuration.setter
    def initial_record_generation_configuration(self, initial_record_generation_configuration):
        """
        Sets the initial_record_generation_configuration of this Dataset.

        :param initial_record_generation_configuration: The initial_record_generation_configuration of this Dataset.
        :type: oci.data_labeling_service.models.InitialRecordGenerationConfiguration
        """
        self._initial_record_generation_configuration = initial_record_generation_configuration

    @property
    def labeling_instructions(self):
        """
        Gets the labeling_instructions of this Dataset.
        The labeling instructions for human labelers in rich text format


        :return: The labeling_instructions of this Dataset.
        :rtype: str
        """
        return self._labeling_instructions

    @labeling_instructions.setter
    def labeling_instructions(self, labeling_instructions):
        """
        Sets the labeling_instructions of this Dataset.
        The labeling instructions for human labelers in rich text format


        :param labeling_instructions: The labeling_instructions of this Dataset.
        :type: str
        """
        self._labeling_instructions = labeling_instructions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Dataset.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Dataset.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Dataset.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Dataset.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Dataset.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Dataset.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Dataset.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Dataset.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Dataset.
        The usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Dataset.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Dataset.
        The usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Dataset.
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
