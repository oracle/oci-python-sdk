# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StartMigrationDetails(object):
    """
    Parameters to specify to a Migration job operation.
    """

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_TGT"
    WAIT_AFTER_ODMS_VALIDATE_TGT = "ODMS_VALIDATE_TGT"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_SRC = "ODMS_VALIDATE_SRC"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_PREMIGRATION_ADVISOR"
    WAIT_AFTER_ODMS_VALIDATE_PREMIGRATION_ADVISOR = "ODMS_VALIDATE_PREMIGRATION_ADVISOR"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_GG_HUB"
    WAIT_AFTER_ODMS_VALIDATE_GG_HUB = "ODMS_VALIDATE_GG_HUB"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS = "ODMS_VALIDATE_DATAPUMP_SETTINGS"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC = "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT = "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SRC = "ODMS_VALIDATE_DATAPUMP_SRC"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC = "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_VALIDATE"
    WAIT_AFTER_ODMS_VALIDATE = "ODMS_VALIDATE"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_PREPARE"
    WAIT_AFTER_ODMS_PREPARE = "ODMS_PREPARE"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_EXPORT = "ODMS_INITIAL_LOAD_EXPORT"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_DATA_UPLOAD"
    WAIT_AFTER_ODMS_DATA_UPLOAD = "ODMS_DATA_UPLOAD"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_INITIAL_LOAD_IMPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_IMPORT = "ODMS_INITIAL_LOAD_IMPORT"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_POST_INITIAL_LOAD"
    WAIT_AFTER_ODMS_POST_INITIAL_LOAD = "ODMS_POST_INITIAL_LOAD"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_PREPARE_REPLICATION_TARGET"
    WAIT_AFTER_ODMS_PREPARE_REPLICATION_TARGET = "ODMS_PREPARE_REPLICATION_TARGET"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_MONITOR_REPLICATION_LAG"
    WAIT_AFTER_ODMS_MONITOR_REPLICATION_LAG = "ODMS_MONITOR_REPLICATION_LAG"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_SWITCHOVER"
    WAIT_AFTER_ODMS_SWITCHOVER = "ODMS_SWITCHOVER"

    #: A constant which can be used with the wait_after property of a StartMigrationDetails.
    #: This constant has a value of "ODMS_CLEANUP"
    WAIT_AFTER_ODMS_CLEANUP = "ODMS_CLEANUP"

    def __init__(self, **kwargs):
        """
        Initializes a new StartMigrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wait_after:
            The value to assign to the wait_after property of this StartMigrationDetails.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"
        :type wait_after: str

        """
        self.swagger_types = {
            'wait_after': 'str'
        }

        self.attribute_map = {
            'wait_after': 'waitAfter'
        }

        self._wait_after = None

    @property
    def wait_after(self):
        """
        Gets the wait_after of this StartMigrationDetails.
        Name of a migration phase. The Job will wait after executing this
        phase until the Resume Job endpoint is called.

        Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"


        :return: The wait_after of this StartMigrationDetails.
        :rtype: str
        """
        return self._wait_after

    @wait_after.setter
    def wait_after(self, wait_after):
        """
        Sets the wait_after of this StartMigrationDetails.
        Name of a migration phase. The Job will wait after executing this
        phase until the Resume Job endpoint is called.


        :param wait_after: The wait_after of this StartMigrationDetails.
        :type: str
        """
        allowed_values = ["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]
        if not value_allowed_none_or_none_sentinel(wait_after, allowed_values):
            raise ValueError(
                "Invalid value for `wait_after`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._wait_after = wait_after

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
