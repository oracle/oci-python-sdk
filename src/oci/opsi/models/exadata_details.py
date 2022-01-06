# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataDetails(object):
    """
    Partial information about the exadata which includes id and name.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExadataDetails.
        :type id: str

        :param name:
            The value to assign to the name property of this ExadataDetails.
        :type name: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = None
        self._name = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExadataDetails.
        The `OCID`__ of exadata insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ExadataDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExadataDetails.
        The `OCID`__ of exadata insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExadataDetails.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExadataDetails.
        Name of exadata insight resource.


        :return: The name of this ExadataDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExadataDetails.
        Name of exadata insight resource.


        :param name: The name of this ExadataDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
