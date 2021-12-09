# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompartmentMetadata(object):
    """
    CompartmentMetadata model.
    """

    #: A constant which can be used with the access_level property of a CompartmentMetadata.
    #: This constant has a value of "accessible"
    ACCESS_LEVEL_ACCESSIBLE = "accessible"

    #: A constant which can be used with the access_level property of a CompartmentMetadata.
    #: This constant has a value of "visible"
    ACCESS_LEVEL_VISIBLE = "visible"

    #: A constant which can be used with the access_level property of a CompartmentMetadata.
    #: This constant has a value of "inaccessible"
    ACCESS_LEVEL_INACCESSIBLE = "inaccessible"

    def __init__(self, **kwargs):
        """
        Initializes a new CompartmentMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CompartmentMetadata.
        :type compartment_id: str

        :param access_level:
            The value to assign to the access_level property of this CompartmentMetadata.
            Allowed values for this property are: "accessible", "visible", "inaccessible"
        :type access_level: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'access_level': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'access_level': 'accessLevel'
        }

        self._compartment_id = None
        self._access_level = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CompartmentMetadata.
        The compartment id.


        :return: The compartment_id of this CompartmentMetadata.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CompartmentMetadata.
        The compartment id.


        :param compartment_id: The compartment_id of this CompartmentMetadata.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def access_level(self):
        """
        **[Required]** Gets the access_level of this CompartmentMetadata.
        The access level.

        Allowed values for this property are: "accessible", "visible", "inaccessible"


        :return: The access_level of this CompartmentMetadata.
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """
        Sets the access_level of this CompartmentMetadata.
        The access level.


        :param access_level: The access_level of this CompartmentMetadata.
        :type: str
        """
        allowed_values = ["accessible", "visible", "inaccessible"]
        if not value_allowed_none_or_none_sentinel(access_level, allowed_values):
            raise ValueError(
                "Invalid value for `access_level`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._access_level = access_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
