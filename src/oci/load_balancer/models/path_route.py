# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathRoute(object):
    """
    A \"path route rule\" to evaluate an incoming URI path, and then route a matching request to the specified backend set.

    Path route rules apply only to HTTP and HTTPS requests. They have no effect on TCP requests.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PathRoute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backend_set_name:
            The value to assign to the backend_set_name property of this PathRoute.
        :type backend_set_name: str

        :param path:
            The value to assign to the path property of this PathRoute.
        :type path: str

        :param path_match_type:
            The value to assign to the path_match_type property of this PathRoute.
        :type path_match_type: PathMatchType

        """
        self.swagger_types = {
            'backend_set_name': 'str',
            'path': 'str',
            'path_match_type': 'PathMatchType'
        }

        self.attribute_map = {
            'backend_set_name': 'backendSetName',
            'path': 'path',
            'path_match_type': 'pathMatchType'
        }

        self._backend_set_name = None
        self._path = None
        self._path_match_type = None

    @property
    def backend_set_name(self):
        """
        **[Required]** Gets the backend_set_name of this PathRoute.
        The name of the target backend set for requests where the incoming URI matches the specified path.

        Example: `example_backend_set`


        :return: The backend_set_name of this PathRoute.
        :rtype: str
        """
        return self._backend_set_name

    @backend_set_name.setter
    def backend_set_name(self, backend_set_name):
        """
        Sets the backend_set_name of this PathRoute.
        The name of the target backend set for requests where the incoming URI matches the specified path.

        Example: `example_backend_set`


        :param backend_set_name: The backend_set_name of this PathRoute.
        :type: str
        """
        self._backend_set_name = backend_set_name

    @property
    def path(self):
        """
        **[Required]** Gets the path of this PathRoute.
        The path string to match against the incoming URI path.

        *  Path strings are case-insensitive.

        *  Asterisk (*) wildcards are not supported.

        *  Regular expressions are not supported.

        Example: `/example/video/123`


        :return: The path of this PathRoute.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this PathRoute.
        The path string to match against the incoming URI path.

        *  Path strings are case-insensitive.

        *  Asterisk (*) wildcards are not supported.

        *  Regular expressions are not supported.

        Example: `/example/video/123`


        :param path: The path of this PathRoute.
        :type: str
        """
        self._path = path

    @property
    def path_match_type(self):
        """
        **[Required]** Gets the path_match_type of this PathRoute.
        The type of matching to apply to incoming URIs.


        :return: The path_match_type of this PathRoute.
        :rtype: PathMatchType
        """
        return self._path_match_type

    @path_match_type.setter
    def path_match_type(self, path_match_type):
        """
        Sets the path_match_type of this PathRoute.
        The type of matching to apply to incoming URIs.


        :param path_match_type: The path_match_type of this PathRoute.
        :type: PathMatchType
        """
        self._path_match_type = path_match_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
