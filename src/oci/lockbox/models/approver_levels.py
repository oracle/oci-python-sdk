# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApproverLevels(object):
    """
    The approver levels.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApproverLevels object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param level1:
            The value to assign to the level1 property of this ApproverLevels.
        :type level1: oci.lockbox.models.ApproverInfo

        :param level2:
            The value to assign to the level2 property of this ApproverLevels.
        :type level2: oci.lockbox.models.ApproverInfo

        :param level3:
            The value to assign to the level3 property of this ApproverLevels.
        :type level3: oci.lockbox.models.ApproverInfo

        """
        self.swagger_types = {
            'level1': 'ApproverInfo',
            'level2': 'ApproverInfo',
            'level3': 'ApproverInfo'
        }

        self.attribute_map = {
            'level1': 'level1',
            'level2': 'level2',
            'level3': 'level3'
        }

        self._level1 = None
        self._level2 = None
        self._level3 = None

    @property
    def level1(self):
        """
        **[Required]** Gets the level1 of this ApproverLevels.

        :return: The level1 of this ApproverLevels.
        :rtype: oci.lockbox.models.ApproverInfo
        """
        return self._level1

    @level1.setter
    def level1(self, level1):
        """
        Sets the level1 of this ApproverLevels.

        :param level1: The level1 of this ApproverLevels.
        :type: oci.lockbox.models.ApproverInfo
        """
        self._level1 = level1

    @property
    def level2(self):
        """
        Gets the level2 of this ApproverLevels.

        :return: The level2 of this ApproverLevels.
        :rtype: oci.lockbox.models.ApproverInfo
        """
        return self._level2

    @level2.setter
    def level2(self, level2):
        """
        Sets the level2 of this ApproverLevels.

        :param level2: The level2 of this ApproverLevels.
        :type: oci.lockbox.models.ApproverInfo
        """
        self._level2 = level2

    @property
    def level3(self):
        """
        Gets the level3 of this ApproverLevels.

        :return: The level3 of this ApproverLevels.
        :rtype: oci.lockbox.models.ApproverInfo
        """
        return self._level3

    @level3.setter
    def level3(self, level3):
        """
        Sets the level3 of this ApproverLevels.

        :param level3: The level3 of this ApproverLevels.
        :type: oci.lockbox.models.ApproverInfo
        """
        self._level3 = level3

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
