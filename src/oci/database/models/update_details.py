# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDetails(object):
    """
    Details specifying which maintenance update to apply to the cloud VM cluster and which actions are to be performed by the maintenance update. Applies to Exadata Cloud Service instances only.
    """

    #: A constant which can be used with the update_action property of a UpdateDetails.
    #: This constant has a value of "ROLLING_APPLY"
    UPDATE_ACTION_ROLLING_APPLY = "ROLLING_APPLY"

    #: A constant which can be used with the update_action property of a UpdateDetails.
    #: This constant has a value of "NON_ROLLING_APPLY"
    UPDATE_ACTION_NON_ROLLING_APPLY = "NON_ROLLING_APPLY"

    #: A constant which can be used with the update_action property of a UpdateDetails.
    #: This constant has a value of "PRECHECK"
    UPDATE_ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the update_action property of a UpdateDetails.
    #: This constant has a value of "ROLLBACK"
    UPDATE_ACTION_ROLLBACK = "ROLLBACK"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param update_id:
            The value to assign to the update_id property of this UpdateDetails.
        :type update_id: str

        :param update_action:
            The value to assign to the update_action property of this UpdateDetails.
            Allowed values for this property are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK"
        :type update_action: str

        """
        self.swagger_types = {
            'update_id': 'str',
            'update_action': 'str'
        }

        self.attribute_map = {
            'update_id': 'updateId',
            'update_action': 'updateAction'
        }

        self._update_id = None
        self._update_action = None

    @property
    def update_id(self):
        """
        Gets the update_id of this UpdateDetails.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The update_id of this UpdateDetails.
        :rtype: str
        """
        return self._update_id

    @update_id.setter
    def update_id(self, update_id):
        """
        Sets the update_id of this UpdateDetails.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param update_id: The update_id of this UpdateDetails.
        :type: str
        """
        self._update_id = update_id

    @property
    def update_action(self):
        """
        Gets the update_action of this UpdateDetails.
        The update action.

        Allowed values for this property are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK"


        :return: The update_action of this UpdateDetails.
        :rtype: str
        """
        return self._update_action

    @update_action.setter
    def update_action(self, update_action):
        """
        Sets the update_action of this UpdateDetails.
        The update action.


        :param update_action: The update_action of this UpdateDetails.
        :type: str
        """
        allowed_values = ["ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(update_action, allowed_values):
            raise ValueError(
                "Invalid value for `update_action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._update_action = update_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
