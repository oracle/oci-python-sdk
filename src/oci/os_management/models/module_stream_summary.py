# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamSummary(object):
    """
    Summary information pertaining to a module stream provided by a software source
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamSummary.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamSummary.
        :type stream_name: str

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleStreamSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'software_source_id': 'str'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'software_source_id': 'softwareSourceId'
        }

        self._module_name = None
        self._stream_name = None
        self._software_source_id = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamSummary.
        The name of the module that contains the stream.


        :return: The module_name of this ModuleStreamSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamSummary.
        The name of the module that contains the stream.


        :param module_name: The module_name of this ModuleStreamSummary.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamSummary.
        The name of the stream.


        :return: The stream_name of this ModuleStreamSummary.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamSummary.
        The name of the stream.


        :param stream_name: The stream_name of this ModuleStreamSummary.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ModuleStreamSummary.
        The OCID of the software source that provides this module stream.


        :return: The software_source_id of this ModuleStreamSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleStreamSummary.
        The OCID of the software source that provides this module stream.


        :param software_source_id: The software_source_id of this ModuleStreamSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
