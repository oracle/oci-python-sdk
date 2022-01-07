# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateDetails(object):
    """
    Information about a new certificate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateCertificateDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCertificateDetails.
        :type compartment_id: str

        :param private_key:
            The value to assign to the private_key property of this CreateCertificateDetails.
        :type private_key: str

        :param certificate:
            The value to assign to the certificate property of this CreateCertificateDetails.
        :type certificate: str

        :param intermediate_certificates:
            The value to assign to the intermediate_certificates property of this CreateCertificateDetails.
        :type intermediate_certificates: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCertificateDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCertificateDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'private_key': 'str',
            'certificate': 'str',
            'intermediate_certificates': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'private_key': 'privateKey',
            'certificate': 'certificate',
            'intermediate_certificates': 'intermediateCertificates',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._private_key = None
        self._certificate = None
        self._intermediate_certificates = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCertificateDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this CreateCertificateDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCertificateDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this CreateCertificateDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCertificateDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateCertificateDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCertificateDetails.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateCertificateDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def private_key(self):
        """
        **[Required]** Gets the private_key of this CreateCertificateDetails.
        The private key associated with the certificate in pem format.


        :return: The private_key of this CreateCertificateDetails.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """
        Sets the private_key of this CreateCertificateDetails.
        The private key associated with the certificate in pem format.


        :param private_key: The private_key of this CreateCertificateDetails.
        :type: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """
        **[Required]** Gets the certificate of this CreateCertificateDetails.
        The data of the leaf certificate in pem format.


        :return: The certificate of this CreateCertificateDetails.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this CreateCertificateDetails.
        The data of the leaf certificate in pem format.


        :param certificate: The certificate of this CreateCertificateDetails.
        :type: str
        """
        self._certificate = certificate

    @property
    def intermediate_certificates(self):
        """
        Gets the intermediate_certificates of this CreateCertificateDetails.
        The intermediate certificate data associated with the certificate in pem format.


        :return: The intermediate_certificates of this CreateCertificateDetails.
        :rtype: str
        """
        return self._intermediate_certificates

    @intermediate_certificates.setter
    def intermediate_certificates(self, intermediate_certificates):
        """
        Sets the intermediate_certificates of this CreateCertificateDetails.
        The intermediate certificate data associated with the certificate in pem format.


        :param intermediate_certificates: The intermediate_certificates of this CreateCertificateDetails.
        :type: str
        """
        self._intermediate_certificates = intermediate_certificates

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

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
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

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
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

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
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

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
