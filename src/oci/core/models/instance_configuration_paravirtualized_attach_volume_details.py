# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .instance_configuration_attach_volume_details import InstanceConfigurationAttachVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationParavirtualizedAttachVolumeDetails(InstanceConfigurationAttachVolumeDetails):
    """
    InstanceConfigurationParavirtualizedAttachVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationParavirtualizedAttachVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationParavirtualizedAttachVolumeDetails.type` attribute
        of this class is ``paravirtualized`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type display_name: str

        :param is_read_only:
            The value to assign to the is_read_only property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type is_read_only: bool

        :param type:
            The value to assign to the type property of this InstanceConfigurationParavirtualizedAttachVolumeDetails.
        :type type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_read_only': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_read_only': 'isReadOnly',
            'type': 'type'
        }

        self._display_name = None
        self._is_read_only = None
        self._type = None
        self._type = 'paravirtualized'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
