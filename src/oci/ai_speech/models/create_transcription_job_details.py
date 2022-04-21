# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTranscriptionJobDetails(object):
    """
    The information about new Transcription Job.
    """

    #: A constant which can be used with the additional_transcription_formats property of a CreateTranscriptionJobDetails.
    #: This constant has a value of "SRT"
    ADDITIONAL_TRANSCRIPTION_FORMATS_SRT = "SRT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTranscriptionJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTranscriptionJobDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTranscriptionJobDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateTranscriptionJobDetails.
        :type description: str

        :param additional_transcription_formats:
            The value to assign to the additional_transcription_formats property of this CreateTranscriptionJobDetails.
            Allowed values for items in this list are: "SRT"
        :type additional_transcription_formats: list[str]

        :param model_details:
            The value to assign to the model_details property of this CreateTranscriptionJobDetails.
        :type model_details: oci.ai_speech.models.TranscriptionModelDetails

        :param normalization:
            The value to assign to the normalization property of this CreateTranscriptionJobDetails.
        :type normalization: oci.ai_speech.models.TranscriptionNormalization

        :param input_location:
            The value to assign to the input_location property of this CreateTranscriptionJobDetails.
        :type input_location: oci.ai_speech.models.InputLocation

        :param output_location:
            The value to assign to the output_location property of this CreateTranscriptionJobDetails.
        :type output_location: oci.ai_speech.models.OutputLocation

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTranscriptionJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTranscriptionJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'additional_transcription_formats': 'list[str]',
            'model_details': 'TranscriptionModelDetails',
            'normalization': 'TranscriptionNormalization',
            'input_location': 'InputLocation',
            'output_location': 'OutputLocation',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'additional_transcription_formats': 'additionalTranscriptionFormats',
            'model_details': 'modelDetails',
            'normalization': 'normalization',
            'input_location': 'inputLocation',
            'output_location': 'outputLocation',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._additional_transcription_formats = None
        self._model_details = None
        self._normalization = None
        self._input_location = None
        self._output_location = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateTranscriptionJobDetails.
        A user-friendly display name for the job.


        :return: The display_name of this CreateTranscriptionJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTranscriptionJobDetails.
        A user-friendly display name for the job.


        :param display_name: The display_name of this CreateTranscriptionJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTranscriptionJobDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateTranscriptionJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTranscriptionJobDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateTranscriptionJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateTranscriptionJobDetails.
        A short description of the job.


        :return: The description of this CreateTranscriptionJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTranscriptionJobDetails.
        A short description of the job.


        :param description: The description of this CreateTranscriptionJobDetails.
        :type: str
        """
        self._description = description

    @property
    def additional_transcription_formats(self):
        """
        Gets the additional_transcription_formats of this CreateTranscriptionJobDetails.
        Transcription Format. By default JSON format will be considered.

        Allowed values for items in this list are: "SRT"


        :return: The additional_transcription_formats of this CreateTranscriptionJobDetails.
        :rtype: list[str]
        """
        return self._additional_transcription_formats

    @additional_transcription_formats.setter
    def additional_transcription_formats(self, additional_transcription_formats):
        """
        Sets the additional_transcription_formats of this CreateTranscriptionJobDetails.
        Transcription Format. By default JSON format will be considered.


        :param additional_transcription_formats: The additional_transcription_formats of this CreateTranscriptionJobDetails.
        :type: list[str]
        """
        allowed_values = ["SRT"]

        if additional_transcription_formats and additional_transcription_formats is not NONE_SENTINEL:
            for value in additional_transcription_formats:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `additional_transcription_formats`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._additional_transcription_formats = additional_transcription_formats

    @property
    def model_details(self):
        """
        Gets the model_details of this CreateTranscriptionJobDetails.

        :return: The model_details of this CreateTranscriptionJobDetails.
        :rtype: oci.ai_speech.models.TranscriptionModelDetails
        """
        return self._model_details

    @model_details.setter
    def model_details(self, model_details):
        """
        Sets the model_details of this CreateTranscriptionJobDetails.

        :param model_details: The model_details of this CreateTranscriptionJobDetails.
        :type: oci.ai_speech.models.TranscriptionModelDetails
        """
        self._model_details = model_details

    @property
    def normalization(self):
        """
        Gets the normalization of this CreateTranscriptionJobDetails.

        :return: The normalization of this CreateTranscriptionJobDetails.
        :rtype: oci.ai_speech.models.TranscriptionNormalization
        """
        return self._normalization

    @normalization.setter
    def normalization(self, normalization):
        """
        Sets the normalization of this CreateTranscriptionJobDetails.

        :param normalization: The normalization of this CreateTranscriptionJobDetails.
        :type: oci.ai_speech.models.TranscriptionNormalization
        """
        self._normalization = normalization

    @property
    def input_location(self):
        """
        **[Required]** Gets the input_location of this CreateTranscriptionJobDetails.

        :return: The input_location of this CreateTranscriptionJobDetails.
        :rtype: oci.ai_speech.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this CreateTranscriptionJobDetails.

        :param input_location: The input_location of this CreateTranscriptionJobDetails.
        :type: oci.ai_speech.models.InputLocation
        """
        self._input_location = input_location

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this CreateTranscriptionJobDetails.

        :return: The output_location of this CreateTranscriptionJobDetails.
        :rtype: oci.ai_speech.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this CreateTranscriptionJobDetails.

        :param output_location: The output_location of this CreateTranscriptionJobDetails.
        :type: oci.ai_speech.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTranscriptionJobDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateTranscriptionJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTranscriptionJobDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateTranscriptionJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTranscriptionJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateTranscriptionJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTranscriptionJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateTranscriptionJobDetails.
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
