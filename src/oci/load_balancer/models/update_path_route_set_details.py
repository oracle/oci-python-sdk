# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePathRouteSetDetails(object):
    """
    An updated set of path route rules that overwrites the existing set of rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePathRouteSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param path_routes:
            The value to assign to the path_routes property of this UpdatePathRouteSetDetails.
        :type path_routes: list[PathRoute]

        """
        self.swagger_types = {
            'path_routes': 'list[PathRoute]'
        }

        self.attribute_map = {
            'path_routes': 'pathRoutes'
        }

        self._path_routes = None

    @property
    def path_routes(self):
        """
        **[Required]** Gets the path_routes of this UpdatePathRouteSetDetails.
        The set of path route rules.


        :return: The path_routes of this UpdatePathRouteSetDetails.
        :rtype: list[PathRoute]
        """
        return self._path_routes

    @path_routes.setter
    def path_routes(self, path_routes):
        """
        Sets the path_routes of this UpdatePathRouteSetDetails.
        The set of path route rules.


        :param path_routes: The path_routes of this UpdatePathRouteSetDetails.
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
