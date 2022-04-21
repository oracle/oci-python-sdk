# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MeshMutualTransportLayerSecurity(object):
    """
    Sets a minimum level of mTLS authentication for all virtual services within the mesh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MeshMutualTransportLayerSecurity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param minimum:
            The value to assign to the minimum property of this MeshMutualTransportLayerSecurity.
        :type minimum: str

        """
        self.swagger_types = {
            'minimum': 'str'
        }

        self.attribute_map = {
            'minimum': 'minimum'
        }

        self._minimum = None

    @property
    def minimum(self):
        """
        **[Required]** Gets the minimum of this MeshMutualTransportLayerSecurity.
        DISABLED: No minimum virtual services within this mesh can use any mTLS authentication mode.
        PERMISSIVE: Virtual services within this mesh can use either PERMISSIVE or STRICT modes.
        STRICT: All virtual services within this mesh must use STRICT mode.


        :return: The minimum of this MeshMutualTransportLayerSecurity.
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this MeshMutualTransportLayerSecurity.
        DISABLED: No minimum virtual services within this mesh can use any mTLS authentication mode.
        PERMISSIVE: Virtual services within this mesh can use either PERMISSIVE or STRICT modes.
        STRICT: All virtual services within this mesh must use STRICT mode.


        :param minimum: The minimum of this MeshMutualTransportLayerSecurity.
        :type: str
        """
        self._minimum = minimum

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
