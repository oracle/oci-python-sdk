# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .db_system_source import DbSystemSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemSourceFromPitr(DbSystemSource):
    """
    DB System OCID to perform a point in time recovery to the current point in time.

    DB System OCID and recovery point to perform a point in time recovery to the
    specified recovery point.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemSourceFromPitr object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.DbSystemSourceFromPitr.source_type` attribute
        of this class is ``PITR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this DbSystemSourceFromPitr.
            Allowed values for this property are: "NONE", "BACKUP", "PITR", "IMPORTURL"
        :type source_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbSystemSourceFromPitr.
        :type db_system_id: str

        :param recovery_point:
            The value to assign to the recovery_point property of this DbSystemSourceFromPitr.
        :type recovery_point: datetime

        """
        self.swagger_types = {
            'source_type': 'str',
            'db_system_id': 'str',
            'recovery_point': 'datetime'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'db_system_id': 'dbSystemId',
            'recovery_point': 'recoveryPoint'
        }

        self._source_type = None
        self._db_system_id = None
        self._recovery_point = None
        self._source_type = 'PITR'

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this DbSystemSourceFromPitr.
        The OCID of the DB System from which a backup shall be selected to be
        restored when creating the new DB System. Use this together with
        recovery point to perform a point in time recovery operation.


        :return: The db_system_id of this DbSystemSourceFromPitr.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbSystemSourceFromPitr.
        The OCID of the DB System from which a backup shall be selected to be
        restored when creating the new DB System. Use this together with
        recovery point to perform a point in time recovery operation.


        :param db_system_id: The db_system_id of this DbSystemSourceFromPitr.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def recovery_point(self):
        """
        Gets the recovery_point of this DbSystemSourceFromPitr.
        The date and time, as per RFC 3339, of the change up to which the
        new DB System shall be restored to, using a backup and logs from the
        original DB System. In case no point in time is specified, then this
        new DB System shall be restored up to the latest change recorded for
        the original DB System.


        :return: The recovery_point of this DbSystemSourceFromPitr.
        :rtype: datetime
        """
        return self._recovery_point

    @recovery_point.setter
    def recovery_point(self, recovery_point):
        """
        Sets the recovery_point of this DbSystemSourceFromPitr.
        The date and time, as per RFC 3339, of the change up to which the
        new DB System shall be restored to, using a backup and logs from the
        original DB System. In case no point in time is specified, then this
        new DB System shall be restored up to the latest change recorded for
        the original DB System.


        :param recovery_point: The recovery_point of this DbSystemSourceFromPitr.
        :type: datetime
        """
        self._recovery_point = recovery_point

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
