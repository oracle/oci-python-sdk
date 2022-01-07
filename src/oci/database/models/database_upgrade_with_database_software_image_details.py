# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_upgrade_source_base import DatabaseUpgradeSourceBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUpgradeWithDatabaseSoftwareImageDetails(DatabaseUpgradeSourceBase):
    """
    Details of the database software image to be used to upgrade a database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUpgradeWithDatabaseSoftwareImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.DatabaseUpgradeWithDatabaseSoftwareImageDetails.source` attribute
        of this class is ``DB_SOFTWARE_IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
            Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"
        :type source: str

        :param options:
            The value to assign to the options property of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        :type options: str

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        :type database_software_image_id: str

        """
        self.swagger_types = {
            'source': 'str',
            'options': 'str',
            'database_software_image_id': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'options': 'options',
            'database_software_image_id': 'databaseSoftwareImageId'
        }

        self._source = None
        self._options = None
        self._database_software_image_id = None
        self._source = 'DB_SOFTWARE_IMAGE'

    @property
    def database_software_image_id(self):
        """
        **[Required]** Gets the database_software_image_id of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        The database software image `OCID`__ of the image to be used to upgrade a database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_software_image_id of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        :rtype: str
        """
        return self._database_software_image_id

    @database_software_image_id.setter
    def database_software_image_id(self, database_software_image_id):
        """
        Sets the database_software_image_id of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        The database software image `OCID`__ of the image to be used to upgrade a database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_software_image_id: The database_software_image_id of this DatabaseUpgradeWithDatabaseSoftwareImageDetails.
        :type: str
        """
        self._database_software_image_id = database_software_image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
