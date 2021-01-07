# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param shapes:
            The value to assign to the shapes property of this NodePoolOptions.
        :type shapes: list[str]

        :param images:
            The value to assign to the images property of this NodePoolOptions.
        :type images: list[str]

        :param sources:
            The value to assign to the sources property of this NodePoolOptions.
        :type sources: list[oci.container_engine.models.NodeSourceOption]

        """
        self.swagger_types = {
            'kubernetes_versions': 'list[str]',
            'shapes': 'list[str]',
            'images': 'list[str]',
            'sources': 'list[NodeSourceOption]'
        }

        self.attribute_map = {
            'kubernetes_versions': 'kubernetesVersions',
            'shapes': 'shapes',
            'images': 'images',
            'sources': 'sources'
        }

        self._kubernetes_versions = None
        self._shapes = None
        self._images = None
        self._sources = None

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

    @property
    def images(self):
        """
        Gets the images of this NodePoolOptions.
        Deprecated. See sources.
        When creating a node pool using the `CreateNodePoolDetails` object, only image names contained in this
        property can be passed to the `nodeImageName` property.


        :return: The images of this NodePoolOptions.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this NodePoolOptions.
        Deprecated. See sources.
        When creating a node pool using the `CreateNodePoolDetails` object, only image names contained in this
        property can be passed to the `nodeImageName` property.


        :param images: The images of this NodePoolOptions.
        :type: list[str]
        """
        self._images = images

    @property
    def sources(self):
        """
        Gets the sources of this NodePoolOptions.
        Available source of the node.


        :return: The sources of this NodePoolOptions.
        :rtype: list[oci.container_engine.models.NodeSourceOption]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this NodePoolOptions.
        Available source of the node.


        :param sources: The sources of this NodePoolOptions.
        :type: list[oci.container_engine.models.NodeSourceOption]
        """
        self._sources = sources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
