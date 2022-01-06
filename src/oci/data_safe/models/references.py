# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class References(object):
    """
    References to the sections of STIG, CIS, and/or GDPR relevant to the current finding.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new References object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stig:
            The value to assign to the stig property of this References.
        :type stig: str

        :param cis:
            The value to assign to the cis property of this References.
        :type cis: str

        :param gdpr:
            The value to assign to the gdpr property of this References.
        :type gdpr: str

        """
        self.swagger_types = {
            'stig': 'str',
            'cis': 'str',
            'gdpr': 'str'
        }

        self.attribute_map = {
            'stig': 'stig',
            'cis': 'cis',
            'gdpr': 'gdpr'
        }

        self._stig = None
        self._cis = None
        self._gdpr = None

    @property
    def stig(self):
        """
        Gets the stig of this References.
        Relevant section from STIG.


        :return: The stig of this References.
        :rtype: str
        """
        return self._stig

    @stig.setter
    def stig(self, stig):
        """
        Sets the stig of this References.
        Relevant section from STIG.


        :param stig: The stig of this References.
        :type: str
        """
        self._stig = stig

    @property
    def cis(self):
        """
        Gets the cis of this References.
        Relevant section from CIS.


        :return: The cis of this References.
        :rtype: str
        """
        return self._cis

    @cis.setter
    def cis(self, cis):
        """
        Sets the cis of this References.
        Relevant section from CIS.


        :param cis: The cis of this References.
        :type: str
        """
        self._cis = cis

    @property
    def gdpr(self):
        """
        Gets the gdpr of this References.
        Relevant section from GDPR.


        :return: The gdpr of this References.
        :rtype: str
        """
        return self._gdpr

    @gdpr.setter
    def gdpr(self, gdpr):
        """
        Sets the gdpr of this References.
        Relevant section from GDPR.


        :param gdpr: The gdpr of this References.
        :type: str
        """
        self._gdpr = gdpr

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
