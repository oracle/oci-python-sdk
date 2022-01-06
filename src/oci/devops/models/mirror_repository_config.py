# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MirrorRepositoryConfig(object):
    """
    Configuration information for mirroring the repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MirrorRepositoryConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_id:
            The value to assign to the connector_id property of this MirrorRepositoryConfig.
        :type connector_id: str

        :param repository_url:
            The value to assign to the repository_url property of this MirrorRepositoryConfig.
        :type repository_url: str

        :param trigger_schedule:
            The value to assign to the trigger_schedule property of this MirrorRepositoryConfig.
        :type trigger_schedule: oci.devops.models.TriggerSchedule

        """
        self.swagger_types = {
            'connector_id': 'str',
            'repository_url': 'str',
            'trigger_schedule': 'TriggerSchedule'
        }

        self.attribute_map = {
            'connector_id': 'connectorId',
            'repository_url': 'repositoryUrl',
            'trigger_schedule': 'triggerSchedule'
        }

        self._connector_id = None
        self._repository_url = None
        self._trigger_schedule = None

    @property
    def connector_id(self):
        """
        Gets the connector_id of this MirrorRepositoryConfig.
        Upstream git repository connection identifer.


        :return: The connector_id of this MirrorRepositoryConfig.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this MirrorRepositoryConfig.
        Upstream git repository connection identifer.


        :param connector_id: The connector_id of this MirrorRepositoryConfig.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def repository_url(self):
        """
        Gets the repository_url of this MirrorRepositoryConfig.
        URL of external repository you want to mirror.


        :return: The repository_url of this MirrorRepositoryConfig.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this MirrorRepositoryConfig.
        URL of external repository you want to mirror.


        :param repository_url: The repository_url of this MirrorRepositoryConfig.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def trigger_schedule(self):
        """
        Gets the trigger_schedule of this MirrorRepositoryConfig.

        :return: The trigger_schedule of this MirrorRepositoryConfig.
        :rtype: oci.devops.models.TriggerSchedule
        """
        return self._trigger_schedule

    @trigger_schedule.setter
    def trigger_schedule(self, trigger_schedule):
        """
        Sets the trigger_schedule of this MirrorRepositoryConfig.

        :param trigger_schedule: The trigger_schedule of this MirrorRepositoryConfig.
        :type: oci.devops.models.TriggerSchedule
        """
        self._trigger_schedule = trigger_schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
