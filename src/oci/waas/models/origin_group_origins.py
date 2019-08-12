# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OriginGroupOrigins(object):
    """
    OriginGroupOrigins model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OriginGroupOrigins object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param origin:
            The value to assign to the origin property of this OriginGroupOrigins.
        :type origin: str

        :param weight:
            The value to assign to the weight property of this OriginGroupOrigins.
        :type weight: int

        """
        self.swagger_types = {
            'origin': 'str',
            'weight': 'int'
        }

        self.attribute_map = {
            'origin': 'origin',
            'weight': 'weight'
        }

        self._origin = None
        self._weight = None

    @property
    def origin(self):
        """
        Gets the origin of this OriginGroupOrigins.
        The reference string to the origin server.


        :return: The origin of this OriginGroupOrigins.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this OriginGroupOrigins.
        The reference string to the origin server.


        :param origin: The origin of this OriginGroupOrigins.
        :type: str
        """
        self._origin = origin

    @property
    def weight(self):
        """
        Gets the weight of this OriginGroupOrigins.
        The weight of the origin used in load balancing. The higher the weight, the larger the proportion of client requests the server receives.


        :return: The weight of this OriginGroupOrigins.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this OriginGroupOrigins.
        The weight of the origin used in load balancing. The higher the weight, the larger the proportion of client requests the server receives.


        :param weight: The weight of this OriginGroupOrigins.
        :type: int
        """
        self._weight = weight

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
