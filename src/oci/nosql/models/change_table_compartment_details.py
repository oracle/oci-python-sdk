# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeTableCompartmentDetails(object):
    """
    Specification of both from and to compartments.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeTableCompartmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param from_compartment_id:
            The value to assign to the from_compartment_id property of this ChangeTableCompartmentDetails.
        :type from_compartment_id: str

        :param to_compartment_id:
            The value to assign to the to_compartment_id property of this ChangeTableCompartmentDetails.
        :type to_compartment_id: str

        """
        self.swagger_types = {
            'from_compartment_id': 'str',
            'to_compartment_id': 'str'
        }

        self.attribute_map = {
            'from_compartment_id': 'fromCompartmentId',
            'to_compartment_id': 'toCompartmentId'
        }

        self._from_compartment_id = None
        self._to_compartment_id = None

    @property
    def from_compartment_id(self):
        """
        Gets the from_compartment_id of this ChangeTableCompartmentDetails.
        The OCID of the table's current compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and fromCompartmentId is supplied, the latter
        must match the identified table's current compartmentId.


        :return: The from_compartment_id of this ChangeTableCompartmentDetails.
        :rtype: str
        """
        return self._from_compartment_id

    @from_compartment_id.setter
    def from_compartment_id(self, from_compartment_id):
        """
        Sets the from_compartment_id of this ChangeTableCompartmentDetails.
        The OCID of the table's current compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and fromCompartmentId is supplied, the latter
        must match the identified table's current compartmentId.


        :param from_compartment_id: The from_compartment_id of this ChangeTableCompartmentDetails.
        :type: str
        """
        self._from_compartment_id = from_compartment_id

    @property
    def to_compartment_id(self):
        """
        **[Required]** Gets the to_compartment_id of this ChangeTableCompartmentDetails.
        The OCID of the table's new compartment.


        :return: The to_compartment_id of this ChangeTableCompartmentDetails.
        :rtype: str
        """
        return self._to_compartment_id

    @to_compartment_id.setter
    def to_compartment_id(self, to_compartment_id):
        """
        Sets the to_compartment_id of this ChangeTableCompartmentDetails.
        The OCID of the table's new compartment.


        :param to_compartment_id: The to_compartment_id of this ChangeTableCompartmentDetails.
        :type: str
        """
        self._to_compartment_id = to_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
