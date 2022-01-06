# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateHostDumpTransferDetails(object):
    """
    Optional additional properties for dump transfer in source or target host. Default kind is CURL
    """

    #: A constant which can be used with the kind property of a CreateHostDumpTransferDetails.
    #: This constant has a value of "CURL"
    KIND_CURL = "CURL"

    #: A constant which can be used with the kind property of a CreateHostDumpTransferDetails.
    #: This constant has a value of "OCI_CLI"
    KIND_OCI_CLI = "OCI_CLI"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateHostDumpTransferDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_migration.models.CreateOciCliDumpTransferDetails`
        * :class:`~oci.database_migration.models.CreateCurlTransferDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this CreateHostDumpTransferDetails.
            Allowed values for this property are: "CURL", "OCI_CLI"
        :type kind: str

        """
        self.swagger_types = {
            'kind': 'str'
        }

        self.attribute_map = {
            'kind': 'kind'
        }

        self._kind = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'OCI_CLI':
            return 'CreateOciCliDumpTransferDetails'

        if type == 'CURL':
            return 'CreateCurlTransferDetails'
        else:
            return 'CreateHostDumpTransferDetails'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this CreateHostDumpTransferDetails.
        Type of dump transfer to use during migration in source or target host. Default kind is CURL

        Allowed values for this property are: "CURL", "OCI_CLI"


        :return: The kind of this CreateHostDumpTransferDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this CreateHostDumpTransferDetails.
        Type of dump transfer to use during migration in source or target host. Default kind is CURL


        :param kind: The kind of this CreateHostDumpTransferDetails.
        :type: str
        """
        allowed_values = ["CURL", "OCI_CLI"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            raise ValueError(
                "Invalid value for `kind`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._kind = kind

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
