# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolOptions(object):
    """
    Options for creating or updating node pools.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kubernetes_versions:
            The value to assign to the kubernetes_versions property of this NodePoolOptions.
        :type kubernetes_versions: list[str]

        :param images:
            The value to assign to the images property of this NodePoolOptions.
        :type images: list[str]

        :param shapes:
            The value to assign to the shapes property of this NodePoolOptions.
        :type shapes: list[str]

        """
        self.swagger_types = {
            'kubernetes_versions': 'list[str]',
            'images': 'list[str]',
            'shapes': 'list[str]'
        }

        self.attribute_map = {
            'kubernetes_versions': 'kubernetesVersions',
            'images': 'images',
            'shapes': 'shapes'
        }

        self._kubernetes_versions = None
        self._images = None
        self._shapes = None

    @property
    def kubernetes_versions(self):
        """
        Gets the kubernetes_versions of this NodePoolOptions.
        Available Kubernetes versions.


        :return: The kubernetes_versions of this NodePoolOptions.
        :rtype: list[str]
        """
        return self._kubernetes_versions

    @kubernetes_versions.setter
    def kubernetes_versions(self, kubernetes_versions):
        """
        Sets the kubernetes_versions of this NodePoolOptions.
        Available Kubernetes versions.


        :param kubernetes_versions: The kubernetes_versions of this NodePoolOptions.
        :type: list[str]
        """
        self._kubernetes_versions = kubernetes_versions

    @property
    def images(self):
        """
        Gets the images of this NodePoolOptions.
        Available Kubernetes versions.


        :return: The images of this NodePoolOptions.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this NodePoolOptions.
        Available Kubernetes versions.


        :param images: The images of this NodePoolOptions.
        :type: list[str]
        """
        self._images = images

    @property
    def shapes(self):
        """
        Gets the shapes of this NodePoolOptions.
        Available shapes for nodes.


        :return: The shapes of this NodePoolOptions.
        :rtype: list[str]
        """
        return self._shapes

    @shapes.setter
    def shapes(self, shapes):
        """
        Sets the shapes of this NodePoolOptions.
        Available shapes for nodes.


        :param shapes: The shapes of this NodePoolOptions.
        :type: list[str]
        """
        self._shapes = shapes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
