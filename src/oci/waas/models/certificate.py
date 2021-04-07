# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Certificate(object):
    """
    The details of the SSL certificate.
    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Certificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Certificate.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Certificate.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Certificate.
        :type display_name: str

        :param issued_by:
            The value to assign to the issued_by property of this Certificate.
        :type issued_by: str

        :param subject_name:
            The value to assign to the subject_name property of this Certificate.
        :type subject_name: oci.waas.models.CertificateSubjectName

        :param issuer_name:
            The value to assign to the issuer_name property of this Certificate.
        :type issuer_name: oci.waas.models.CertificateIssuerName

        :param serial_number:
            The value to assign to the serial_number property of this Certificate.
        :type serial_number: str

        :param version:
            The value to assign to the version property of this Certificate.
        :type version: int

        :param signature_algorithm:
            The value to assign to the signature_algorithm property of this Certificate.
        :type signature_algorithm: str

        :param time_not_valid_before:
            The value to assign to the time_not_valid_before property of this Certificate.
        :type time_not_valid_before: datetime

        :param time_not_valid_after:
            The value to assign to the time_not_valid_after property of this Certificate.
        :type time_not_valid_after: datetime

        :param public_key_info:
            The value to assign to the public_key_info property of this Certificate.
        :type public_key_info: oci.waas.models.CertificatePublicKeyInfo

        :param extensions:
            The value to assign to the extensions property of this Certificate.
        :type extensions: list[oci.waas.models.CertificateExtensions]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Certificate.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Certificate.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Certificate.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Certificate.
        :type time_created: datetime

        :param is_trust_verification_disabled:
            The value to assign to the is_trust_verification_disabled property of this Certificate.
        :type is_trust_verification_disabled: bool

        :param certificate_data:
            The value to assign to the certificate_data property of this Certificate.
        :type certificate_data: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'issued_by': 'str',
            'subject_name': 'CertificateSubjectName',
            'issuer_name': 'CertificateIssuerName',
            'serial_number': 'str',
            'version': 'int',
            'signature_algorithm': 'str',
            'time_not_valid_before': 'datetime',
            'time_not_valid_after': 'datetime',
            'public_key_info': 'CertificatePublicKeyInfo',
            'extensions': 'list[CertificateExtensions]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'is_trust_verification_disabled': 'bool',
            'certificate_data': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'issued_by': 'issuedBy',
            'subject_name': 'subjectName',
            'issuer_name': 'issuerName',
            'serial_number': 'serialNumber',
            'version': 'version',
            'signature_algorithm': 'signatureAlgorithm',
            'time_not_valid_before': 'timeNotValidBefore',
            'time_not_valid_after': 'timeNotValidAfter',
            'public_key_info': 'publicKeyInfo',
            'extensions': 'extensions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'is_trust_verification_disabled': 'isTrustVerificationDisabled',
            'certificate_data': 'certificateData'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._issued_by = None
        self._subject_name = None
        self._issuer_name = None
        self._serial_number = None
        self._version = None
        self._signature_algorithm = None
        self._time_not_valid_before = None
        self._time_not_valid_after = None
        self._public_key_info = None
        self._extensions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None
        self._time_created = None
        self._is_trust_verification_disabled = None
        self._certificate_data = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Certificate.
        The `OCID`__ of the certificate.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Certificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Certificate.
        The `OCID`__ of the certificate.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Certificate.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Certificate.
        The `OCID`__ of the certificate's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Certificate.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Certificate.
        The `OCID`__ of the certificate's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Certificate.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Certificate.
        The user-friendly name of the certificate.


        :return: The display_name of this Certificate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Certificate.
        The user-friendly name of the certificate.


        :param display_name: The display_name of this Certificate.
        :type: str
        """
        self._display_name = display_name

    @property
    def issued_by(self):
        """
        Gets the issued_by of this Certificate.

        :return: The issued_by of this Certificate.
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """
        Sets the issued_by of this Certificate.

        :param issued_by: The issued_by of this Certificate.
        :type: str
        """
        self._issued_by = issued_by

    @property
    def subject_name(self):
        """
        Gets the subject_name of this Certificate.

        :return: The subject_name of this Certificate.
        :rtype: oci.waas.models.CertificateSubjectName
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """
        Sets the subject_name of this Certificate.

        :param subject_name: The subject_name of this Certificate.
        :type: oci.waas.models.CertificateSubjectName
        """
        self._subject_name = subject_name

    @property
    def issuer_name(self):
        """
        Gets the issuer_name of this Certificate.

        :return: The issuer_name of this Certificate.
        :rtype: oci.waas.models.CertificateIssuerName
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """
        Sets the issuer_name of this Certificate.

        :param issuer_name: The issuer_name of this Certificate.
        :type: oci.waas.models.CertificateIssuerName
        """
        self._issuer_name = issuer_name

    @property
    def serial_number(self):
        """
        **[Required]** Gets the serial_number of this Certificate.
        A unique, positive integer assigned by the Certificate Authority (CA). The issuer name and serial number identify a unique certificate.


        :return: The serial_number of this Certificate.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this Certificate.
        A unique, positive integer assigned by the Certificate Authority (CA). The issuer name and serial number identify a unique certificate.


        :param serial_number: The serial_number of this Certificate.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def version(self):
        """
        **[Required]** Gets the version of this Certificate.
        The version of the encoded certificate.


        :return: The version of this Certificate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Certificate.
        The version of the encoded certificate.


        :param version: The version of this Certificate.
        :type: int
        """
        self._version = version

    @property
    def signature_algorithm(self):
        """
        **[Required]** Gets the signature_algorithm of this Certificate.
        The identifier for the cryptographic algorithm used by the Certificate Authority (CA) to sign this certificate.


        :return: The signature_algorithm of this Certificate.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """
        Sets the signature_algorithm of this Certificate.
        The identifier for the cryptographic algorithm used by the Certificate Authority (CA) to sign this certificate.


        :param signature_algorithm: The signature_algorithm of this Certificate.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def time_not_valid_before(self):
        """
        **[Required]** Gets the time_not_valid_before of this Certificate.
        The date and time the certificate will become valid, expressed in RFC 3339 timestamp format.


        :return: The time_not_valid_before of this Certificate.
        :rtype: datetime
        """
        return self._time_not_valid_before

    @time_not_valid_before.setter
    def time_not_valid_before(self, time_not_valid_before):
        """
        Sets the time_not_valid_before of this Certificate.
        The date and time the certificate will become valid, expressed in RFC 3339 timestamp format.


        :param time_not_valid_before: The time_not_valid_before of this Certificate.
        :type: datetime
        """
        self._time_not_valid_before = time_not_valid_before

    @property
    def time_not_valid_after(self):
        """
        **[Required]** Gets the time_not_valid_after of this Certificate.
        The date and time the certificate will expire, expressed in RFC 3339 timestamp format.


        :return: The time_not_valid_after of this Certificate.
        :rtype: datetime
        """
        return self._time_not_valid_after

    @time_not_valid_after.setter
    def time_not_valid_after(self, time_not_valid_after):
        """
        Sets the time_not_valid_after of this Certificate.
        The date and time the certificate will expire, expressed in RFC 3339 timestamp format.


        :param time_not_valid_after: The time_not_valid_after of this Certificate.
        :type: datetime
        """
        self._time_not_valid_after = time_not_valid_after

    @property
    def public_key_info(self):
        """
        Gets the public_key_info of this Certificate.

        :return: The public_key_info of this Certificate.
        :rtype: oci.waas.models.CertificatePublicKeyInfo
        """
        return self._public_key_info

    @public_key_info.setter
    def public_key_info(self, public_key_info):
        """
        Sets the public_key_info of this Certificate.

        :param public_key_info: The public_key_info of this Certificate.
        :type: oci.waas.models.CertificatePublicKeyInfo
        """
        self._public_key_info = public_key_info

    @property
    def extensions(self):
        """
        Gets the extensions of this Certificate.
        Additional attributes associated with users or public keys for managing relationships between Certificate Authorities.


        :return: The extensions of this Certificate.
        :rtype: list[oci.waas.models.CertificateExtensions]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """
        Sets the extensions of this Certificate.
        Additional attributes associated with users or public keys for managing relationships between Certificate Authorities.


        :param extensions: The extensions of this Certificate.
        :type: list[oci.waas.models.CertificateExtensions]
        """
        self._extensions = extensions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Certificate.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Certificate.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Certificate.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Certificate.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Certificate.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Certificate.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Certificate.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Certificate.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Certificate.
        The current lifecycle state of the SSL certificate.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Certificate.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Certificate.
        The current lifecycle state of the SSL certificate.


        :param lifecycle_state: The lifecycle_state of this Certificate.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Certificate.
        The date and time the certificate was created, expressed in RFC 3339 timestamp format.


        :return: The time_created of this Certificate.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Certificate.
        The date and time the certificate was created, expressed in RFC 3339 timestamp format.


        :param time_created: The time_created of this Certificate.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def is_trust_verification_disabled(self):
        """
        Gets the is_trust_verification_disabled of this Certificate.
        This indicates whether trust verification was disabled during the creation of SSL certificate.
        If `true` SSL certificate trust verification was disabled and this SSL certificate is most likely self-signed.


        :return: The is_trust_verification_disabled of this Certificate.
        :rtype: bool
        """
        return self._is_trust_verification_disabled

    @is_trust_verification_disabled.setter
    def is_trust_verification_disabled(self, is_trust_verification_disabled):
        """
        Sets the is_trust_verification_disabled of this Certificate.
        This indicates whether trust verification was disabled during the creation of SSL certificate.
        If `true` SSL certificate trust verification was disabled and this SSL certificate is most likely self-signed.


        :param is_trust_verification_disabled: The is_trust_verification_disabled of this Certificate.
        :type: bool
        """
        self._is_trust_verification_disabled = is_trust_verification_disabled

    @property
    def certificate_data(self):
        """
        Gets the certificate_data of this Certificate.
        The data of the SSL certificate.


        :return: The certificate_data of this Certificate.
        :rtype: str
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """
        Sets the certificate_data of this Certificate.
        The data of the SSL certificate.


        :param certificate_data: The certificate_data of this Certificate.
        :type: str
        """
        self._certificate_data = certificate_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
