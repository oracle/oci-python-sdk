# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRefreshActivityDetails(object):
    """
    The information about current refresh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRefreshActivityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_fusion_environment_id:
            The value to assign to the source_fusion_environment_id property of this CreateRefreshActivityDetails.
        :type source_fusion_environment_id: str

        """
        self.swagger_types = {
            'source_fusion_environment_id': 'str'
        }

        self.attribute_map = {
            'source_fusion_environment_id': 'sourceFusionEnvironmentId'
        }

        self._source_fusion_environment_id = None

    @property
    def source_fusion_environment_id(self):
        """
        **[Required]** Gets the source_fusion_environment_id of this CreateRefreshActivityDetails.
        The `OCID`__ of the source environment

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_fusion_environment_id of this CreateRefreshActivityDetails.
        :rtype: str
        """
        return self._source_fusion_environment_id

    @source_fusion_environment_id.setter
    def source_fusion_environment_id(self, source_fusion_environment_id):
        """
        Sets the source_fusion_environment_id of this CreateRefreshActivityDetails.
        The `OCID`__ of the source environment

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_fusion_environment_id: The source_fusion_environment_id of this CreateRefreshActivityDetails.
        :type: str
        """
        self._source_fusion_environment_id = source_fusion_environment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
