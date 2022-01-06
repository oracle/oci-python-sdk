# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbIormConfigUpdateDetail(object):
    """
    Details of the IORM configuration settings update request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbIormConfigUpdateDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_name:
            The value to assign to the db_name property of this DbIormConfigUpdateDetail.
        :type db_name: str

        :param share:
            The value to assign to the share property of this DbIormConfigUpdateDetail.
        :type share: int

        """
        self.swagger_types = {
            'db_name': 'str',
            'share': 'int'
        }

        self.attribute_map = {
            'db_name': 'dbName',
            'share': 'share'
        }

        self._db_name = None
        self._share = None

    @property
    def db_name(self):
        """
        Gets the db_name of this DbIormConfigUpdateDetail.
        The database name. For the default `DbPlan`, the `dbName` is `default`.


        :return: The db_name of this DbIormConfigUpdateDetail.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this DbIormConfigUpdateDetail.
        The database name. For the default `DbPlan`, the `dbName` is `default`.


        :param db_name: The db_name of this DbIormConfigUpdateDetail.
        :type: str
        """
        self._db_name = db_name

    @property
    def share(self):
        """
        Gets the share of this DbIormConfigUpdateDetail.
        The relative priority of this database.


        :return: The share of this DbIormConfigUpdateDetail.
        :rtype: int
        """
        return self._share

    @share.setter
    def share(self, share):
        """
        Sets the share of this DbIormConfigUpdateDetail.
        The relative priority of this database.


        :param share: The share of this DbIormConfigUpdateDetail.
        :type: int
        """
        self._share = share

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
