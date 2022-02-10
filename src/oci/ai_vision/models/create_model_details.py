# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelDetails(object):
    """
    Information needed to create a new model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateModelDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateModelDetails.
        :type description: str

        :param model_version:
            The value to assign to the model_version property of this CreateModelDetails.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this CreateModelDetails.
        :type model_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateModelDetails.
        :type compartment_id: str

        :param is_quick_mode:
            The value to assign to the is_quick_mode property of this CreateModelDetails.
        :type is_quick_mode: bool

        :param max_training_duration_in_hours:
            The value to assign to the max_training_duration_in_hours property of this CreateModelDetails.
        :type max_training_duration_in_hours: float

        :param training_dataset:
            The value to assign to the training_dataset property of this CreateModelDetails.
        :type training_dataset: oci.ai_vision.models.Dataset

        :param testing_dataset:
            The value to assign to the testing_dataset property of this CreateModelDetails.
        :type testing_dataset: oci.ai_vision.models.Dataset

        :param validation_dataset:
            The value to assign to the validation_dataset property of this CreateModelDetails.
        :type validation_dataset: oci.ai_vision.models.Dataset

        :param project_id:
            The value to assign to the project_id property of this CreateModelDetails.
        :type project_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateModelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateModelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'compartment_id': 'str',
            'is_quick_mode': 'bool',
            'max_training_duration_in_hours': 'float',
            'training_dataset': 'Dataset',
            'testing_dataset': 'Dataset',
            'validation_dataset': 'Dataset',
            'project_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'compartment_id': 'compartmentId',
            'is_quick_mode': 'isQuickMode',
            'max_training_duration_in_hours': 'maxTrainingDurationInHours',
            'training_dataset': 'trainingDataset',
            'testing_dataset': 'testingDataset',
            'validation_dataset': 'validationDataset',
            'project_id': 'projectId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._model_version = None
        self._model_type = None
        self._compartment_id = None
        self._is_quick_mode = None
        self._max_training_duration_in_hours = None
        self._training_dataset = None
        self._testing_dataset = None
        self._validation_dataset = None
        self._project_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateModelDetails.
        Human-friendly name for the model, which can be changed.


        :return: The display_name of this CreateModelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateModelDetails.
        Human-friendly name for the model, which can be changed.


        :param display_name: The display_name of this CreateModelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateModelDetails.
        Optional description of the model.


        :return: The description of this CreateModelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateModelDetails.
        Optional description of the model.


        :param description: The description of this CreateModelDetails.
        :type: str
        """
        self._description = description

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateModelDetails.
        Model version


        :return: The model_version of this CreateModelDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateModelDetails.
        Model version


        :param model_version: The model_version of this CreateModelDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateModelDetails.
        What type of Vision model this is.


        :return: The model_type of this CreateModelDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateModelDetails.
        What type of Vision model this is.


        :param model_type: The model_type of this CreateModelDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateModelDetails.
        Compartment identifier.


        :return: The compartment_id of this CreateModelDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateModelDetails.
        Compartment identifier.


        :param compartment_id: The compartment_id of this CreateModelDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_quick_mode(self):
        """
        Gets the is_quick_mode of this CreateModelDetails.
        Set to true when experimenting with a new model type or dataset so model training is quick, with a predefined low number of passes through the training data.


        :return: The is_quick_mode of this CreateModelDetails.
        :rtype: bool
        """
        return self._is_quick_mode

    @is_quick_mode.setter
    def is_quick_mode(self, is_quick_mode):
        """
        Sets the is_quick_mode of this CreateModelDetails.
        Set to true when experimenting with a new model type or dataset so model training is quick, with a predefined low number of passes through the training data.


        :param is_quick_mode: The is_quick_mode of this CreateModelDetails.
        :type: bool
        """
        self._is_quick_mode = is_quick_mode

    @property
    def max_training_duration_in_hours(self):
        """
        Gets the max_training_duration_in_hours of this CreateModelDetails.
        Maximum model training duration in hours, expressed as a decimal fraction.


        :return: The max_training_duration_in_hours of this CreateModelDetails.
        :rtype: float
        """
        return self._max_training_duration_in_hours

    @max_training_duration_in_hours.setter
    def max_training_duration_in_hours(self, max_training_duration_in_hours):
        """
        Sets the max_training_duration_in_hours of this CreateModelDetails.
        Maximum model training duration in hours, expressed as a decimal fraction.


        :param max_training_duration_in_hours: The max_training_duration_in_hours of this CreateModelDetails.
        :type: float
        """
        self._max_training_duration_in_hours = max_training_duration_in_hours

    @property
    def training_dataset(self):
        """
        **[Required]** Gets the training_dataset of this CreateModelDetails.

        :return: The training_dataset of this CreateModelDetails.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """
        Sets the training_dataset of this CreateModelDetails.

        :param training_dataset: The training_dataset of this CreateModelDetails.
        :type: oci.ai_vision.models.Dataset
        """
        self._training_dataset = training_dataset

    @property
    def testing_dataset(self):
        """
        Gets the testing_dataset of this CreateModelDetails.

        :return: The testing_dataset of this CreateModelDetails.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._testing_dataset

    @testing_dataset.setter
    def testing_dataset(self, testing_dataset):
        """
        Sets the testing_dataset of this CreateModelDetails.

        :param testing_dataset: The testing_dataset of this CreateModelDetails.
        :type: oci.ai_vision.models.Dataset
        """
        self._testing_dataset = testing_dataset

    @property
    def validation_dataset(self):
        """
        Gets the validation_dataset of this CreateModelDetails.

        :return: The validation_dataset of this CreateModelDetails.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._validation_dataset

    @validation_dataset.setter
    def validation_dataset(self, validation_dataset):
        """
        Sets the validation_dataset of this CreateModelDetails.

        :param validation_dataset: The validation_dataset of this CreateModelDetails.
        :type: oci.ai_vision.models.Dataset
        """
        self._validation_dataset = validation_dataset

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateModelDetails.
        The `OCID`__ of the project which contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateModelDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateModelDetails.
        The `OCID`__ of the project which contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateModelDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateModelDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateModelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateModelDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateModelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateModelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateModelDetails.
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
