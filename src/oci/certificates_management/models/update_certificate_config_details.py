# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCertificateConfigDetails(object):
    """
    The details of the contents of the certificate and certificate metadata.
    """

    #: A constant which can be used with the config_type property of a UpdateCertificateConfigDetails.
    #: This constant has a value of "ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_ISSUED_BY_INTERNAL_CA = "ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the config_type property of a UpdateCertificateConfigDetails.
    #: This constant has a value of "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA"
    CONFIG_TYPE_MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA = "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA"

    #: A constant which can be used with the config_type property of a UpdateCertificateConfigDetails.
    #: This constant has a value of "IMPORTED"
    CONFIG_TYPE_IMPORTED = "IMPORTED"

    #: A constant which can be used with the stage property of a UpdateCertificateConfigDetails.
    #: This constant has a value of "CURRENT"
    STAGE_CURRENT = "CURRENT"

    #: A constant which can be used with the stage property of a UpdateCertificateConfigDetails.
    #: This constant has a value of "PENDING"
    STAGE_PENDING = "PENDING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCertificateConfigDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.certificates_management.models.UpdateCertificateByImportingConfigDetails`
        * :class:`~oci.certificates_management.models.UpdateCertificateIssuedByInternalCaConfigDetails`
        * :class:`~oci.certificates_management.models.UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this UpdateCertificateConfigDetails.
            Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this UpdateCertificateConfigDetails.
        :type version_name: str

        :param stage:
            The value to assign to the stage property of this UpdateCertificateConfigDetails.
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

        if type == 'IMPORTED':
            return 'UpdateCertificateByImportingConfigDetails'

        if type == 'ISSUED_BY_INTERNAL_CA':
            return 'UpdateCertificateIssuedByInternalCaConfigDetails'

        if type == 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA':
            return 'UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails'
        else:
            return 'UpdateCertificateConfigDetails'

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this UpdateCertificateConfigDetails.
        The origin of the certificate.

        Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"


        :return: The config_type of this UpdateCertificateConfigDetails.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this UpdateCertificateConfigDetails.
        The origin of the certificate.


        :param config_type: The config_type of this UpdateCertificateConfigDetails.
        :type: str
        """
        allowed_values = ["ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            raise ValueError(
                "Invalid value for `config_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._config_type = config_type

    @property
    def version_name(self):
        """
        Gets the version_name of this UpdateCertificateConfigDetails.
        A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.


        :return: The version_name of this UpdateCertificateConfigDetails.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this UpdateCertificateConfigDetails.
        A name for the certificate version. When the value is not null, a name is unique across versions of a given certificate.


        :param version_name: The version_name of this UpdateCertificateConfigDetails.
        :type: str
        """
        self._version_name = version_name

    @property
    def stage(self):
        """
        Gets the stage of this UpdateCertificateConfigDetails.
        The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version
        that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
        you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.

        Allowed values for this property are: "CURRENT", "PENDING"


        :return: The stage of this UpdateCertificateConfigDetails.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """
        Sets the stage of this UpdateCertificateConfigDetails.
        The rotation state of the certificate. The default is `CURRENT`, meaning that the certificate is currently in use. A certificate version
        that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
        you might update a certificate and mark its rotation state as `PENDING` if you haven't yet updated the certificate on the target system.


        :param stage: The stage of this UpdateCertificateConfigDetails.
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
