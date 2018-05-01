# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathRouteSet(object):
    """
    A named set of path route rules. For more information, see
    `Managing Request Routing`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Tasks/managingrequest.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PathRouteSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PathRouteSet.
        :type name: str

        :param path_routes:
            The value to assign to the path_routes property of this PathRouteSet.
        :type path_routes: list[PathRoute]

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
        **[Required]** Gets the name of this PathRouteSet.
        The unique name for this set of path route rules. Avoid entering confidential information.

        Example: `example_path_route_set`


        :return: The name of this PathRouteSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PathRouteSet.
        The unique name for this set of path route rules. Avoid entering confidential information.

        Example: `example_path_route_set`


        :param name: The name of this PathRouteSet.
        :type: str
        """
        self._name = name

    @property
    def path_routes(self):
        """
        **[Required]** Gets the path_routes of this PathRouteSet.
        The set of path route rules.


        :return: The path_routes of this PathRouteSet.
        :rtype: list[PathRoute]
        """
        return self._path_routes

    @path_routes.setter
    def path_routes(self, path_routes):
        """
        Sets the path_routes of this PathRouteSet.
        The set of path route rules.


        :param path_routes: The path_routes of this PathRouteSet.
        :type: list[PathRoute]
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
