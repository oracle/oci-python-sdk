# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePathRouteSetDetails(object):
    """
    A named set of path route rules to add to the load balancer.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePathRouteSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreatePathRouteSetDetails.
        :type name: str

        :param path_routes:
            The value to assign to the path_routes property of this CreatePathRouteSetDetails.
        :type path_routes: list[oci.load_balancer.models.PathRoute]

        """
        self.swagger_types = {
            'name': 'str',
            'path_routes': 'list[PathRoute]'
        }

        self.attribute_map = {
            'name': 'name',
            'path_routes': 'pathRoutes'
        }

        self._name = None
        self._path_routes = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreatePathRouteSetDetails.
        The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_path_route_set`


        :return: The name of this CreatePathRouteSetDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePathRouteSetDetails.
        The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_path_route_set`


        :param name: The name of this CreatePathRouteSetDetails.
        :type: str
        """
        self._name = name

    @property
    def path_routes(self):
        """
        **[Required]** Gets the path_routes of this CreatePathRouteSetDetails.
        The set of path route rules.


        :return: The path_routes of this CreatePathRouteSetDetails.
        :rtype: list[oci.load_balancer.models.PathRoute]
        """
        return self._path_routes

    @path_routes.setter
    def path_routes(self, path_routes):
        """
        Sets the path_routes of this CreatePathRouteSetDetails.
        The set of path route rules.


        :param path_routes: The path_routes of this CreatePathRouteSetDetails.
        :type: list[oci.load_balancer.models.PathRoute]
        """
        self._path_routes = path_routes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
