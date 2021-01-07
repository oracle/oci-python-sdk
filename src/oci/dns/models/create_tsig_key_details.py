# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTsigKeyDetails(object):
    """
    The body for defining a TSIG key.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTsigKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this CreateTsigKeyDetails.
        :type algorithm: str

        :param name:
            The value to assign to the name property of this CreateTsigKeyDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTsigKeyDetails.
        :type compartment_id: str

        :param secret:
            The value to assign to the secret property of this CreateTsigKeyDetails.
        :type secret: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTsigKeyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTsigKeyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'algorithm': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'secret': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'secret': 'secret',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._algorithm = None
        self._name = None
        self._compartment_id = None
        self._secret = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def algorithm(self):
        """
        **[Required]** Gets the algorithm of this CreateTsigKeyDetails.
        TSIG key algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute.
        Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
        hmac-sha512. For more information on these algorithms, see `RFC 4635`__.

        __ https://tools.ietf.org/html/rfc4635#section-2


        :return: The algorithm of this CreateTsigKeyDetails.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this CreateTsigKeyDetails.
        TSIG key algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute.
        Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
        hmac-sha512. For more information on these algorithms, see `RFC 4635`__.

        __ https://tools.ietf.org/html/rfc4635#section-2


        :param algorithm: The algorithm of this CreateTsigKeyDetails.
        :type: str
        """
        self._algorithm = algorithm

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateTsigKeyDetails.
        A globally unique domain name identifying the key for a given pair of hosts.


        :return: The name of this CreateTsigKeyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTsigKeyDetails.
        A globally unique domain name identifying the key for a given pair of hosts.


        :param name: The name of this CreateTsigKeyDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTsigKeyDetails.
        The OCID of the compartment containing the TSIG key.


        :return: The compartment_id of this CreateTsigKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTsigKeyDetails.
        The OCID of the compartment containing the TSIG key.


        :param compartment_id: The compartment_id of this CreateTsigKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def secret(self):
        """
        **[Required]** Gets the secret of this CreateTsigKeyDetails.
        A base64 string encoding the binary shared secret.


        :return: The secret of this CreateTsigKeyDetails.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this CreateTsigKeyDetails.
        A base64 string encoding the binary shared secret.


        :param secret: The secret of this CreateTsigKeyDetails.
        :type: str
        """
        self._secret = secret

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTsigKeyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateTsigKeyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTsigKeyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateTsigKeyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTsigKeyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateTsigKeyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTsigKeyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateTsigKeyDetails.
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
