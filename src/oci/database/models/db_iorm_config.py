# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbIormConfig(object):
    """
    IORM Config setting response for this database
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbIormConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_name:
            The value to assign to the db_name property of this DbIormConfig.
        :type db_name: str

        :param share:
            The value to assign to the share property of this DbIormConfig.
        :type share: int

        :param flash_cache_limit:
            The value to assign to the flash_cache_limit property of this DbIormConfig.
        :type flash_cache_limit: str

        """
        self.swagger_types = {
            'db_name': 'str',
            'share': 'int',
            'flash_cache_limit': 'str'
        }

        self.attribute_map = {
            'db_name': 'dbName',
            'share': 'share',
            'flash_cache_limit': 'flashCacheLimit'
        }

        self._db_name = None
        self._share = None
        self._flash_cache_limit = None

    @property
    def db_name(self):
        """
        Gets the db_name of this DbIormConfig.
        Database Name. For default DbPlan, the dbName will always be `default`


        :return: The db_name of this DbIormConfig.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this DbIormConfig.
        Database Name. For default DbPlan, the dbName will always be `default`


        :param db_name: The db_name of this DbIormConfig.
        :type: str
        """
        self._db_name = db_name

    @property
    def share(self):
        """
        Gets the share of this DbIormConfig.
        Relative priority of a database


        :return: The share of this DbIormConfig.
        :rtype: int
        """
        return self._share

    @share.setter
    def share(self, share):
        """
        Sets the share of this DbIormConfig.
        Relative priority of a database


        :param share: The share of this DbIormConfig.
        :type: int
        """
        self._share = share

    @property
    def flash_cache_limit(self):
        """
        Gets the flash_cache_limit of this DbIormConfig.
        Flash Cache limit, internally configured based on shares


        :return: The flash_cache_limit of this DbIormConfig.
        :rtype: str
        """
        return self._flash_cache_limit

    @flash_cache_limit.setter
    def flash_cache_limit(self, flash_cache_limit):
        """
        Sets the flash_cache_limit of this DbIormConfig.
        Flash Cache limit, internally configured based on shares


        :param flash_cache_limit: The flash_cache_limit of this DbIormConfig.
        :type: str
        """
        self._flash_cache_limit = flash_cache_limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
