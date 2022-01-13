# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatasetDetails(object):
    """
    Parameters needed to create a new Dataset. A Dataset allows a user to describe the data source that provides the Records and how Annotations should be applied to the Records.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatasetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDatasetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDatasetDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatasetDetails.
        :type compartment_id: str

        :param annotation_format:
            The value to assign to the annotation_format property of this CreateDatasetDetails.
        :type annotation_format: str

        :param dataset_source_details:
            The value to assign to the dataset_source_details property of this CreateDatasetDetails.
        :type dataset_source_details: oci.data_labeling_service.models.DatasetSourceDetails

        :param dataset_format_details:
            The value to assign to the dataset_format_details property of this CreateDatasetDetails.
        :type dataset_format_details: oci.data_labeling_service.models.DatasetFormatDetails

        :param initial_record_generation_configuration:
            The value to assign to the initial_record_generation_configuration property of this CreateDatasetDetails.
        :type initial_record_generation_configuration: oci.data_labeling_service.models.InitialRecordGenerationConfiguration

        :param label_set:
            The value to assign to the label_set property of this CreateDatasetDetails.
        :type label_set: oci.data_labeling_service.models.LabelSet

        :param labeling_instructions:
            The value to assign to the labeling_instructions property of this CreateDatasetDetails.
        :type labeling_instructions: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatasetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatasetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'annotation_format': 'str',
            'dataset_source_details': 'DatasetSourceDetails',
            'dataset_format_details': 'DatasetFormatDetails',
            'initial_record_generation_configuration': 'InitialRecordGenerationConfiguration',
            'label_set': 'LabelSet',
            'labeling_instructions': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'annotation_format': 'annotationFormat',
            'dataset_source_details': 'datasetSourceDetails',
            'dataset_format_details': 'datasetFormatDetails',
            'initial_record_generation_configuration': 'initialRecordGenerationConfiguration',
            'label_set': 'labelSet',
            'labeling_instructions': 'labelingInstructions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._annotation_format = None
        self._dataset_source_details = None
        self._dataset_format_details = None
        self._initial_record_generation_configuration = None
        self._label_set = None
        self._labeling_instructions = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDatasetDetails.
        A user-friendly display name for the resource.


        :return: The display_name of this CreateDatasetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDatasetDetails.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this CreateDatasetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDatasetDetails.
        A user provided description of the dataset


        :return: The description of this CreateDatasetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDatasetDetails.
        A user provided description of the dataset


        :param description: The description of this CreateDatasetDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatasetDetails.
        The OCID of the compartment of the resource.


        :return: The compartment_id of this CreateDatasetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatasetDetails.
        The OCID of the compartment of the resource.


        :param compartment_id: The compartment_id of this CreateDatasetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def annotation_format(self):
        """
        **[Required]** Gets the annotation_format of this CreateDatasetDetails.
        The annotation format name required for labeling records.


        :return: The annotation_format of this CreateDatasetDetails.
        :rtype: str
        """
        return self._annotation_format

    @annotation_format.setter
    def annotation_format(self, annotation_format):
        """
        Sets the annotation_format of this CreateDatasetDetails.
        The annotation format name required for labeling records.


        :param annotation_format: The annotation_format of this CreateDatasetDetails.
        :type: str
        """
        self._annotation_format = annotation_format

    @property
    def dataset_source_details(self):
        """
        **[Required]** Gets the dataset_source_details of this CreateDatasetDetails.

        :return: The dataset_source_details of this CreateDatasetDetails.
        :rtype: oci.data_labeling_service.models.DatasetSourceDetails
        """
        return self._dataset_source_details

    @dataset_source_details.setter
    def dataset_source_details(self, dataset_source_details):
        """
        Sets the dataset_source_details of this CreateDatasetDetails.

        :param dataset_source_details: The dataset_source_details of this CreateDatasetDetails.
        :type: oci.data_labeling_service.models.DatasetSourceDetails
        """
        self._dataset_source_details = dataset_source_details

    @property
    def dataset_format_details(self):
        """
        **[Required]** Gets the dataset_format_details of this CreateDatasetDetails.

        :return: The dataset_format_details of this CreateDatasetDetails.
        :rtype: oci.data_labeling_service.models.DatasetFormatDetails
        """
        return self._dataset_format_details

    @dataset_format_details.setter
    def dataset_format_details(self, dataset_format_details):
        """
        Sets the dataset_format_details of this CreateDatasetDetails.

        :param dataset_format_details: The dataset_format_details of this CreateDatasetDetails.
        :type: oci.data_labeling_service.models.DatasetFormatDetails
        """
        self._dataset_format_details = dataset_format_details

    @property
    def initial_record_generation_configuration(self):
        """
        Gets the initial_record_generation_configuration of this CreateDatasetDetails.

        :return: The initial_record_generation_configuration of this CreateDatasetDetails.
        :rtype: oci.data_labeling_service.models.InitialRecordGenerationConfiguration
        """
        return self._initial_record_generation_configuration

    @initial_record_generation_configuration.setter
    def initial_record_generation_configuration(self, initial_record_generation_configuration):
        """
        Sets the initial_record_generation_configuration of this CreateDatasetDetails.

        :param initial_record_generation_configuration: The initial_record_generation_configuration of this CreateDatasetDetails.
        :type: oci.data_labeling_service.models.InitialRecordGenerationConfiguration
        """
        self._initial_record_generation_configuration = initial_record_generation_configuration

    @property
    def label_set(self):
        """
        **[Required]** Gets the label_set of this CreateDatasetDetails.

        :return: The label_set of this CreateDatasetDetails.
        :rtype: oci.data_labeling_service.models.LabelSet
        """
        return self._label_set

    @label_set.setter
    def label_set(self, label_set):
        """
        Sets the label_set of this CreateDatasetDetails.

        :param label_set: The label_set of this CreateDatasetDetails.
        :type: oci.data_labeling_service.models.LabelSet
        """
        self._label_set = label_set

    @property
    def labeling_instructions(self):
        """
        Gets the labeling_instructions of this CreateDatasetDetails.
        The labeling instructions for human labelers in rich text format


        :return: The labeling_instructions of this CreateDatasetDetails.
        :rtype: str
        """
        return self._labeling_instructions

    @labeling_instructions.setter
    def labeling_instructions(self, labeling_instructions):
        """
        Sets the labeling_instructions of this CreateDatasetDetails.
        The labeling instructions for human labelers in rich text format


        :param labeling_instructions: The labeling_instructions of this CreateDatasetDetails.
        :type: str
        """
        self._labeling_instructions = labeling_instructions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatasetDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDatasetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatasetDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDatasetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatasetDetails.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDatasetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatasetDetails.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDatasetDetails.
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
