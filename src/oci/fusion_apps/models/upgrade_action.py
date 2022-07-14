# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeAction(Action):
    """
    Quarterly upgrade details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeAction object with values from keyword arguments. The default value of the :py:attr:`~oci.fusion_apps.models.UpgradeAction.action_type` attribute
        of this class is ``QUARTERLY_UPGRADE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference_key:
            The value to assign to the reference_key property of this UpgradeAction.
        :type reference_key: str

        :param action_type:
            The value to assign to the action_type property of this UpgradeAction.
            Allowed values for this property are: "QUARTERLY_UPGRADE", "PATCH", "VERTEX"
        :type action_type: str

        :param state:
            The value to assign to the state property of this UpgradeAction.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"
        :type state: str

        :param description:
            The value to assign to the description property of this UpgradeAction.
        :type description: str

        :param version:
            The value to assign to the version property of this UpgradeAction.
        :type version: str

        :param qualifier:
            The value to assign to the qualifier property of this UpgradeAction.
        :type qualifier: str

        """
        self.swagger_types = {
            'reference_key': 'str',
            'action_type': 'str',
            'state': 'str',
            'description': 'str',
            'version': 'str',
            'qualifier': 'str'
        }

        self.attribute_map = {
            'reference_key': 'referenceKey',
            'action_type': 'actionType',
            'state': 'state',
            'description': 'description',
            'version': 'version',
            'qualifier': 'qualifier'
        }

        self._reference_key = None
        self._action_type = None
        self._state = None
        self._description = None
        self._version = None
        self._qualifier = None
        self._action_type = 'QUARTERLY_UPGRADE'

    @property
    def version(self):
        """
        Gets the version of this UpgradeAction.
        name of the repo


        :return: The version of this UpgradeAction.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpgradeAction.
        name of the repo


        :param version: The version of this UpgradeAction.
        :type: str
        """
        self._version = version

    @property
    def qualifier(self):
        """
        Gets the qualifier of this UpgradeAction.
        month qualifier


        :return: The qualifier of this UpgradeAction.
        :rtype: str
        """
        return self._qualifier

    @qualifier.setter
    def qualifier(self, qualifier):
        """
        Sets the qualifier of this UpgradeAction.
        month qualifier


        :param qualifier: The qualifier of this UpgradeAction.
        :type: str
        """
        self._qualifier = qualifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
