# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisassociateMonitoredResourcesDetails(object):
    """
    The information required to create new monitored resource association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DisassociateMonitoredResourcesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DisassociateMonitoredResourcesDetails.
        :type compartment_id: str

        :param association_type:
            The value to assign to the association_type property of this DisassociateMonitoredResourcesDetails.
        :type association_type: str

        :param source_resource_id:
            The value to assign to the source_resource_id property of this DisassociateMonitoredResourcesDetails.
        :type source_resource_id: str

        :param destination_resource_id:
            The value to assign to the destination_resource_id property of this DisassociateMonitoredResourcesDetails.
        :type destination_resource_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'association_type': 'str',
            'source_resource_id': 'str',
            'destination_resource_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'association_type': 'associationType',
            'source_resource_id': 'sourceResourceId',
            'destination_resource_id': 'destinationResourceId'
        }

        self._compartment_id = None
        self._association_type = None
        self._source_resource_id = None
        self._destination_resource_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DisassociateMonitoredResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DisassociateMonitoredResourcesDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DisassociateMonitoredResourcesDetails.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DisassociateMonitoredResourcesDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def association_type(self):
        """
        Gets the association_type of this DisassociateMonitoredResourcesDetails.
        Association type to be created between source and destination resources


        :return: The association_type of this DisassociateMonitoredResourcesDetails.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this DisassociateMonitoredResourcesDetails.
        Association type to be created between source and destination resources


        :param association_type: The association_type of this DisassociateMonitoredResourcesDetails.
        :type: str
        """
        self._association_type = association_type

    @property
    def source_resource_id(self):
        """
        Gets the source_resource_id of this DisassociateMonitoredResourcesDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_resource_id of this DisassociateMonitoredResourcesDetails.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """
        Sets the source_resource_id of this DisassociateMonitoredResourcesDetails.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_resource_id: The source_resource_id of this DisassociateMonitoredResourcesDetails.
        :type: str
        """
        self._source_resource_id = source_resource_id

    @property
    def destination_resource_id(self):
        """
        Gets the destination_resource_id of this DisassociateMonitoredResourcesDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The destination_resource_id of this DisassociateMonitoredResourcesDetails.
        :rtype: str
        """
        return self._destination_resource_id

    @destination_resource_id.setter
    def destination_resource_id(self, destination_resource_id):
        """
        Sets the destination_resource_id of this DisassociateMonitoredResourcesDetails.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param destination_resource_id: The destination_resource_id of this DisassociateMonitoredResourcesDetails.
        :type: str
        """
        self._destination_resource_id = destination_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
