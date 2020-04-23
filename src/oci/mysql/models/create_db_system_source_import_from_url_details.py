# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_db_system_source_details import CreateDbSystemSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbSystemSourceImportFromUrlDetails(CreateDbSystemSourceDetails):
    """
    An Object Storage PAR from which to import the DB System initial data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbSystemSourceImportFromUrlDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.CreateDbSystemSourceImportFromUrlDetails.source_type` attribute
        of this class is ``IMPORTURL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this CreateDbSystemSourceImportFromUrlDetails.
            Allowed values for this property are: "NONE", "BACKUP", "IMPORTURL"
        :type source_type: str

        :param source_url:
            The value to assign to the source_url property of this CreateDbSystemSourceImportFromUrlDetails.
        :type source_url: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'source_url': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source_url': 'sourceUrl'
        }

        self._source_type = None
        self._source_url = None
        self._source_type = 'IMPORTURL'

    @property
    def source_url(self):
        """
        **[Required]** Gets the source_url of this CreateDbSystemSourceImportFromUrlDetails.
        The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.


        :return: The source_url of this CreateDbSystemSourceImportFromUrlDetails.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """
        Sets the source_url of this CreateDbSystemSourceImportFromUrlDetails.
        The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.


        :param source_url: The source_url of this CreateDbSystemSourceImportFromUrlDetails.
        :type: str
        """
        self._source_url = source_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
