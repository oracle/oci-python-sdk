# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Term(object):
    """
    Full term definition. A defined business term in a business glossary. As well as a term definition, simple format
    rules for attributes mapping to the term (for example, the expected data type and length restrictions) may be
    stated at the term level. Nesting of terms to support a hierarchy is supported by default.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Term object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Term.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Term.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Term.
        :type description: str

        :param glossary_key:
            The value to assign to the glossary_key property of this Term.
        :type glossary_key: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this Term.
        :type parent_term_key: str

        :param is_allowed_to_have_child_terms:
            The value to assign to the is_allowed_to_have_child_terms property of this Term.
        :type is_allowed_to_have_child_terms: bool

        :param path:
            The value to assign to the path property of this Term.
        :type path: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Term.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Term.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Term.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Term.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Term.
        :type updated_by_id: str

        :param owner:
            The value to assign to the owner property of this Term.
        :type owner: str

        :param workflow_status:
            The value to assign to the workflow_status property of this Term.
        :type workflow_status: str

        :param uri:
            The value to assign to the uri property of this Term.
        :type uri: str

        :param associated_object_count:
            The value to assign to the associated_object_count property of this Term.
        :type associated_object_count: int

        :param associated_objects:
            The value to assign to the associated_objects property of this Term.
        :type associated_objects: list[TermAssociatedObject]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'glossary_key': 'str',
            'parent_term_key': 'str',
            'is_allowed_to_have_child_terms': 'bool',
            'path': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'owner': 'str',
            'workflow_status': 'str',
            'uri': 'str',
            'associated_object_count': 'int',
            'associated_objects': 'list[TermAssociatedObject]'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'glossary_key': 'glossaryKey',
            'parent_term_key': 'parentTermKey',
            'is_allowed_to_have_child_terms': 'isAllowedToHaveChildTerms',
            'path': 'path',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'owner': 'owner',
            'workflow_status': 'workflowStatus',
            'uri': 'uri',
            'associated_object_count': 'associatedObjectCount',
            'associated_objects': 'associatedObjects'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._glossary_key = None
        self._parent_term_key = None
        self._is_allowed_to_have_child_terms = None
        self._path = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._owner = None
        self._workflow_status = None
        self._uri = None
        self._associated_object_count = None
        self._associated_objects = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Term.
        Unique term key that is immutable.


        :return: The key of this Term.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Term.
        Unique term key that is immutable.


        :param key: The key of this Term.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Term.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Term.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Term.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Term.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Term.
        Detailed description of the term.


        :return: The description of this Term.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Term.
        Detailed description of the term.


        :param description: The description of this Term.
        :type: str
        """
        self._description = description

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this Term.
        Unique id of the parent glossary.


        :return: The glossary_key of this Term.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this Term.
        Unique id of the parent glossary.


        :param glossary_key: The glossary_key of this Term.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this Term.
        This terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this Term.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this Term.
        This terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this Term.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def is_allowed_to_have_child_terms(self):
        """
        Gets the is_allowed_to_have_child_terms of this Term.
        Indicates whether a term may contain child terms.


        :return: The is_allowed_to_have_child_terms of this Term.
        :rtype: bool
        """
        return self._is_allowed_to_have_child_terms

    @is_allowed_to_have_child_terms.setter
    def is_allowed_to_have_child_terms(self, is_allowed_to_have_child_terms):
        """
        Sets the is_allowed_to_have_child_terms of this Term.
        Indicates whether a term may contain child terms.


        :param is_allowed_to_have_child_terms: The is_allowed_to_have_child_terms of this Term.
        :type: bool
        """
        self._is_allowed_to_have_child_terms = is_allowed_to_have_child_terms

    @property
    def path(self):
        """
        Gets the path of this Term.
        Absolute path of the term.


        :return: The path of this Term.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Term.
        Absolute path of the term.


        :param path: The path of this Term.
        :type: str
        """
        self._path = path

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Term.
        The current state of the term.


        :return: The lifecycle_state of this Term.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Term.
        The current state of the term.


        :param lifecycle_state: The lifecycle_state of this Term.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Term.
        The date and time the term was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Term.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Term.
        The date and time the term was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Term.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Term.
        The last time that any change was made to the term. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Term.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Term.
        The last time that any change was made to the term. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Term.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Term.
        OCID of the user who created the term.


        :return: The created_by_id of this Term.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Term.
        OCID of the user who created the term.


        :param created_by_id: The created_by_id of this Term.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Term.
        OCID of the user who modified the term.


        :return: The updated_by_id of this Term.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Term.
        OCID of the user who modified the term.


        :param updated_by_id: The updated_by_id of this Term.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def owner(self):
        """
        Gets the owner of this Term.
        OCID of the user who is the owner of this business terminology.


        :return: The owner of this Term.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Term.
        OCID of the user who is the owner of this business terminology.


        :param owner: The owner of this Term.
        :type: str
        """
        self._owner = owner

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this Term.
        Status of the approval process workflow for this business term in the glossary.


        :return: The workflow_status of this Term.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this Term.
        Status of the approval process workflow for this business term in the glossary.


        :param workflow_status: The workflow_status of this Term.
        :type: str
        """
        self._workflow_status = workflow_status

    @property
    def uri(self):
        """
        Gets the uri of this Term.
        URI to the term instance in the API.


        :return: The uri of this Term.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Term.
        URI to the term instance in the API.


        :param uri: The uri of this Term.
        :type: str
        """
        self._uri = uri

    @property
    def associated_object_count(self):
        """
        Gets the associated_object_count of this Term.
        The number of objects tagged with this term


        :return: The associated_object_count of this Term.
        :rtype: int
        """
        return self._associated_object_count

    @associated_object_count.setter
    def associated_object_count(self, associated_object_count):
        """
        Sets the associated_object_count of this Term.
        The number of objects tagged with this term


        :param associated_object_count: The associated_object_count of this Term.
        :type: int
        """
        self._associated_object_count = associated_object_count

    @property
    def associated_objects(self):
        """
        Gets the associated_objects of this Term.
        Array of objects associated to a term.


        :return: The associated_objects of this Term.
        :rtype: list[TermAssociatedObject]
        """
        return self._associated_objects

    @associated_objects.setter
    def associated_objects(self, associated_objects):
        """
        Sets the associated_objects of this Term.
        Array of objects associated to a term.


        :param associated_objects: The associated_objects of this Term.
        :type: list[TermAssociatedObject]
        """
        self._associated_objects = associated_objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
