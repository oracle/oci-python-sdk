# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentImageSummary(object):
    """
    Available ODMS Agent Images.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AgentImageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this AgentImageSummary.
        :type version: str

        :param download_url:
            The value to assign to the download_url property of this AgentImageSummary.
        :type download_url: str

        """
        self.swagger_types = {
            'version': 'str',
            'download_url': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'download_url': 'downloadUrl'
        }

        self._version = None
        self._download_url = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this AgentImageSummary.
        ODMS Agent Image version.


        :return: The version of this AgentImageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AgentImageSummary.
        ODMS Agent Image version.


        :param version: The version of this AgentImageSummary.
        :type: str
        """
        self._version = version

    @property
    def download_url(self):
        """
        **[Required]** Gets the download_url of this AgentImageSummary.
        URL to download Agent Image of the ODMS Agent.


        :return: The download_url of this AgentImageSummary.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this AgentImageSummary.
        URL to download Agent Image of the ODMS Agent.


        :param download_url: The download_url of this AgentImageSummary.
        :type: str
        """
        self._download_url = download_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
