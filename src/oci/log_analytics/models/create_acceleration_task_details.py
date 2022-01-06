# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_scheduled_task_details import CreateScheduledTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAccelerationTaskDetails(CreateScheduledTaskDetails):
    """
    Details for creating a scheduled task to accelerate a saved search.
    The client must specify the savedSearchId, and the service will supply other details.
    The resulting scheduled task will have TaskType ACCELERATION.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAccelerationTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.CreateAccelerationTaskDetails.kind` attribute
        of this class is ``ACCELERATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this CreateAccelerationTaskDetails.
            Allowed values for this property are: "ACCELERATION", "STANDARD"
        :type kind: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAccelerationTaskDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAccelerationTaskDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAccelerationTaskDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAccelerationTaskDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param saved_search_id:
            The value to assign to the saved_search_id property of this CreateAccelerationTaskDetails.
        :type saved_search_id: str

        """
        self.swagger_types = {
            'kind': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'saved_search_id': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'saved_search_id': 'savedSearchId'
        }

        self._kind = None
        self._compartment_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._saved_search_id = None
        self._kind = 'ACCELERATION'

    @property
    def saved_search_id(self):
        """
        **[Required]** Gets the saved_search_id of this CreateAccelerationTaskDetails.
        The ManagementSavedSearch id [OCID] to be accelerated.


        :return: The saved_search_id of this CreateAccelerationTaskDetails.
        :rtype: str
        """
        return self._saved_search_id

    @saved_search_id.setter
    def saved_search_id(self, saved_search_id):
        """
        Sets the saved_search_id of this CreateAccelerationTaskDetails.
        The ManagementSavedSearch id [OCID] to be accelerated.


        :param saved_search_id: The saved_search_id of this CreateAccelerationTaskDetails.
        :type: str
        """
        self._saved_search_id = saved_search_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
