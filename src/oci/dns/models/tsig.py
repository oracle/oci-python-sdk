# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TSIG(object):
    """
    A `TSIG`__ key.

    __ https://tools.ietf.org/html/rfc2845
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TSIG object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this TSIG.
        :type name: str

        :param secret:
            The value to assign to the secret property of this TSIG.
        :type secret: str

        :param algorithm:
            The value to assign to the algorithm property of this TSIG.
        :type algorithm: str

        """
        self.swagger_types = {
            'name': 'str',
            'secret': 'str',
            'algorithm': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'secret': 'secret',
            'algorithm': 'algorithm'
        }

        self._name = None
        self._secret = None
        self._algorithm = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this TSIG.
        A domain name identifying the key for a given pair of hosts.


        :return: The name of this TSIG.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TSIG.
        A domain name identifying the key for a given pair of hosts.


        :param name: The name of this TSIG.
        :type: str
        """
        self._name = name

    @property
    def secret(self):
        """
        **[Required]** Gets the secret of this TSIG.
        A base64 string encoding the binary shared secret.


        :return: The secret of this TSIG.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this TSIG.
        A base64 string encoding the binary shared secret.


        :param secret: The secret of this TSIG.
        :type: str
        """
        self._secret = secret

    @property
    def algorithm(self):
        """
        **[Required]** Gets the algorithm of this TSIG.
        TSIG Algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute. For a
        full list of TSIG algorithms, see `Secret Key Transaction Authentication for DNS (TSIG) Algorithm Names`__

        __ http://www.iana.org/assignments/tsig-algorithm-names/tsig-algorithm-names.xhtml#tsig-algorithm-names-1


        :return: The algorithm of this TSIG.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this TSIG.
        TSIG Algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute. For a
        full list of TSIG algorithms, see `Secret Key Transaction Authentication for DNS (TSIG) Algorithm Names`__

        __ http://www.iana.org/assignments/tsig-algorithm-names/tsig-algorithm-names.xhtml#tsig-algorithm-names-1


        :param algorithm: The algorithm of this TSIG.
        :type: str
        """
        self._algorithm = algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
