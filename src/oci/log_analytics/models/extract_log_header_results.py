# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtractLogHeaderResults(object):
    """
    log header values
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtractLogHeaderResults object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param json_paths:
            The value to assign to the json_paths property of this ExtractLogHeaderResults.
        :type json_paths: list[ExtractLogHeaderDetails]

        :param xml_paths:
            The value to assign to the xml_paths property of this ExtractLogHeaderResults.
        :type xml_paths: list[str]

        """
        self.swagger_types = {
            'json_paths': 'list[ExtractLogHeaderDetails]',
            'xml_paths': 'list[str]'
        }

        self.attribute_map = {
            'json_paths': 'jsonPaths',
            'xml_paths': 'xmlPaths'
        }

        self._json_paths = None
        self._xml_paths = None

    @property
    def json_paths(self):
        """
        Gets the json_paths of this ExtractLogHeaderResults.
        log header json paths


        :return: The json_paths of this ExtractLogHeaderResults.
        :rtype: list[ExtractLogHeaderDetails]
        """
        return self._json_paths

    @json_paths.setter
    def json_paths(self, json_paths):
        """
        Sets the json_paths of this ExtractLogHeaderResults.
        log header json paths


        :param json_paths: The json_paths of this ExtractLogHeaderResults.
        :type: list[ExtractLogHeaderDetails]
        """
        self._json_paths = json_paths

    @property
    def xml_paths(self):
        """
        Gets the xml_paths of this ExtractLogHeaderResults.
        log field or header values


        :return: The xml_paths of this ExtractLogHeaderResults.
        :rtype: list[str]
        """
        return self._xml_paths

    @xml_paths.setter
    def xml_paths(self, xml_paths):
        """
        Sets the xml_paths of this ExtractLogHeaderResults.
        log field or header values


        :param xml_paths: The xml_paths of this ExtractLogHeaderResults.
        :type: list[str]
        """
        self._xml_paths = xml_paths

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
