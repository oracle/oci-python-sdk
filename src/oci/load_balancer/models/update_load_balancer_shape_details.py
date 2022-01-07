# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLoadBalancerShapeDetails(object):
    """
    UpdateLoadBalancerShapeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLoadBalancerShapeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape_name:
            The value to assign to the shape_name property of this UpdateLoadBalancerShapeDetails.
        :type shape_name: str

        :param shape_details:
            The value to assign to the shape_details property of this UpdateLoadBalancerShapeDetails.
        :type shape_details: oci.load_balancer.models.ShapeDetails

        """
        self.swagger_types = {
            'shape_name': 'str',
            'shape_details': 'ShapeDetails'
        }

        self.attribute_map = {
            'shape_name': 'shapeName',
            'shape_details': 'shapeDetails'
        }

        self._shape_name = None
        self._shape_details = None

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this UpdateLoadBalancerShapeDetails.
        The new shape name for the load balancer.

        Allowed values are :
          *  10Mbps
          *  100Mbps
          *  400Mbps
          *  8000Mbps
          *  Flexible

          Example: `Flexible`


        :return: The shape_name of this UpdateLoadBalancerShapeDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this UpdateLoadBalancerShapeDetails.
        The new shape name for the load balancer.

        Allowed values are :
          *  10Mbps
          *  100Mbps
          *  400Mbps
          *  8000Mbps
          *  Flexible

          Example: `Flexible`


        :param shape_name: The shape_name of this UpdateLoadBalancerShapeDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def shape_details(self):
        """
        Gets the shape_details of this UpdateLoadBalancerShapeDetails.
        The configuration details to update load balancer to a different profile.


        :return: The shape_details of this UpdateLoadBalancerShapeDetails.
        :rtype: oci.load_balancer.models.ShapeDetails
        """
        return self._shape_details

    @shape_details.setter
    def shape_details(self, shape_details):
        """
        Sets the shape_details of this UpdateLoadBalancerShapeDetails.
        The configuration details to update load balancer to a different profile.


        :param shape_details: The shape_details of this UpdateLoadBalancerShapeDetails.
        :type: oci.load_balancer.models.ShapeDetails
        """
        self._shape_details = shape_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
