# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateDetails(object):
    """
    The data used to create a new SSL certificate.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCertificateDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCertificateDetails.
        :type display_name: str

        :param certificate_data:
            The value to assign to the certificate_data property of this CreateCertificateDetails.
        :type certificate_data: str

        :param private_key_data:
            The value to assign to the private_key_data property of this CreateCertificateDetails.
        :type private_key_data: str

        :param is_trust_verification_disabled:
            The value to assign to the is_trust_verification_disabled property of this CreateCertificateDetails.
        :type is_trust_verification_disabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCertificateDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCertificateDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'certificate_data': 'str',
            'private_key_data': 'str',
            'is_trust_verification_disabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'certificate_data': 'certificateData',
            'private_key_data': 'privateKeyData',
            'is_trust_verification_disabled': 'isTrustVerificationDisabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._certificate_data = None
        self._private_key_data = None
        self._is_trust_verification_disabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCertificateDetails.
        The `OCID`__ of the compartment in which to create the SSL certificate.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCertificateDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCertificateDetails.
        The `OCID`__ of the compartment in which to create the SSL certificate.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCertificateDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCertificateDetails.
        A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.


        :return: The display_name of this CreateCertificateDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCertificateDetails.
        A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.


        :param display_name: The display_name of this CreateCertificateDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def certificate_data(self):
        """
        **[Required]** Gets the certificate_data of this CreateCertificateDetails.
        The data of the SSL certificate.


        **Note:** Many SSL certificate providers require an intermediate certificate chain to ensure a trusted status.
        If your SSL certificate requires an intermediate certificate chain, please append the intermediate certificate
        key in the `certificateData` field after the leaf certificate issued by the SSL certificate provider. If you
        are unsure if your certificate requires an intermediate certificate chain, see your certificate
        provider's documentation.


        The example below shows an intermediate certificate appended to a leaf certificate.


        :return: The certificate_data of this CreateCertificateDetails.
        :rtype: str
        """
        return self._certificate_data

    @certificate_data.setter
    def certificate_data(self, certificate_data):
        """
        Sets the certificate_data of this CreateCertificateDetails.
        The data of the SSL certificate.


        **Note:** Many SSL certificate providers require an intermediate certificate chain to ensure a trusted status.
        If your SSL certificate requires an intermediate certificate chain, please append the intermediate certificate
        key in the `certificateData` field after the leaf certificate issued by the SSL certificate provider. If you
        are unsure if your certificate requires an intermediate certificate chain, see your certificate
        provider's documentation.


        The example below shows an intermediate certificate appended to a leaf certificate.


        :param certificate_data: The certificate_data of this CreateCertificateDetails.
        :type: str
        """
        self._certificate_data = certificate_data

    @property
    def private_key_data(self):
        """
        **[Required]** Gets the private_key_data of this CreateCertificateDetails.
        The private key of the SSL certificate.


        :return: The private_key_data of this CreateCertificateDetails.
        :rtype: str
        """
        return self._private_key_data

    @private_key_data.setter
    def private_key_data(self, private_key_data):
        """
        Sets the private_key_data of this CreateCertificateDetails.
        The private key of the SSL certificate.


        :param private_key_data: The private_key_data of this CreateCertificateDetails.
        :type: str
        """
        self._private_key_data = private_key_data

    @property
    def is_trust_verification_disabled(self):
        """
        Gets the is_trust_verification_disabled of this CreateCertificateDetails.
        Set to `true` if the SSL certificate is self-signed.


        :return: The is_trust_verification_disabled of this CreateCertificateDetails.
        :rtype: bool
        """
        return self._is_trust_verification_disabled

    @is_trust_verification_disabled.setter
    def is_trust_verification_disabled(self, is_trust_verification_disabled):
        """
        Sets the is_trust_verification_disabled of this CreateCertificateDetails.
        Set to `true` if the SSL certificate is self-signed.


        :param is_trust_verification_disabled: The is_trust_verification_disabled of this CreateCertificateDetails.
        :type: bool
        """
        self._is_trust_verification_disabled = is_trust_verification_disabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCertificateDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCertificateDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCertificateDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCertificateDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
