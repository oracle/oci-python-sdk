# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .autotune_policy import AutotunePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachedVolumeAutotunePolicy(AutotunePolicy):
    """
    Volume's performace will be tuned to the lower cost settings once detached.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachedVolumeAutotunePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DetachedVolumeAutotunePolicy.autotune_type` attribute
        of this class is ``DETACHED_VOLUME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autotune_type:
            The value to assign to the autotune_type property of this DetachedVolumeAutotunePolicy.
            Allowed values for this property are: "DETACHED_VOLUME", "PERFORMANCE_BASED"
        :type autotune_type: str

        """
        self.swagger_types = {
            'autotune_type': 'str'
        }

        self.attribute_map = {
            'autotune_type': 'autotuneType'
        }

        self._autotune_type = None
        self._autotune_type = 'DETACHED_VOLUME'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
