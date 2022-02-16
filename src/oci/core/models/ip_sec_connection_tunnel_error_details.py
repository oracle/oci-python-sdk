# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPSecConnectionTunnelErrorDetails(object):
    """
    Details for an error on an IPSec tunnel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IPSecConnectionTunnelErrorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IPSecConnectionTunnelErrorDetails.
        :type id: str

        :param error_code:
            The value to assign to the error_code property of this IPSecConnectionTunnelErrorDetails.
        :type error_code: str

        :param error_description:
            The value to assign to the error_description property of this IPSecConnectionTunnelErrorDetails.
        :type error_description: str

        :param solution:
            The value to assign to the solution property of this IPSecConnectionTunnelErrorDetails.
        :type solution: str

        :param oci_resources_link:
            The value to assign to the oci_resources_link property of this IPSecConnectionTunnelErrorDetails.
        :type oci_resources_link: str

        :param timestamp:
            The value to assign to the timestamp property of this IPSecConnectionTunnelErrorDetails.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'error_code': 'str',
            'error_description': 'str',
            'solution': 'str',
            'oci_resources_link': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'error_code': 'errorCode',
            'error_description': 'errorDescription',
            'solution': 'solution',
            'oci_resources_link': 'ociResourcesLink',
            'timestamp': 'timestamp'
        }

        self._id = None
        self._error_code = None
        self._error_description = None
        self._solution = None
        self._oci_resources_link = None
        self._timestamp = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnectionTunnelErrorDetails.
        Unique ID generated for each error report.


        :return: The id of this IPSecConnectionTunnelErrorDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnectionTunnelErrorDetails.
        Unique ID generated for each error report.


        :param id: The id of this IPSecConnectionTunnelErrorDetails.
        :type: str
        """
        self._id = id

    @property
    def error_code(self):
        """
        **[Required]** Gets the error_code of this IPSecConnectionTunnelErrorDetails.
        Unique code describes the error type.


        :return: The error_code of this IPSecConnectionTunnelErrorDetails.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this IPSecConnectionTunnelErrorDetails.
        Unique code describes the error type.


        :param error_code: The error_code of this IPSecConnectionTunnelErrorDetails.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_description(self):
        """
        **[Required]** Gets the error_description of this IPSecConnectionTunnelErrorDetails.
        A detailed description of the error.


        :return: The error_description of this IPSecConnectionTunnelErrorDetails.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """
        Sets the error_description of this IPSecConnectionTunnelErrorDetails.
        A detailed description of the error.


        :param error_description: The error_description of this IPSecConnectionTunnelErrorDetails.
        :type: str
        """
        self._error_description = error_description

    @property
    def solution(self):
        """
        **[Required]** Gets the solution of this IPSecConnectionTunnelErrorDetails.
        Resolution for the error.


        :return: The solution of this IPSecConnectionTunnelErrorDetails.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """
        Sets the solution of this IPSecConnectionTunnelErrorDetails.
        Resolution for the error.


        :param solution: The solution of this IPSecConnectionTunnelErrorDetails.
        :type: str
        """
        self._solution = solution

    @property
    def oci_resources_link(self):
        """
        **[Required]** Gets the oci_resources_link of this IPSecConnectionTunnelErrorDetails.
        Link to more Oracle resources or relevant documentation.


        :return: The oci_resources_link of this IPSecConnectionTunnelErrorDetails.
        :rtype: str
        """
        return self._oci_resources_link

    @oci_resources_link.setter
    def oci_resources_link(self, oci_resources_link):
        """
        Sets the oci_resources_link of this IPSecConnectionTunnelErrorDetails.
        Link to more Oracle resources or relevant documentation.


        :param oci_resources_link: The oci_resources_link of this IPSecConnectionTunnelErrorDetails.
        :type: str
        """
        self._oci_resources_link = oci_resources_link

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this IPSecConnectionTunnelErrorDetails.
        Timestamp when the error occurred.


        :return: The timestamp of this IPSecConnectionTunnelErrorDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this IPSecConnectionTunnelErrorDetails.
        Timestamp when the error occurred.


        :param timestamp: The timestamp of this IPSecConnectionTunnelErrorDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
