# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConvertToPdbDetails(object):
    """
    Details for converting a non-container database to pluggable database.
    """

    #: A constant which can be used with the action property of a ConvertToPdbDetails.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a ConvertToPdbDetails.
    #: This constant has a value of "CONVERT"
    ACTION_CONVERT = "CONVERT"

    #: A constant which can be used with the action property of a ConvertToPdbDetails.
    #: This constant has a value of "SYNC"
    ACTION_SYNC = "SYNC"

    #: A constant which can be used with the action property of a ConvertToPdbDetails.
    #: This constant has a value of "SYNC_ROLLBACK"
    ACTION_SYNC_ROLLBACK = "SYNC_ROLLBACK"

    def __init__(self, **kwargs):
        """
        Initializes a new ConvertToPdbDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this ConvertToPdbDetails.
            Allowed values for this property are: "PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK"
        :type action: str

        :param convert_to_pdb_target_details:
            The value to assign to the convert_to_pdb_target_details property of this ConvertToPdbDetails.
        :type convert_to_pdb_target_details: oci.database.models.ConvertToPdbTargetBase

        """
        self.swagger_types = {
            'action': 'str',
            'convert_to_pdb_target_details': 'ConvertToPdbTargetBase'
        }

        self.attribute_map = {
            'action': 'action',
            'convert_to_pdb_target_details': 'convertToPdbTargetDetails'
        }

        self._action = None
        self._convert_to_pdb_target_details = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ConvertToPdbDetails.
        The operations used to convert a non-container database to a pluggable database.
        - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database.
        - Use `CONVERT` to convert a non-container database into a pluggable database.
        - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API.
        - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.

        Allowed values for this property are: "PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK"


        :return: The action of this ConvertToPdbDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ConvertToPdbDetails.
        The operations used to convert a non-container database to a pluggable database.
        - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database.
        - Use `CONVERT` to convert a non-container database into a pluggable database.
        - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API.
        - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.


        :param action: The action of this ConvertToPdbDetails.
        :type: str
        """
        allowed_values = ["PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def convert_to_pdb_target_details(self):
        """
        Gets the convert_to_pdb_target_details of this ConvertToPdbDetails.

        :return: The convert_to_pdb_target_details of this ConvertToPdbDetails.
        :rtype: oci.database.models.ConvertToPdbTargetBase
        """
        return self._convert_to_pdb_target_details

    @convert_to_pdb_target_details.setter
    def convert_to_pdb_target_details(self, convert_to_pdb_target_details):
        """
        Sets the convert_to_pdb_target_details of this ConvertToPdbDetails.

        :param convert_to_pdb_target_details: The convert_to_pdb_target_details of this ConvertToPdbDetails.
        :type: oci.database.models.ConvertToPdbTargetBase
        """
        self._convert_to_pdb_target_details = convert_to_pdb_target_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
