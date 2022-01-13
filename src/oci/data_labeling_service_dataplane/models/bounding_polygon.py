# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BoundingPolygon(object):
    """
    A polygon used to describe the location of an object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BoundingPolygon object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param normalized_vertices:
            The value to assign to the normalized_vertices property of this BoundingPolygon.
        :type normalized_vertices: list[oci.data_labeling_service_dataplane.models.NormalizedVertex]

        """
        self.swagger_types = {
            'normalized_vertices': 'list[NormalizedVertex]'
        }

        self.attribute_map = {
            'normalized_vertices': 'normalizedVertices'
        }

        self._normalized_vertices = None

    @property
    def normalized_vertices(self):
        """
        **[Required]** Gets the normalized_vertices of this BoundingPolygon.
        The normalized vertices that make up the polygon.  They are in the order of the segments they connect.


        :return: The normalized_vertices of this BoundingPolygon.
        :rtype: list[oci.data_labeling_service_dataplane.models.NormalizedVertex]
        """
        return self._normalized_vertices

    @normalized_vertices.setter
    def normalized_vertices(self, normalized_vertices):
        """
        Sets the normalized_vertices of this BoundingPolygon.
        The normalized vertices that make up the polygon.  They are in the order of the segments they connect.


        :param normalized_vertices: The normalized_vertices of this BoundingPolygon.
        :type: list[oci.data_labeling_service_dataplane.models.NormalizedVertex]
        """
        self._normalized_vertices = normalized_vertices

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
