# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaRuntimeId(object):
    """
    The essential properties to identify a Java Runtime.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JavaRuntimeId object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this JavaRuntimeId.
        :type version: str

        :param vendor:
            The value to assign to the vendor property of this JavaRuntimeId.
        :type vendor: str

        :param distribution:
            The value to assign to the distribution property of this JavaRuntimeId.
        :type distribution: str

        :param jre_key:
            The value to assign to the jre_key property of this JavaRuntimeId.
        :type jre_key: str

        """
        self.swagger_types = {
            'version': 'str',
            'vendor': 'str',
            'distribution': 'str',
            'jre_key': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'vendor': 'vendor',
            'distribution': 'distribution',
            'jre_key': 'jreKey'
        }

        self._version = None
        self._vendor = None
        self._distribution = None
        self._jre_key = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this JavaRuntimeId.
        The version of the Java Runtime.


        :return: The version of this JavaRuntimeId.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this JavaRuntimeId.
        The version of the Java Runtime.


        :param version: The version of this JavaRuntimeId.
        :type: str
        """
        self._version = version

    @property
    def vendor(self):
        """
        **[Required]** Gets the vendor of this JavaRuntimeId.
        The vendor of the Java Runtime.


        :return: The vendor of this JavaRuntimeId.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this JavaRuntimeId.
        The vendor of the Java Runtime.


        :param vendor: The vendor of this JavaRuntimeId.
        :type: str
        """
        self._vendor = vendor

    @property
    def distribution(self):
        """
        **[Required]** Gets the distribution of this JavaRuntimeId.
        The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.


        :return: The distribution of this JavaRuntimeId.
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """
        Sets the distribution of this JavaRuntimeId.
        The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.


        :param distribution: The distribution of this JavaRuntimeId.
        :type: str
        """
        self._distribution = distribution

    @property
    def jre_key(self):
        """
        Gets the jre_key of this JavaRuntimeId.
        The unique identifier for a Java Runtime.


        :return: The jre_key of this JavaRuntimeId.
        :rtype: str
        """
        return self._jre_key

    @jre_key.setter
    def jre_key(self, jre_key):
        """
        Sets the jre_key of this JavaRuntimeId.
        The unique identifier for a Java Runtime.


        :param jre_key: The jre_key of this JavaRuntimeId.
        :type: str
        """
        self._jre_key = jre_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
