# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachInstancePoolInstanceDetails(object):
    """
    An instance that is to be attached to an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachInstancePoolInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this AttachInstancePoolInstanceDetails.
        :type instance_id: str

        """
        self.swagger_types = {
            'instance_id': 'str'
        }

        self.attribute_map = {
            'instance_id': 'instanceId'
        }

        self._instance_id = None

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this AttachInstancePoolInstanceDetails.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this AttachInstancePoolInstanceDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachInstancePoolInstanceDetails.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this AttachInstancePoolInstanceDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
