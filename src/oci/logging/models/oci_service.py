# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .source import Source
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciService(Source):
    """
    OCI service logging configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciService object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.OciService.source_type` attribute
        of this class is ``OCISERVICE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this OciService.
            Allowed values for this property are: "OCISERVICE"
        :type source_type: str

        :param service:
            The value to assign to the service property of this OciService.
        :type service: str

        :param resource:
            The value to assign to the resource property of this OciService.
        :type resource: str

        :param category:
            The value to assign to the category property of this OciService.
        :type category: str

        :param parameters:
            The value to assign to the parameters property of this OciService.
        :type parameters: dict(str, str)

        """
        self.swagger_types = {
            'source_type': 'str',
            'service': 'str',
            'resource': 'str',
            'category': 'str',
            'parameters': 'dict(str, str)'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'service': 'service',
            'resource': 'resource',
            'category': 'category',
            'parameters': 'parameters'
        }

        self._source_type = None
        self._service = None
        self._resource = None
        self._category = None
        self._parameters = None
        self._source_type = 'OCISERVICE'

    @property
    def service(self):
        """
        **[Required]** Gets the service of this OciService.
        Service generating log.


        :return: The service of this OciService.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this OciService.
        Service generating log.


        :param service: The service of this OciService.
        :type: str
        """
        self._service = service

    @property
    def resource(self):
        """
        **[Required]** Gets the resource of this OciService.
        The unique identifier of the resource emitting the log.


        :return: The resource of this OciService.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this OciService.
        The unique identifier of the resource emitting the log.


        :param resource: The resource of this OciService.
        :type: str
        """
        self._resource = resource

    @property
    def category(self):
        """
        **[Required]** Gets the category of this OciService.
        Log object category.


        :return: The category of this OciService.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this OciService.
        Log object category.


        :param category: The category of this OciService.
        :type: str
        """
        self._category = category

    @property
    def parameters(self):
        """
        Gets the parameters of this OciService.
        Log category parameters are stored here.


        :return: The parameters of this OciService.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this OciService.
        Log category parameters are stored here.


        :param parameters: The parameters of this OciService.
        :type: dict(str, str)
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
