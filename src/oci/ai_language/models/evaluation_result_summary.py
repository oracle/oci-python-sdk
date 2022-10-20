# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EvaluationResultSummary(object):
    """
    model evaluation analysis of different models
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EvaluationResultSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_language.models.NamedEntityRecognitionEvaluationResult`
        * :class:`~oci.ai_language.models.TextClassificationModelEvaluationResult`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this EvaluationResultSummary.
        :type model_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EvaluationResultSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EvaluationResultSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'model_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._model_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'NAMED_ENTITY_RECOGNITION':
            return 'NamedEntityRecognitionEvaluationResult'

        if type == 'TEXT_CLASSIFICATION':
            return 'TextClassificationModelEvaluationResult'
        else:
            return 'EvaluationResultSummary'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this EvaluationResultSummary.
        Model type


        :return: The model_type of this EvaluationResultSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this EvaluationResultSummary.
        Model type


        :param model_type: The model_type of this EvaluationResultSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EvaluationResultSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EvaluationResultSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EvaluationResultSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EvaluationResultSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EvaluationResultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EvaluationResultSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EvaluationResultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EvaluationResultSummary.
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
