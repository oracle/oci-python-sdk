# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateImageJobDetails(object):
    """
    Details about the batch image analysis.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateImageJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_location:
            The value to assign to the input_location property of this CreateImageJobDetails.
        :type input_location: oci.ai_vision.models.InputLocation

        :param features:
            The value to assign to the features property of this CreateImageJobDetails.
        :type features: list[oci.ai_vision.models.ImageFeature]

        :param output_location:
            The value to assign to the output_location property of this CreateImageJobDetails.
        :type output_location: oci.ai_vision.models.OutputLocation

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateImageJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateImageJobDetails.
        :type display_name: str

        :param is_zip_output_enabled:
            The value to assign to the is_zip_output_enabled property of this CreateImageJobDetails.
        :type is_zip_output_enabled: bool

        """
        self.swagger_types = {
            'input_location': 'InputLocation',
            'features': 'list[ImageFeature]',
            'output_location': 'OutputLocation',
            'compartment_id': 'str',
            'display_name': 'str',
            'is_zip_output_enabled': 'bool'
        }

        self.attribute_map = {
            'input_location': 'inputLocation',
            'features': 'features',
            'output_location': 'outputLocation',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_zip_output_enabled': 'isZipOutputEnabled'
        }

        self._input_location = None
        self._features = None
        self._output_location = None
        self._compartment_id = None
        self._display_name = None
        self._is_zip_output_enabled = None

    @property
    def input_location(self):
        """
        **[Required]** Gets the input_location of this CreateImageJobDetails.

        :return: The input_location of this CreateImageJobDetails.
        :rtype: oci.ai_vision.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this CreateImageJobDetails.

        :param input_location: The input_location of this CreateImageJobDetails.
        :type: oci.ai_vision.models.InputLocation
        """
        self._input_location = input_location

    @property
    def features(self):
        """
        **[Required]** Gets the features of this CreateImageJobDetails.
        List of image analysis types requested.


        :return: The features of this CreateImageJobDetails.
        :rtype: list[oci.ai_vision.models.ImageFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this CreateImageJobDetails.
        List of image analysis types requested.


        :param features: The features of this CreateImageJobDetails.
        :type: list[oci.ai_vision.models.ImageFeature]
        """
        self._features = features

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this CreateImageJobDetails.

        :return: The output_location of this CreateImageJobDetails.
        :rtype: oci.ai_vision.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this CreateImageJobDetails.

        :param output_location: The output_location of this CreateImageJobDetails.
        :type: oci.ai_vision.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateImageJobDetails.
        Compartment identifier from the requester.


        :return: The compartment_id of this CreateImageJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateImageJobDetails.
        Compartment identifier from the requester.


        :param compartment_id: The compartment_id of this CreateImageJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateImageJobDetails.
        Image job display name.


        :return: The display_name of this CreateImageJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateImageJobDetails.
        Image job display name.


        :param display_name: The display_name of this CreateImageJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_zip_output_enabled(self):
        """
        Gets the is_zip_output_enabled of this CreateImageJobDetails.
        Whether to generate a Zip file containing the results.


        :return: The is_zip_output_enabled of this CreateImageJobDetails.
        :rtype: bool
        """
        return self._is_zip_output_enabled

    @is_zip_output_enabled.setter
    def is_zip_output_enabled(self, is_zip_output_enabled):
        """
        Sets the is_zip_output_enabled of this CreateImageJobDetails.
        Whether to generate a Zip file containing the results.


        :param is_zip_output_enabled: The is_zip_output_enabled of this CreateImageJobDetails.
        :type: bool
        """
        self._is_zip_output_enabled = is_zip_output_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
