# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Filter(object):
    """
    The filters for the trigger.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Filter object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.DevopsCodeRepositoryFilter`
        * :class:`~oci.devops.models.BitbucketCloudFilter`
        * :class:`~oci.devops.models.GitlabFilter`
        * :class:`~oci.devops.models.GithubFilter`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param trigger_source:
            The value to assign to the trigger_source property of this Filter.
        :type trigger_source: str

        """
        self.swagger_types = {
            'trigger_source': 'str'
        }

        self.attribute_map = {
            'trigger_source': 'triggerSource'
        }

        self._trigger_source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['triggerSource']

        if type == 'DEVOPS_CODE_REPOSITORY':
            return 'DevopsCodeRepositoryFilter'

        if type == 'BITBUCKET_CLOUD':
            return 'BitbucketCloudFilter'

        if type == 'GITLAB':
            return 'GitlabFilter'

        if type == 'GITHUB':
            return 'GithubFilter'
        else:
            return 'Filter'

    @property
    def trigger_source(self):
        """
        **[Required]** Gets the trigger_source of this Filter.
        Source of the trigger. Allowed values are, GITHUB and GITLAB.


        :return: The trigger_source of this Filter.
        :rtype: str
        """
        return self._trigger_source

    @trigger_source.setter
    def trigger_source(self, trigger_source):
        """
        Sets the trigger_source of this Filter.
        Source of the trigger. Allowed values are, GITHUB and GITLAB.


        :param trigger_source: The trigger_source of this Filter.
        :type: str
        """
        self._trigger_source = trigger_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
