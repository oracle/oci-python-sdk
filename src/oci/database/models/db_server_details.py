# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbServerDetails(object):
    """
    Details of the Exacc Db server. Applies to Exadata Cloud@Customer instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbServerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_server_id:
            The value to assign to the db_server_id property of this DbServerDetails.
        :type db_server_id: str

        """
        self.swagger_types = {
            'db_server_id': 'str'
        }

        self.attribute_map = {
            'db_server_id': 'dbServerId'
        }

        self._db_server_id = None

    @property
    def db_server_id(self):
        """
        **[Required]** Gets the db_server_id of this DbServerDetails.
        The `OCID`__ of Exacc Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_server_id of this DbServerDetails.
        :rtype: str
        """
        return self._db_server_id

    @db_server_id.setter
    def db_server_id(self, db_server_id):
        """
        Sets the db_server_id of this DbServerDetails.
        The `OCID`__ of Exacc Db server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_server_id: The db_server_id of this DbServerDetails.
        :type: str
        """
        self._db_server_id = db_server_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
