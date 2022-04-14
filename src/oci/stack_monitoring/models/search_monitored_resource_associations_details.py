# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchMonitoredResourceAssociationsDetails(object):
    """
    The information required to search monitored resource associations.
    """

    #: A constant which can be used with the sort_by property of a SearchMonitoredResourceAssociationsDetails.
    #: This constant has a value of "TIME_CREATED"
    SORT_BY_TIME_CREATED = "TIME_CREATED"

    #: A constant which can be used with the sort_by property of a SearchMonitoredResourceAssociationsDetails.
    #: This constant has a value of "ASSOC_TYPE"
    SORT_BY_ASSOC_TYPE = "ASSOC_TYPE"

    #: A constant which can be used with the sort_order property of a SearchMonitoredResourceAssociationsDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a SearchMonitoredResourceAssociationsDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchMonitoredResourceAssociationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SearchMonitoredResourceAssociationsDetails.
        :type compartment_id: str

        :param source_resource_id:
            The value to assign to the source_resource_id property of this SearchMonitoredResourceAssociationsDetails.
        :type source_resource_id: str

        :param source_resource_name:
            The value to assign to the source_resource_name property of this SearchMonitoredResourceAssociationsDetails.
        :type source_resource_name: str

        :param source_resource_type:
            The value to assign to the source_resource_type property of this SearchMonitoredResourceAssociationsDetails.
        :type source_resource_type: str

        :param destination_resource_id:
            The value to assign to the destination_resource_id property of this SearchMonitoredResourceAssociationsDetails.
        :type destination_resource_id: str

        :param destination_resource_name:
            The value to assign to the destination_resource_name property of this SearchMonitoredResourceAssociationsDetails.
        :type destination_resource_name: str

        :param destination_resource_type:
            The value to assign to the destination_resource_type property of this SearchMonitoredResourceAssociationsDetails.
        :type destination_resource_type: str

        :param association_type:
            The value to assign to the association_type property of this SearchMonitoredResourceAssociationsDetails.
        :type association_type: str

        :param sort_by:
            The value to assign to the sort_by property of this SearchMonitoredResourceAssociationsDetails.
            Allowed values for this property are: "TIME_CREATED", "ASSOC_TYPE"
        :type sort_by: str

        :param sort_order:
            The value to assign to the sort_order property of this SearchMonitoredResourceAssociationsDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'source_resource_id': 'str',
            'source_resource_name': 'str',
            'source_resource_type': 'str',
            'destination_resource_id': 'str',
            'destination_resource_name': 'str',
            'destination_resource_type': 'str',
            'association_type': 'str',
            'sort_by': 'str',
            'sort_order': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'source_resource_id': 'sourceResourceId',
            'source_resource_name': 'sourceResourceName',
            'source_resource_type': 'sourceResourceType',
            'destination_resource_id': 'destinationResourceId',
            'destination_resource_name': 'destinationResourceName',
            'destination_resource_type': 'destinationResourceType',
            'association_type': 'associationType',
            'sort_by': 'sortBy',
            'sort_order': 'sortOrder'
        }

        self._compartment_id = None
        self._source_resource_id = None
        self._source_resource_name = None
        self._source_resource_type = None
        self._destination_resource_id = None
        self._destination_resource_name = None
        self._destination_resource_type = None
        self._association_type = None
        self._sort_by = None
        self._sort_order = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SearchMonitoredResourceAssociationsDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SearchMonitoredResourceAssociationsDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_resource_id(self):
        """
        Gets the source_resource_id of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_resource_id of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """
        Sets the source_resource_id of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_resource_id: The source_resource_id of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._source_resource_id = source_resource_id

    @property
    def source_resource_name(self):
        """
        Gets the source_resource_name of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Name


        :return: The source_resource_name of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._source_resource_name

    @source_resource_name.setter
    def source_resource_name(self, source_resource_name):
        """
        Sets the source_resource_name of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Name


        :param source_resource_name: The source_resource_name of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._source_resource_name = source_resource_name

    @property
    def source_resource_type(self):
        """
        Gets the source_resource_type of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Type


        :return: The source_resource_type of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._source_resource_type

    @source_resource_type.setter
    def source_resource_type(self, source_resource_type):
        """
        Sets the source_resource_type of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Type


        :param source_resource_type: The source_resource_type of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._source_resource_type = source_resource_type

    @property
    def destination_resource_id(self):
        """
        Gets the destination_resource_id of this SearchMonitoredResourceAssociationsDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The destination_resource_id of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._destination_resource_id

    @destination_resource_id.setter
    def destination_resource_id(self, destination_resource_id):
        """
        Sets the destination_resource_id of this SearchMonitoredResourceAssociationsDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param destination_resource_id: The destination_resource_id of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._destination_resource_id = destination_resource_id

    @property
    def destination_resource_name(self):
        """
        Gets the destination_resource_name of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Name


        :return: The destination_resource_name of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._destination_resource_name

    @destination_resource_name.setter
    def destination_resource_name(self, destination_resource_name):
        """
        Sets the destination_resource_name of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Name


        :param destination_resource_name: The destination_resource_name of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._destination_resource_name = destination_resource_name

    @property
    def destination_resource_type(self):
        """
        Gets the destination_resource_type of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Type


        :return: The destination_resource_type of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._destination_resource_type

    @destination_resource_type.setter
    def destination_resource_type(self, destination_resource_type):
        """
        Sets the destination_resource_type of this SearchMonitoredResourceAssociationsDetails.
        Source Monitored Resource Type


        :param destination_resource_type: The destination_resource_type of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._destination_resource_type = destination_resource_type

    @property
    def association_type(self):
        """
        Gets the association_type of this SearchMonitoredResourceAssociationsDetails.
        Association type to be created between source and destination resources


        :return: The association_type of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this SearchMonitoredResourceAssociationsDetails.
        Association type to be created between source and destination resources


        :param association_type: The association_type of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        self._association_type = association_type

    @property
    def sort_by(self):
        """
        Gets the sort_by of this SearchMonitoredResourceAssociationsDetails.
        The field to sort by. Only one sort order may be provided.
        Default order for timeCreated is descending. Default order for assocType is descending.

        Allowed values for this property are: "TIME_CREATED", "ASSOC_TYPE"


        :return: The sort_by of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchMonitoredResourceAssociationsDetails.
        The field to sort by. Only one sort order may be provided.
        Default order for timeCreated is descending. Default order for assocType is descending.


        :param sort_by: The sort_by of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        allowed_values = ["TIME_CREATED", "ASSOC_TYPE"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                "Invalid value for `sort_by`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_by = sort_by

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SearchMonitoredResourceAssociationsDetails.
        The sort order to use, either 'ASC' or 'DESC'.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this SearchMonitoredResourceAssociationsDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SearchMonitoredResourceAssociationsDetails.
        The sort order to use, either 'ASC' or 'DESC'.


        :param sort_order: The sort_order of this SearchMonitoredResourceAssociationsDetails.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(sort_order, allowed_values):
            raise ValueError(
                "Invalid value for `sort_order`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_order = sort_order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
