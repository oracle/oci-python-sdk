# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    The details for updating a connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.UpdateGithubAccessTokenConnectionDetails`
        * :class:`~oci.devops.models.UpdateVbsAccessTokenConnectionDetails`
        * :class:`~oci.devops.models.UpdateBitbucketServerAccessTokenConnectionDetails`
        * :class:`~oci.devops.models.UpdateGitlabAccessTokenConnectionDetails`
        * :class:`~oci.devops.models.UpdateBitbucketCloudAppPasswordConnectionDetails`
        * :class:`~oci.devops.models.UpdateGitlabServerAccessTokenConnectionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateConnectionDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateConnectionDetails.
        :type display_name: str

        :param connection_type:
            The value to assign to the connection_type property of this UpdateConnectionDetails.
        :type connection_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'connection_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'connection_type': 'connectionType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._connection_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'GITHUB_ACCESS_TOKEN':
            return 'UpdateGithubAccessTokenConnectionDetails'

        if type == 'VBS_ACCESS_TOKEN':
            return 'UpdateVbsAccessTokenConnectionDetails'

        if type == 'BITBUCKET_SERVER_ACCESS_TOKEN':
            return 'UpdateBitbucketServerAccessTokenConnectionDetails'

        if type == 'GITLAB_ACCESS_TOKEN':
            return 'UpdateGitlabAccessTokenConnectionDetails'

        if type == 'BITBUCKET_CLOUD_APP_PASSWORD':
            return 'UpdateBitbucketCloudAppPasswordConnectionDetails'

        if type == 'GITLAB_SERVER_ACCESS_TOKEN':
            return 'UpdateGitlabServerAccessTokenConnectionDetails'
        else:
            return 'UpdateConnectionDetails'

    @property
    def description(self):
        """
        Gets the description of this UpdateConnectionDetails.
        Optional description about the connection.


        :return: The description of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConnectionDetails.
        Optional description about the connection.


        :param description: The description of this UpdateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConnectionDetails.
        Optional connection display name. Avoid entering confidential information.


        :return: The display_name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConnectionDetails.
        Optional connection display name. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this UpdateConnectionDetails.
        The type of connection.


        :return: The connection_type of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this UpdateConnectionDetails.
        The type of connection.


        :param connection_type: The connection_type of this UpdateConnectionDetails.
        :type: str
        """
        self._connection_type = connection_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateConnectionDetails.
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
