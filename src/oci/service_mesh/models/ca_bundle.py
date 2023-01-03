# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaBundle(object):
    """
    Resource representing the CA bundle.
    """

    #: A constant which can be used with the type property of a CaBundle.
    #: This constant has a value of "OCI_CERTIFICATES"
    TYPE_OCI_CERTIFICATES = "OCI_CERTIFICATES"

    #: A constant which can be used with the type property of a CaBundle.
    #: This constant has a value of "LOCAL_FILE"
    TYPE_LOCAL_FILE = "LOCAL_FILE"

    def __init__(self, **kwargs):
        """
        Initializes a new CaBundle object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.LocalFileCaBundle`
        * :class:`~oci.service_mesh.models.OciCaBundle`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CaBundle.
            Allowed values for this property are: "OCI_CERTIFICATES", "LOCAL_FILE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'LOCAL_FILE':
            return 'LocalFileCaBundle'

        if type == 'OCI_CERTIFICATES':
            return 'OciCaBundle'
        else:
            return 'CaBundle'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CaBundle.
        Type of certificate.

        Allowed values for this property are: "OCI_CERTIFICATES", "LOCAL_FILE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this CaBundle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CaBundle.
        Type of certificate.


        :param type: The type of this CaBundle.
        :type: str
        """
        allowed_values = ["OCI_CERTIFICATES", "LOCAL_FILE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
