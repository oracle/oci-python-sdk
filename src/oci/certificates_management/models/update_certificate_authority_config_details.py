# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCertificateAuthorityConfigDetails(object):
    """
    The configuration details for updating a certificate authority (CA).
    """

    #: A constant which can be used with the config_type property of a UpdateCertificateAuthorityConfigDetails.
    #: This constant has a value of "ROOT_CA_GENERATED_INTERNALLY"
    CONFIG_TYPE_ROOT_CA_GENERATED_INTERNALLY = "ROOT_CA_GENERATED_INTERNALLY"

    #: A constant which can be used with the config_type property of a UpdateCertificateAuthorityConfigDetails.
    #: This constant has a value of "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA = "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the stage property of a UpdateCertificateAuthorityConfigDetails.
    #: This constant has a value of "CURRENT"
    STAGE_CURRENT = "CURRENT"

    #: A constant which can be used with the stage property of a UpdateCertificateAuthorityConfigDetails.
    #: This constant has a value of "PENDING"
    STAGE_PENDING = "PENDING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCertificateAuthorityConfigDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.certificates_management.models.UpdateSubordinateCaIssuedByInternalCaConfigDetails`
        * :class:`~oci.certificates_management.models.UpdateRootCaByGeneratingInternallyConfigDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this UpdateCertificateAuthorityConfigDetails.
            Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this UpdateCertificateAuthorityConfigDetails.
        :type version_name: str

        :param stage:
            The value to assign to the stage property of this UpdateCertificateAuthorityConfigDetails.
            Allowed values for this property are: "CURRENT", "PENDING"
        :type stage: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'stage': 'str'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'stage': 'stage'
        }

        self._config_type = None
        self._version_name = None
        self._stage = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configType']

        if type == 'SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA':
            return 'UpdateSubordinateCaIssuedByInternalCaConfigDetails'

        if type == 'ROOT_CA_GENERATED_INTERNALLY':
            return 'UpdateRootCaByGeneratingInternallyConfigDetails'
        else:
            return 'UpdateCertificateAuthorityConfigDetails'

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this UpdateCertificateAuthorityConfigDetails.
        The origin of the CA.

        Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"


        :return: The config_type of this UpdateCertificateAuthorityConfigDetails.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this UpdateCertificateAuthorityConfigDetails.
        The origin of the CA.


        :param config_type: The config_type of this UpdateCertificateAuthorityConfigDetails.
        :type: str
        """
        allowed_values = ["ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            raise ValueError(
                "Invalid value for `config_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._config_type = config_type

    @property
    def version_name(self):
        """
        Gets the version_name of this UpdateCertificateAuthorityConfigDetails.
        The name of the CA version. When the value is not null, a name is unique across versions of a given CA.


        :return: The version_name of this UpdateCertificateAuthorityConfigDetails.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this UpdateCertificateAuthorityConfigDetails.
        The name of the CA version. When the value is not null, a name is unique across versions of a given CA.


        :param version_name: The version_name of this UpdateCertificateAuthorityConfigDetails.
        :type: str
        """
        self._version_name = version_name

    @property
    def stage(self):
        """
        Gets the stage of this UpdateCertificateAuthorityConfigDetails.
        The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version
        that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example,
        you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.

        Allowed values for this property are: "CURRENT", "PENDING"


        :return: The stage of this UpdateCertificateAuthorityConfigDetails.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """
        Sets the stage of this UpdateCertificateAuthorityConfigDetails.
        The rotation state of the CA. The default is `PENDING`, meaning that the CA is staged and available for use. A CA version
        that you mark as `CURRENT` is currently in use, but you don't yet want to rotate it into current, active use. For example,
        you might create or update a CA and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.


        :param stage: The stage of this UpdateCertificateAuthorityConfigDetails.
        :type: str
        """
        allowed_values = ["CURRENT", "PENDING"]
        if not value_allowed_none_or_none_sentinel(stage, allowed_values):
            raise ValueError(
                "Invalid value for `stage`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._stage = stage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
