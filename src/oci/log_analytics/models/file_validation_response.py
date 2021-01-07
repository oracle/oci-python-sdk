# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileValidationResponse(object):
    """
    Response object containing details about file upload eligibility.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FileValidationResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_file:
            The value to assign to the input_file property of this FileValidationResponse.
        :type input_file: str

        :param object_location:
            The value to assign to the object_location property of this FileValidationResponse.
        :type object_location: str

        :param files:
            The value to assign to the files property of this FileValidationResponse.
        :type files: list[oci.log_analytics.models.UploadFileStatus]

        """
        self.swagger_types = {
            'input_file': 'str',
            'object_location': 'str',
            'files': 'list[UploadFileStatus]'
        }

        self.attribute_map = {
            'input_file': 'inputFile',
            'object_location': 'objectLocation',
            'files': 'files'
        }

        self._input_file = None
        self._object_location = None
        self._files = None

    @property
    def input_file(self):
        """
        **[Required]** Gets the input_file of this FileValidationResponse.
        Input File Name.


        :return: The input_file of this FileValidationResponse.
        :rtype: str
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """
        Sets the input_file of this FileValidationResponse.
        Input File Name.


        :param input_file: The input_file of this FileValidationResponse.
        :type: str
        """
        self._input_file = input_file

    @property
    def object_location(self):
        """
        **[Required]** Gets the object_location of this FileValidationResponse.
        Object Location where file content is available.


        :return: The object_location of this FileValidationResponse.
        :rtype: str
        """
        return self._object_location

    @object_location.setter
    def object_location(self, object_location):
        """
        Sets the object_location of this FileValidationResponse.
        Object Location where file content is available.


        :param object_location: The object_location of this FileValidationResponse.
        :type: str
        """
        self._object_location = object_location

    @property
    def files(self):
        """
        Gets the files of this FileValidationResponse.
        List of files inside the given archive file and their corresponding status information.


        :return: The files of this FileValidationResponse.
        :rtype: list[oci.log_analytics.models.UploadFileStatus]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this FileValidationResponse.
        List of files inside the given archive file and their corresponding status information.


        :param files: The files of this FileValidationResponse.
        :type: list[oci.log_analytics.models.UploadFileStatus]
        """
        self._files = files

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
