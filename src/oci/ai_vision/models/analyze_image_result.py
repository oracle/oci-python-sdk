# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyzeImageResult(object):
    """
    The image analysis results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyzeImageResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_objects:
            The value to assign to the image_objects property of this AnalyzeImageResult.
        :type image_objects: list[oci.ai_vision.models.ImageObject]

        :param labels:
            The value to assign to the labels property of this AnalyzeImageResult.
        :type labels: list[oci.ai_vision.models.Label]

        :param ontology_classes:
            The value to assign to the ontology_classes property of this AnalyzeImageResult.
        :type ontology_classes: list[oci.ai_vision.models.OntologyClass]

        :param image_text:
            The value to assign to the image_text property of this AnalyzeImageResult.
        :type image_text: oci.ai_vision.models.ImageText

        :param image_classification_model_version:
            The value to assign to the image_classification_model_version property of this AnalyzeImageResult.
        :type image_classification_model_version: str

        :param object_detection_model_version:
            The value to assign to the object_detection_model_version property of this AnalyzeImageResult.
        :type object_detection_model_version: str

        :param text_detection_model_version:
            The value to assign to the text_detection_model_version property of this AnalyzeImageResult.
        :type text_detection_model_version: str

        :param errors:
            The value to assign to the errors property of this AnalyzeImageResult.
        :type errors: list[oci.ai_vision.models.ProcessingError]

        """
        self.swagger_types = {
            'image_objects': 'list[ImageObject]',
            'labels': 'list[Label]',
            'ontology_classes': 'list[OntologyClass]',
            'image_text': 'ImageText',
            'image_classification_model_version': 'str',
            'object_detection_model_version': 'str',
            'text_detection_model_version': 'str',
            'errors': 'list[ProcessingError]'
        }

        self.attribute_map = {
            'image_objects': 'imageObjects',
            'labels': 'labels',
            'ontology_classes': 'ontologyClasses',
            'image_text': 'imageText',
            'image_classification_model_version': 'imageClassificationModelVersion',
            'object_detection_model_version': 'objectDetectionModelVersion',
            'text_detection_model_version': 'textDetectionModelVersion',
            'errors': 'errors'
        }

        self._image_objects = None
        self._labels = None
        self._ontology_classes = None
        self._image_text = None
        self._image_classification_model_version = None
        self._object_detection_model_version = None
        self._text_detection_model_version = None
        self._errors = None

    @property
    def image_objects(self):
        """
        Gets the image_objects of this AnalyzeImageResult.
        The detected objects.


        :return: The image_objects of this AnalyzeImageResult.
        :rtype: list[oci.ai_vision.models.ImageObject]
        """
        return self._image_objects

    @image_objects.setter
    def image_objects(self, image_objects):
        """
        Sets the image_objects of this AnalyzeImageResult.
        The detected objects.


        :param image_objects: The image_objects of this AnalyzeImageResult.
        :type: list[oci.ai_vision.models.ImageObject]
        """
        self._image_objects = image_objects

    @property
    def labels(self):
        """
        Gets the labels of this AnalyzeImageResult.
        The image classification labels.


        :return: The labels of this AnalyzeImageResult.
        :rtype: list[oci.ai_vision.models.Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this AnalyzeImageResult.
        The image classification labels.


        :param labels: The labels of this AnalyzeImageResult.
        :type: list[oci.ai_vision.models.Label]
        """
        self._labels = labels

    @property
    def ontology_classes(self):
        """
        Gets the ontology_classes of this AnalyzeImageResult.
        The ontologyClasses of image labels.


        :return: The ontology_classes of this AnalyzeImageResult.
        :rtype: list[oci.ai_vision.models.OntologyClass]
        """
        return self._ontology_classes

    @ontology_classes.setter
    def ontology_classes(self, ontology_classes):
        """
        Sets the ontology_classes of this AnalyzeImageResult.
        The ontologyClasses of image labels.


        :param ontology_classes: The ontology_classes of this AnalyzeImageResult.
        :type: list[oci.ai_vision.models.OntologyClass]
        """
        self._ontology_classes = ontology_classes

    @property
    def image_text(self):
        """
        Gets the image_text of this AnalyzeImageResult.

        :return: The image_text of this AnalyzeImageResult.
        :rtype: oci.ai_vision.models.ImageText
        """
        return self._image_text

    @image_text.setter
    def image_text(self, image_text):
        """
        Sets the image_text of this AnalyzeImageResult.

        :param image_text: The image_text of this AnalyzeImageResult.
        :type: oci.ai_vision.models.ImageText
        """
        self._image_text = image_text

    @property
    def image_classification_model_version(self):
        """
        Gets the image_classification_model_version of this AnalyzeImageResult.
        The image classification model version.


        :return: The image_classification_model_version of this AnalyzeImageResult.
        :rtype: str
        """
        return self._image_classification_model_version

    @image_classification_model_version.setter
    def image_classification_model_version(self, image_classification_model_version):
        """
        Sets the image_classification_model_version of this AnalyzeImageResult.
        The image classification model version.


        :param image_classification_model_version: The image_classification_model_version of this AnalyzeImageResult.
        :type: str
        """
        self._image_classification_model_version = image_classification_model_version

    @property
    def object_detection_model_version(self):
        """
        Gets the object_detection_model_version of this AnalyzeImageResult.
        The object detection model version.


        :return: The object_detection_model_version of this AnalyzeImageResult.
        :rtype: str
        """
        return self._object_detection_model_version

    @object_detection_model_version.setter
    def object_detection_model_version(self, object_detection_model_version):
        """
        Sets the object_detection_model_version of this AnalyzeImageResult.
        The object detection model version.


        :param object_detection_model_version: The object_detection_model_version of this AnalyzeImageResult.
        :type: str
        """
        self._object_detection_model_version = object_detection_model_version

    @property
    def text_detection_model_version(self):
        """
        Gets the text_detection_model_version of this AnalyzeImageResult.
        The text detection model version.


        :return: The text_detection_model_version of this AnalyzeImageResult.
        :rtype: str
        """
        return self._text_detection_model_version

    @text_detection_model_version.setter
    def text_detection_model_version(self, text_detection_model_version):
        """
        Sets the text_detection_model_version of this AnalyzeImageResult.
        The text detection model version.


        :param text_detection_model_version: The text_detection_model_version of this AnalyzeImageResult.
        :type: str
        """
        self._text_detection_model_version = text_detection_model_version

    @property
    def errors(self):
        """
        Gets the errors of this AnalyzeImageResult.
        The errors encountered during image analysis.


        :return: The errors of this AnalyzeImageResult.
        :rtype: list[oci.ai_vision.models.ProcessingError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this AnalyzeImageResult.
        The errors encountered during image analysis.


        :param errors: The errors of this AnalyzeImageResult.
        :type: list[oci.ai_vision.models.ProcessingError]
        """
        self._errors = errors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
