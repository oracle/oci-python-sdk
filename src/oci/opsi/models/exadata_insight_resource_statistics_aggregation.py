# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsightResourceStatisticsAggregation(object):
    """
    Contains resource details and current statistics
    """

    #: A constant which can be used with the exadata_resource_type property of a ExadataInsightResourceStatisticsAggregation.
    #: This constant has a value of "DATABASE"
    EXADATA_RESOURCE_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the exadata_resource_type property of a ExadataInsightResourceStatisticsAggregation.
    #: This constant has a value of "HOST"
    EXADATA_RESOURCE_TYPE_HOST = "HOST"

    #: A constant which can be used with the exadata_resource_type property of a ExadataInsightResourceStatisticsAggregation.
    #: This constant has a value of "STORAGE_SERVER"
    EXADATA_RESOURCE_TYPE_STORAGE_SERVER = "STORAGE_SERVER"

    #: A constant which can be used with the exadata_resource_type property of a ExadataInsightResourceStatisticsAggregation.
    #: This constant has a value of "DISKGROUP"
    EXADATA_RESOURCE_TYPE_DISKGROUP = "DISKGROUP"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsightResourceStatisticsAggregation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.ExadataStorageServerStatisticsSummary`
        * :class:`~oci.opsi.models.ExadataHostStatisticsSummary`
        * :class:`~oci.opsi.models.ExadataDatabaseStatisticsSummary`
        * :class:`~oci.opsi.models.ExadataDiskgroupStatisticsSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_resource_type:
            The value to assign to the exadata_resource_type property of this ExadataInsightResourceStatisticsAggregation.
            Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_resource_type: str

        """
        self.swagger_types = {
            'exadata_resource_type': 'str'
        }

        self.attribute_map = {
            'exadata_resource_type': 'exadataResourceType'
        }

        self._exadata_resource_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['exadataResourceType']

        if type == 'STORAGE_SERVER':
            return 'ExadataStorageServerStatisticsSummary'

        if type == 'HOST':
            return 'ExadataHostStatisticsSummary'

        if type == 'DATABASE':
            return 'ExadataDatabaseStatisticsSummary'

        if type == 'DISKGROUP':
            return 'ExadataDiskgroupStatisticsSummary'
        else:
            return 'ExadataInsightResourceStatisticsAggregation'

    @property
    def exadata_resource_type(self):
        """
        **[Required]** Gets the exadata_resource_type of this ExadataInsightResourceStatisticsAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)

        Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_resource_type of this ExadataInsightResourceStatisticsAggregation.
        :rtype: str
        """
        return self._exadata_resource_type

    @exadata_resource_type.setter
    def exadata_resource_type(self, exadata_resource_type):
        """
        Sets the exadata_resource_type of this ExadataInsightResourceStatisticsAggregation.
        Defines the resource type for an exadata  (example: DATABASE, STORAGE_SERVER, HOST, DISKGROUP)


        :param exadata_resource_type: The exadata_resource_type of this ExadataInsightResourceStatisticsAggregation.
        :type: str
        """
        allowed_values = ["DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP"]
        if not value_allowed_none_or_none_sentinel(exadata_resource_type, allowed_values):
            exadata_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_resource_type = exadata_resource_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
