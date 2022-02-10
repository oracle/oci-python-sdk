# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Model(object):
    """
    Machine-learned Model.
    """

    #: A constant which can be used with the model_type property of a Model.
    #: This constant has a value of "IMAGE_CLASSIFICATION"
    MODEL_TYPE_IMAGE_CLASSIFICATION = "IMAGE_CLASSIFICATION"

    #: A constant which can be used with the model_type property of a Model.
    #: This constant has a value of "OBJECT_DETECTION"
    MODEL_TYPE_OBJECT_DETECTION = "OBJECT_DETECTION"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Model object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Model.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Model.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Model.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Model.
        :type compartment_id: str

        :param model_type:
            The value to assign to the model_type property of this Model.
            Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param is_quick_mode:
            The value to assign to the is_quick_mode property of this Model.
        :type is_quick_mode: bool

        :param max_training_duration_in_hours:
            The value to assign to the max_training_duration_in_hours property of this Model.
        :type max_training_duration_in_hours: float

        :param trained_duration_in_hours:
            The value to assign to the trained_duration_in_hours property of this Model.
        :type trained_duration_in_hours: float

        :param training_dataset:
            The value to assign to the training_dataset property of this Model.
        :type training_dataset: oci.ai_vision.models.Dataset

        :param testing_dataset:
            The value to assign to the testing_dataset property of this Model.
        :type testing_dataset: oci.ai_vision.models.Dataset

        :param validation_dataset:
            The value to assign to the validation_dataset property of this Model.
        :type validation_dataset: oci.ai_vision.models.Dataset

        :param model_version:
            The value to assign to the model_version property of this Model.
        :type model_version: str

        :param project_id:
            The value to assign to the project_id property of this Model.
        :type project_id: str

        :param time_created:
            The value to assign to the time_created property of this Model.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Model.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Model.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Model.
        :type lifecycle_details: str

        :param precision:
            The value to assign to the precision property of this Model.
        :type precision: float

        :param recall:
            The value to assign to the recall property of this Model.
        :type recall: float

        :param average_precision:
            The value to assign to the average_precision property of this Model.
        :type average_precision: float

        :param confidence_threshold:
            The value to assign to the confidence_threshold property of this Model.
        :type confidence_threshold: float

        :param total_image_count:
            The value to assign to the total_image_count property of this Model.
        :type total_image_count: int

        :param test_image_count:
            The value to assign to the test_image_count property of this Model.
        :type test_image_count: int

        :param metrics:
            The value to assign to the metrics property of this Model.
        :type metrics: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Model.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Model.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Model.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'model_type': 'str',
            'is_quick_mode': 'bool',
            'max_training_duration_in_hours': 'float',
            'trained_duration_in_hours': 'float',
            'training_dataset': 'Dataset',
            'testing_dataset': 'Dataset',
            'validation_dataset': 'Dataset',
            'model_version': 'str',
            'project_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'precision': 'float',
            'recall': 'float',
            'average_precision': 'float',
            'confidence_threshold': 'float',
            'total_image_count': 'int',
            'test_image_count': 'int',
            'metrics': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'model_type': 'modelType',
            'is_quick_mode': 'isQuickMode',
            'max_training_duration_in_hours': 'maxTrainingDurationInHours',
            'trained_duration_in_hours': 'trainedDurationInHours',
            'training_dataset': 'trainingDataset',
            'testing_dataset': 'testingDataset',
            'validation_dataset': 'validationDataset',
            'model_version': 'modelVersion',
            'project_id': 'projectId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'precision': 'precision',
            'recall': 'recall',
            'average_precision': 'averagePrecision',
            'confidence_threshold': 'confidenceThreshold',
            'total_image_count': 'totalImageCount',
            'test_image_count': 'testImageCount',
            'metrics': 'metrics',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._model_type = None
        self._is_quick_mode = None
        self._max_training_duration_in_hours = None
        self._trained_duration_in_hours = None
        self._training_dataset = None
        self._testing_dataset = None
        self._validation_dataset = None
        self._model_version = None
        self._project_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._precision = None
        self._recall = None
        self._average_precision = None
        self._confidence_threshold = None
        self._total_image_count = None
        self._test_image_count = None
        self._metrics = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Model.
        Unique identifier that is immutable after creation.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.
        Unique identifier that is immutable after creation.


        :param id: The id of this Model.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Model.
        Human-friendly name for the model, which can be changed.


        :return: The display_name of this Model.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Model.
        Human-friendly name for the model, which can be changed.


        :param display_name: The display_name of this Model.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Model.
        Optional description of the model.


        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.
        Optional description of the model.


        :param description: The description of this Model.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Model.
        Compartment identifier.


        :return: The compartment_id of this Model.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Model.
        Compartment identifier.


        :param compartment_id: The compartment_id of this Model.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this Model.
        What type of Vision model this is.

        Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Model.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Model.
        What type of Vision model this is.


        :param model_type: The model_type of this Model.
        :type: str
        """
        allowed_values = ["IMAGE_CLASSIFICATION", "OBJECT_DETECTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def is_quick_mode(self):
        """
        Gets the is_quick_mode of this Model.
        Set to true when experimenting with a new model type or dataset so model training is quick, with a predefined low number of passes through the training data.


        :return: The is_quick_mode of this Model.
        :rtype: bool
        """
        return self._is_quick_mode

    @is_quick_mode.setter
    def is_quick_mode(self, is_quick_mode):
        """
        Sets the is_quick_mode of this Model.
        Set to true when experimenting with a new model type or dataset so model training is quick, with a predefined low number of passes through the training data.


        :param is_quick_mode: The is_quick_mode of this Model.
        :type: bool
        """
        self._is_quick_mode = is_quick_mode

    @property
    def max_training_duration_in_hours(self):
        """
        Gets the max_training_duration_in_hours of this Model.
        Maximum model training duration in hours, expressed as a decimal fraction.


        :return: The max_training_duration_in_hours of this Model.
        :rtype: float
        """
        return self._max_training_duration_in_hours

    @max_training_duration_in_hours.setter
    def max_training_duration_in_hours(self, max_training_duration_in_hours):
        """
        Sets the max_training_duration_in_hours of this Model.
        Maximum model training duration in hours, expressed as a decimal fraction.


        :param max_training_duration_in_hours: The max_training_duration_in_hours of this Model.
        :type: float
        """
        self._max_training_duration_in_hours = max_training_duration_in_hours

    @property
    def trained_duration_in_hours(self):
        """
        Gets the trained_duration_in_hours of this Model.
        Total hours actually used for model training.


        :return: The trained_duration_in_hours of this Model.
        :rtype: float
        """
        return self._trained_duration_in_hours

    @trained_duration_in_hours.setter
    def trained_duration_in_hours(self, trained_duration_in_hours):
        """
        Sets the trained_duration_in_hours of this Model.
        Total hours actually used for model training.


        :param trained_duration_in_hours: The trained_duration_in_hours of this Model.
        :type: float
        """
        self._trained_duration_in_hours = trained_duration_in_hours

    @property
    def training_dataset(self):
        """
        **[Required]** Gets the training_dataset of this Model.

        :return: The training_dataset of this Model.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """
        Sets the training_dataset of this Model.

        :param training_dataset: The training_dataset of this Model.
        :type: oci.ai_vision.models.Dataset
        """
        self._training_dataset = training_dataset

    @property
    def testing_dataset(self):
        """
        Gets the testing_dataset of this Model.

        :return: The testing_dataset of this Model.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._testing_dataset

    @testing_dataset.setter
    def testing_dataset(self, testing_dataset):
        """
        Sets the testing_dataset of this Model.

        :param testing_dataset: The testing_dataset of this Model.
        :type: oci.ai_vision.models.Dataset
        """
        self._testing_dataset = testing_dataset

    @property
    def validation_dataset(self):
        """
        Gets the validation_dataset of this Model.

        :return: The validation_dataset of this Model.
        :rtype: oci.ai_vision.models.Dataset
        """
        return self._validation_dataset

    @validation_dataset.setter
    def validation_dataset(self, validation_dataset):
        """
        Sets the validation_dataset of this Model.

        :param validation_dataset: The validation_dataset of this Model.
        :type: oci.ai_vision.models.Dataset
        """
        self._validation_dataset = validation_dataset

    @property
    def model_version(self):
        """
        **[Required]** Gets the model_version of this Model.
        The version of the model.


        :return: The model_version of this Model.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Model.
        The version of the model.


        :param model_version: The model_version of this Model.
        :type: str
        """
        self._model_version = model_version

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Model.
        The `OCID`__ of the project which contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this Model.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Model.
        The `OCID`__ of the project which contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this Model.
        :type: str
        """
        self._project_id = project_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Model.
        When the model was created, as an RFC3339 datetime string.


        :return: The time_created of this Model.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Model.
        When the model was created, as an RFC3339 datetime string.


        :param time_created: The time_created of this Model.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Model.
        When the model was updated, as an RFC3339 datetime string.


        :return: The time_updated of this Model.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Model.
        When the model was updated, as an RFC3339 datetime string.


        :param time_updated: The time_updated of this Model.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Model.
        Current state of the model.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Model.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Model.
        Current state of the model.


        :param lifecycle_state: The lifecycle_state of this Model.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Model.
        A message describing the current state in more detail which can provide actionable information if training failed.


        :return: The lifecycle_details of this Model.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Model.
        A message describing the current state in more detail which can provide actionable information if training failed.


        :param lifecycle_details: The lifecycle_details of this Model.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def precision(self):
        """
        Gets the precision of this Model.
        Precision of the trained model.


        :return: The precision of this Model.
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this Model.
        Precision of the trained model.


        :param precision: The precision of this Model.
        :type: float
        """
        self._precision = precision

    @property
    def recall(self):
        """
        Gets the recall of this Model.
        Recall of the trained model.


        :return: The recall of this Model.
        :rtype: float
        """
        return self._recall

    @recall.setter
    def recall(self, recall):
        """
        Sets the recall of this Model.
        Recall of the trained model.


        :param recall: The recall of this Model.
        :type: float
        """
        self._recall = recall

    @property
    def average_precision(self):
        """
        Gets the average_precision of this Model.
        Mean average precision of the trained model.


        :return: The average_precision of this Model.
        :rtype: float
        """
        return self._average_precision

    @average_precision.setter
    def average_precision(self, average_precision):
        """
        Sets the average_precision of this Model.
        Mean average precision of the trained model.


        :param average_precision: The average_precision of this Model.
        :type: float
        """
        self._average_precision = average_precision

    @property
    def confidence_threshold(self):
        """
        Gets the confidence_threshold of this Model.
        Intersection over union threshold used for calculating precision and recall.


        :return: The confidence_threshold of this Model.
        :rtype: float
        """
        return self._confidence_threshold

    @confidence_threshold.setter
    def confidence_threshold(self, confidence_threshold):
        """
        Sets the confidence_threshold of this Model.
        Intersection over union threshold used for calculating precision and recall.


        :param confidence_threshold: The confidence_threshold of this Model.
        :type: float
        """
        self._confidence_threshold = confidence_threshold

    @property
    def total_image_count(self):
        """
        Gets the total_image_count of this Model.
        Number of images in the dataset used to train, validate, and test the model.


        :return: The total_image_count of this Model.
        :rtype: int
        """
        return self._total_image_count

    @total_image_count.setter
    def total_image_count(self, total_image_count):
        """
        Sets the total_image_count of this Model.
        Number of images in the dataset used to train, validate, and test the model.


        :param total_image_count: The total_image_count of this Model.
        :type: int
        """
        self._total_image_count = total_image_count

    @property
    def test_image_count(self):
        """
        Gets the test_image_count of this Model.
        Number of images set aside for evaluating model performance metrics after training.


        :return: The test_image_count of this Model.
        :rtype: int
        """
        return self._test_image_count

    @test_image_count.setter
    def test_image_count(self, test_image_count):
        """
        Sets the test_image_count of this Model.
        Number of images set aside for evaluating model performance metrics after training.


        :param test_image_count: The test_image_count of this Model.
        :type: int
        """
        self._test_image_count = test_image_count

    @property
    def metrics(self):
        """
        Gets the metrics of this Model.
        Complete set of per-label metrics for successfully trained model.


        :return: The metrics of this Model.
        :rtype: str
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this Model.
        Complete set of per-label metrics for successfully trained model.


        :param metrics: The metrics of this Model.
        :type: str
        """
        self._metrics = metrics

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Model.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Model.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Model.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Model.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Model.
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
