# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectAnomaliesDetails(object):
    """
    Base class for the DetectAnomalies call. It contains the identifier that will
    be used for deciding what type of request this is.
    """

    #: A constant which can be used with the request_type property of a DetectAnomaliesDetails.
    #: This constant has a value of "INLINE"
    REQUEST_TYPE_INLINE = "INLINE"

    #: A constant which can be used with the request_type property of a DetectAnomaliesDetails.
    #: This constant has a value of "BASE64_ENCODED"
    REQUEST_TYPE_BASE64_ENCODED = "BASE64_ENCODED"

    def __init__(self, **kwargs):
        """
        Initializes a new DetectAnomaliesDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_anomaly_detection.models.InlineDetectAnomaliesRequest`
        * :class:`~oci.ai_anomaly_detection.models.EmbeddedDetectAnomaliesRequest`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_id:
            The value to assign to the model_id property of this DetectAnomaliesDetails.
        :type model_id: str

        :param request_type:
            The value to assign to the request_type property of this DetectAnomaliesDetails.
            Allowed values for this property are: "INLINE", "BASE64_ENCODED"
        :type request_type: str

        """
        self.swagger_types = {
            'model_id': 'str',
            'request_type': 'str'
        }

        self.attribute_map = {
            'model_id': 'modelId',
            'request_type': 'requestType'
        }

        self._model_id = None
        self._request_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['requestType']

        if type == 'INLINE':
            return 'InlineDetectAnomaliesRequest'

        if type == 'BASE64_ENCODED':
            return 'EmbeddedDetectAnomaliesRequest'
        else:
            return 'DetectAnomaliesDetails'

    @property
    def model_id(self):
        """
        **[Required]** Gets the model_id of this DetectAnomaliesDetails.
        The OCID of the trained model\u3002


        :return: The model_id of this DetectAnomaliesDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this DetectAnomaliesDetails.
        The OCID of the trained model\u3002


        :param model_id: The model_id of this DetectAnomaliesDetails.
        :type: str
        """
        self._model_id = model_id

    @property
    def request_type(self):
        """
        **[Required]** Gets the request_type of this DetectAnomaliesDetails.
        Type of request. This parameter will be filled autmatically by classes generated
        by the SDK. For raw curl request, user will have to provide this field.

        Allowed values for this property are: "INLINE", "BASE64_ENCODED"


        :return: The request_type of this DetectAnomaliesDetails.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """
        Sets the request_type of this DetectAnomaliesDetails.
        Type of request. This parameter will be filled autmatically by classes generated
        by the SDK. For raw curl request, user will have to provide this field.


        :param request_type: The request_type of this DetectAnomaliesDetails.
        :type: str
        """
        allowed_values = ["INLINE", "BASE64_ENCODED"]
        if not value_allowed_none_or_none_sentinel(request_type, allowed_values):
            raise ValueError(
                "Invalid value for `request_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._request_type = request_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
