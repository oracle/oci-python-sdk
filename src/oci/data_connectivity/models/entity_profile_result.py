# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityProfileResult(object):
    """
    The metadata details of a profiling entity result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityProfileResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_count:
            The value to assign to the attribute_count property of this EntityProfileResult.
        :type attribute_count: int

        :param sampled_row_count:
            The value to assign to the sampled_row_count property of this EntityProfileResult.
        :type sampled_row_count: int

        :param estimated_row_count:
            The value to assign to the estimated_row_count property of this EntityProfileResult.
        :type estimated_row_count: int

        """
        self.swagger_types = {
            'attribute_count': 'int',
            'sampled_row_count': 'int',
            'estimated_row_count': 'int'
        }

        self.attribute_map = {
            'attribute_count': 'attributeCount',
            'sampled_row_count': 'sampledRowCount',
            'estimated_row_count': 'estimatedRowCount'
        }

        self._attribute_count = None
        self._sampled_row_count = None
        self._estimated_row_count = None

    @property
    def attribute_count(self):
        """
        Gets the attribute_count of this EntityProfileResult.
        Number of columns in the DataFrame (arrow buffer) sent from Java layer. This value is not impacted by the list of attributes to profile as being passed via configuration.


        :return: The attribute_count of this EntityProfileResult.
        :rtype: int
        """
        return self._attribute_count

    @attribute_count.setter
    def attribute_count(self, attribute_count):
        """
        Sets the attribute_count of this EntityProfileResult.
        Number of columns in the DataFrame (arrow buffer) sent from Java layer. This value is not impacted by the list of attributes to profile as being passed via configuration.


        :param attribute_count: The attribute_count of this EntityProfileResult.
        :type: int
        """
        self._attribute_count = attribute_count

    @property
    def sampled_row_count(self):
        """
        Gets the sampled_row_count of this EntityProfileResult.
        Number of rows that are sampled.


        :return: The sampled_row_count of this EntityProfileResult.
        :rtype: int
        """
        return self._sampled_row_count

    @sampled_row_count.setter
    def sampled_row_count(self, sampled_row_count):
        """
        Sets the sampled_row_count of this EntityProfileResult.
        Number of rows that are sampled.


        :param sampled_row_count: The sampled_row_count of this EntityProfileResult.
        :type: int
        """
        self._sampled_row_count = sampled_row_count

    @property
    def estimated_row_count(self):
        """
        Gets the estimated_row_count of this EntityProfileResult.
        The estimated row count in the source.


        :return: The estimated_row_count of this EntityProfileResult.
        :rtype: int
        """
        return self._estimated_row_count

    @estimated_row_count.setter
    def estimated_row_count(self, estimated_row_count):
        """
        Sets the estimated_row_count of this EntityProfileResult.
        The estimated row count in the source.


        :param estimated_row_count: The estimated_row_count of this EntityProfileResult.
        :type: int
        """
        self._estimated_row_count = estimated_row_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
