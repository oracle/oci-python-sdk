# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .db_system_source import DbSystemSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemSourceImportFromUrl(DbSystemSource):
    """
    An Object Storage PAR from which to import the DB System initial data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemSourceImportFromUrl object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.DbSystemSourceImportFromUrl.source_type` attribute
        of this class is ``IMPORTURL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this DbSystemSourceImportFromUrl.
            Allowed values for this property are: "NONE", "BACKUP", "IMPORTURL"
        :type source_type: str

        """
        self.swagger_types = {
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType'
        }

        self._source_type = None
        self._source_type = 'IMPORTURL'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
