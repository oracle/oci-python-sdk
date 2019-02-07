# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PolicyConfig(object):
    """
    The configuration details for the WAAS policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PolicyConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this PolicyConfig.
        :type certificate_id: str

        :param is_https_enabled:
            The value to assign to the is_https_enabled property of this PolicyConfig.
        :type is_https_enabled: bool

        :param is_https_forced:
            The value to assign to the is_https_forced property of this PolicyConfig.
        :type is_https_forced: bool

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'is_https_enabled': 'bool',
            'is_https_forced': 'bool'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'is_https_enabled': 'isHttpsEnabled',
            'is_https_forced': 'isHttpsForced'
        }

        self._certificate_id = None
        self._is_https_enabled = None
        self._is_https_forced = None

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this PolicyConfig.
        The OCID of the SSL certificate to use if HTTPS is supported.


        :return: The certificate_id of this PolicyConfig.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this PolicyConfig.
        The OCID of the SSL certificate to use if HTTPS is supported.


        :param certificate_id: The certificate_id of this PolicyConfig.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def is_https_enabled(self):
        """
        Gets the is_https_enabled of this PolicyConfig.
        Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.


        :return: The is_https_enabled of this PolicyConfig.
        :rtype: bool
        """
        return self._is_https_enabled

    @is_https_enabled.setter
    def is_https_enabled(self, is_https_enabled):
        """
        Sets the is_https_enabled of this PolicyConfig.
        Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.


        :param is_https_enabled: The is_https_enabled of this PolicyConfig.
        :type: bool
        """
        self._is_https_enabled = is_https_enabled

    @property
    def is_https_forced(self):
        """
        Gets the is_https_forced of this PolicyConfig.
        Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.


        :return: The is_https_forced of this PolicyConfig.
        :rtype: bool
        """
        return self._is_https_forced

    @is_https_forced.setter
    def is_https_forced(self, is_https_forced):
        """
        Sets the is_https_forced of this PolicyConfig.
        Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.


        :param is_https_forced: The is_https_forced of this PolicyConfig.
        :type: bool
        """
        self._is_https_forced = is_https_forced

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
