# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Annotation(object):
    """
    An annotation represents a user- or machine-generated annotation for a given record.  The details of the annotation are captured in the RecordAnnotationDetails.
    """

    #: A constant which can be used with the lifecycle_state property of a Annotation.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Annotation.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Annotation.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Annotation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Annotation.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this Annotation.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Annotation.
        :type time_updated: datetime

        :param created_by:
            The value to assign to the created_by property of this Annotation.
        :type created_by: str

        :param updated_by:
            The value to assign to the updated_by property of this Annotation.
        :type updated_by: str

        :param record_id:
            The value to assign to the record_id property of this Annotation.
        :type record_id: str

        :param entities:
            The value to assign to the entities property of this Annotation.
        :type entities: list[oci.data_labeling_service_dataplane.models.Entity]

        :param compartment_id:
            The value to assign to the compartment_id property of this Annotation.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Annotation.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Annotation.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Annotation.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by': 'str',
            'updated_by': 'str',
            'record_id': 'str',
            'entities': 'list[Entity]',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by': 'createdBy',
            'updated_by': 'updatedBy',
            'record_id': 'recordId',
            'entities': 'entities',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._time_created = None
        self._time_updated = None
        self._created_by = None
        self._updated_by = None
        self._record_id = None
        self._entities = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Annotation.
        The OCID of the annotation.


        :return: The id of this Annotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Annotation.
        The OCID of the annotation.


        :param id: The id of this Annotation.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Annotation.
        The date and time the annotation was created, in the timestamp format defined by RFC3339.


        :return: The time_created of this Annotation.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Annotation.
        The date and time the annotation was created, in the timestamp format defined by RFC3339.


        :param time_created: The time_created of this Annotation.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Annotation.
        The date and time the resource was updated, in the timestamp format defined by RFC3339.


        :return: The time_updated of this Annotation.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Annotation.
        The date and time the resource was updated, in the timestamp format defined by RFC3339.


        :param time_updated: The time_updated of this Annotation.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this Annotation.
        The OCID of the principal which created the annotation.


        :return: The created_by of this Annotation.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Annotation.
        The OCID of the principal which created the annotation.


        :param created_by: The created_by of this Annotation.
        :type: str
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        """
        **[Required]** Gets the updated_by of this Annotation.
        The OCID of the principal which updated the annotation.


        :return: The updated_by of this Annotation.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this Annotation.
        The OCID of the principal which updated the annotation.


        :param updated_by: The updated_by of this Annotation.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def record_id(self):
        """
        **[Required]** Gets the record_id of this Annotation.
        The OCID of the record annotated.


        :return: The record_id of this Annotation.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """
        Sets the record_id of this Annotation.
        The OCID of the record annotated.


        :param record_id: The record_id of this Annotation.
        :type: str
        """
        self._record_id = record_id

    @property
    def entities(self):
        """
        **[Required]** Gets the entities of this Annotation.
        The entity types are validated against the dataset to ensure consistency.


        :return: The entities of this Annotation.
        :rtype: list[oci.data_labeling_service_dataplane.models.Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this Annotation.
        The entity types are validated against the dataset to ensure consistency.


        :param entities: The entities of this Annotation.
        :type: list[oci.data_labeling_service_dataplane.models.Entity]
        """
        self._entities = entities

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Annotation.
        The OCID of the compartment for the annotation. This is tied to the dataset. It is not changeable on the record itself.


        :return: The compartment_id of this Annotation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Annotation.
        The OCID of the compartment for the annotation. This is tied to the dataset. It is not changeable on the record itself.


        :param compartment_id: The compartment_id of this Annotation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Annotation.
        The lifecycle state of an annotation.
        ACTIVE - The annotation is active to be used for labeling.
        INACTIVE - The annotation has been marked as inactive and should not be used for labeling.
        DELETED - Tha annotation been deleted and no longer available for labeling.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Annotation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Annotation.
        The lifecycle state of an annotation.
        ACTIVE - The annotation is active to be used for labeling.
        INACTIVE - The annotation has been marked as inactive and should not be used for labeling.
        DELETED - Tha annotation been deleted and no longer available for labeling.


        :param lifecycle_state: The lifecycle_state of this Annotation.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Annotation.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Annotation.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Annotation.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Annotation.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Annotation.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Annotation.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Annotation.
        The defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Annotation.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
