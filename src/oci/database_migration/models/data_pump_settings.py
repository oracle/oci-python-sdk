# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataPumpSettings(object):
    """
    Optional settings for Data Pump Export and Import jobs
    """

    #: A constant which can be used with the job_mode property of a DataPumpSettings.
    #: This constant has a value of "FULL"
    JOB_MODE_FULL = "FULL"

    #: A constant which can be used with the job_mode property of a DataPumpSettings.
    #: This constant has a value of "SCHEMA"
    JOB_MODE_SCHEMA = "SCHEMA"

    #: A constant which can be used with the job_mode property of a DataPumpSettings.
    #: This constant has a value of "TABLE"
    JOB_MODE_TABLE = "TABLE"

    #: A constant which can be used with the job_mode property of a DataPumpSettings.
    #: This constant has a value of "TABLESPACE"
    JOB_MODE_TABLESPACE = "TABLESPACE"

    #: A constant which can be used with the job_mode property of a DataPumpSettings.
    #: This constant has a value of "TRANSPORTABLE"
    JOB_MODE_TRANSPORTABLE = "TRANSPORTABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new DataPumpSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_mode:
            The value to assign to the job_mode property of this DataPumpSettings.
            Allowed values for this property are: "FULL", "SCHEMA", "TABLE", "TABLESPACE", "TRANSPORTABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_mode: str

        :param data_pump_parameters:
            The value to assign to the data_pump_parameters property of this DataPumpSettings.
        :type data_pump_parameters: oci.database_migration.models.DataPumpParameters

        :param metadata_remaps:
            The value to assign to the metadata_remaps property of this DataPumpSettings.
        :type metadata_remaps: list[oci.database_migration.models.MetadataRemap]

        :param export_directory_object:
            The value to assign to the export_directory_object property of this DataPumpSettings.
        :type export_directory_object: oci.database_migration.models.DirectoryObject

        :param import_directory_object:
            The value to assign to the import_directory_object property of this DataPumpSettings.
        :type import_directory_object: oci.database_migration.models.DirectoryObject

        """
        self.swagger_types = {
            'job_mode': 'str',
            'data_pump_parameters': 'DataPumpParameters',
            'metadata_remaps': 'list[MetadataRemap]',
            'export_directory_object': 'DirectoryObject',
            'import_directory_object': 'DirectoryObject'
        }

        self.attribute_map = {
            'job_mode': 'jobMode',
            'data_pump_parameters': 'dataPumpParameters',
            'metadata_remaps': 'metadataRemaps',
            'export_directory_object': 'exportDirectoryObject',
            'import_directory_object': 'importDirectoryObject'
        }

        self._job_mode = None
        self._data_pump_parameters = None
        self._metadata_remaps = None
        self._export_directory_object = None
        self._import_directory_object = None

    @property
    def job_mode(self):
        """
        Gets the job_mode of this DataPumpSettings.
        Data Pump job mode.
        Refer to `Data Pump Export Modes `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4

        Allowed values for this property are: "FULL", "SCHEMA", "TABLE", "TABLESPACE", "TRANSPORTABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_mode of this DataPumpSettings.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        """
        Sets the job_mode of this DataPumpSettings.
        Data Pump job mode.
        Refer to `Data Pump Export Modes `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4


        :param job_mode: The job_mode of this DataPumpSettings.
        :type: str
        """
        allowed_values = ["FULL", "SCHEMA", "TABLE", "TABLESPACE", "TRANSPORTABLE"]
        if not value_allowed_none_or_none_sentinel(job_mode, allowed_values):
            job_mode = 'UNKNOWN_ENUM_VALUE'
        self._job_mode = job_mode

    @property
    def data_pump_parameters(self):
        """
        Gets the data_pump_parameters of this DataPumpSettings.

        :return: The data_pump_parameters of this DataPumpSettings.
        :rtype: oci.database_migration.models.DataPumpParameters
        """
        return self._data_pump_parameters

    @data_pump_parameters.setter
    def data_pump_parameters(self, data_pump_parameters):
        """
        Sets the data_pump_parameters of this DataPumpSettings.

        :param data_pump_parameters: The data_pump_parameters of this DataPumpSettings.
        :type: oci.database_migration.models.DataPumpParameters
        """
        self._data_pump_parameters = data_pump_parameters

    @property
    def metadata_remaps(self):
        """
        Gets the metadata_remaps of this DataPumpSettings.
        Defines remapping to be applied to objects as they are processed.
        Refer to `METADATA_REMAP Procedure `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D


        :return: The metadata_remaps of this DataPumpSettings.
        :rtype: list[oci.database_migration.models.MetadataRemap]
        """
        return self._metadata_remaps

    @metadata_remaps.setter
    def metadata_remaps(self, metadata_remaps):
        """
        Sets the metadata_remaps of this DataPumpSettings.
        Defines remapping to be applied to objects as they are processed.
        Refer to `METADATA_REMAP Procedure `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D


        :param metadata_remaps: The metadata_remaps of this DataPumpSettings.
        :type: list[oci.database_migration.models.MetadataRemap]
        """
        self._metadata_remaps = metadata_remaps

    @property
    def export_directory_object(self):
        """
        Gets the export_directory_object of this DataPumpSettings.

        :return: The export_directory_object of this DataPumpSettings.
        :rtype: oci.database_migration.models.DirectoryObject
        """
        return self._export_directory_object

    @export_directory_object.setter
    def export_directory_object(self, export_directory_object):
        """
        Sets the export_directory_object of this DataPumpSettings.

        :param export_directory_object: The export_directory_object of this DataPumpSettings.
        :type: oci.database_migration.models.DirectoryObject
        """
        self._export_directory_object = export_directory_object

    @property
    def import_directory_object(self):
        """
        Gets the import_directory_object of this DataPumpSettings.

        :return: The import_directory_object of this DataPumpSettings.
        :rtype: oci.database_migration.models.DirectoryObject
        """
        return self._import_directory_object

    @import_directory_object.setter
    def import_directory_object(self, import_directory_object):
        """
        Sets the import_directory_object of this DataPumpSettings.

        :param import_directory_object: The import_directory_object of this DataPumpSettings.
        :type: oci.database_migration.models.DirectoryObject
        """
        self._import_directory_object = import_directory_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
