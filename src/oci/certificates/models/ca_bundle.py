# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaBundle(object):
    """
    The contents of the CA bundle (root and intermediate certificates), properties of the CA bundle, and user-provided contextual metadata for the CA bundle.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CaBundle object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CaBundle.
        :type id: str

        :param name:
            The value to assign to the name property of this CaBundle.
        :type name: str

        :param ca_bundle_pem:
            The value to assign to the ca_bundle_pem property of this CaBundle.
        :type ca_bundle_pem: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'ca_bundle_pem': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'ca_bundle_pem': 'caBundlePem'
        }

        self._id = None
        self._name = None
        self._ca_bundle_pem = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CaBundle.
        The OCID of the CA bundle.


        :return: The id of this CaBundle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CaBundle.
        The OCID of the CA bundle.


        :param id: The id of this CaBundle.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CaBundle.
        A user-friendly name for the CA bundle. Names are unique within a compartment. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CaBundle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CaBundle.
        A user-friendly name for the CA bundle. Names are unique within a compartment. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CaBundle.
        :type: str
        """
        self._name = name

    @property
    def ca_bundle_pem(self):
        """
        **[Required]** Gets the ca_bundle_pem of this CaBundle.
        Certificates (in PEM format) in the CA bundle. Can be of arbitrary length.


        :return: The ca_bundle_pem of this CaBundle.
        :rtype: str
        """
        return self._ca_bundle_pem

    @ca_bundle_pem.setter
    def ca_bundle_pem(self, ca_bundle_pem):
        """
        Sets the ca_bundle_pem of this CaBundle.
        Certificates (in PEM format) in the CA bundle. Can be of arbitrary length.


        :param ca_bundle_pem: The ca_bundle_pem of this CaBundle.
        :type: str
        """
        self._ca_bundle_pem = ca_bundle_pem

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
