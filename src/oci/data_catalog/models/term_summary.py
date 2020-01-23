# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TermSummary(object):
    """
    Summary of a term. A defined business term in a business glossary. As well as a term definition, simple format
    rules for attributes mapping to the term (for example, the expected data type and length restrictions) may be
    stated at the term level.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TermSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TermSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this TermSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TermSummary.
        :type description: str

        :param glossary_key:
            The value to assign to the glossary_key property of this TermSummary.
        :type glossary_key: str

        :param uri:
            The value to assign to the uri property of this TermSummary.
        :type uri: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this TermSummary.
        :type parent_term_key: str

        :param is_allowed_to_have_child_terms:
            The value to assign to the is_allowed_to_have_child_terms property of this TermSummary.
        :type is_allowed_to_have_child_terms: bool

        :param path:
            The value to assign to the path property of this TermSummary.
        :type path: str

        :param time_created:
            The value to assign to the time_created property of this TermSummary.
        :type time_created: datetime

        :param workflow_status:
            The value to assign to the workflow_status property of this TermSummary.
        :type workflow_status: str

        :param associated_object_count:
            The value to assign to the associated_object_count property of this TermSummary.
        :type associated_object_count: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TermSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'glossary_key': 'str',
            'uri': 'str',
            'parent_term_key': 'str',
            'is_allowed_to_have_child_terms': 'bool',
            'path': 'str',
            'time_created': 'datetime',
            'workflow_status': 'str',
            'associated_object_count': 'int',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'glossary_key': 'glossaryKey',
            'uri': 'uri',
            'parent_term_key': 'parentTermKey',
            'is_allowed_to_have_child_terms': 'isAllowedToHaveChildTerms',
            'path': 'path',
            'time_created': 'timeCreated',
            'workflow_status': 'workflowStatus',
            'associated_object_count': 'associatedObjectCount',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._glossary_key = None
        self._uri = None
        self._parent_term_key = None
        self._is_allowed_to_have_child_terms = None
        self._path = None
        self._time_created = None
        self._workflow_status = None
        self._associated_object_count = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TermSummary.
        Unique term key that is immutable.


        :return: The key of this TermSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TermSummary.
        Unique term key that is immutable.


        :param key: The key of this TermSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this TermSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this TermSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TermSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this TermSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TermSummary.
        Detailed description of the term.


        :return: The description of this TermSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TermSummary.
        Detailed description of the term.


        :param description: The description of this TermSummary.
        :type: str
        """
        self._description = description

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this TermSummary.
        Unique id of the parent glossary.


        :return: The glossary_key of this TermSummary.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this TermSummary.
        Unique id of the parent glossary.


        :param glossary_key: The glossary_key of this TermSummary.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def uri(self):
        """
        Gets the uri of this TermSummary.
        URI to the term instance in the API.


        :return: The uri of this TermSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TermSummary.
        URI to the term instance in the API.


        :param uri: The uri of this TermSummary.
        :type: str
        """
        self._uri = uri

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this TermSummary.
        This terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this TermSummary.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this TermSummary.
        This terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this TermSummary.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def is_allowed_to_have_child_terms(self):
        """
        Gets the is_allowed_to_have_child_terms of this TermSummary.
        Indicates whether a term may contain child terms.


        :return: The is_allowed_to_have_child_terms of this TermSummary.
        :rtype: bool
        """
        return self._is_allowed_to_have_child_terms

    @is_allowed_to_have_child_terms.setter
    def is_allowed_to_have_child_terms(self, is_allowed_to_have_child_terms):
        """
        Sets the is_allowed_to_have_child_terms of this TermSummary.
        Indicates whether a term may contain child terms.


        :param is_allowed_to_have_child_terms: The is_allowed_to_have_child_terms of this TermSummary.
        :type: bool
        """
        self._is_allowed_to_have_child_terms = is_allowed_to_have_child_terms

    @property
    def path(self):
        """
        Gets the path of this TermSummary.
        Absolute path of the term.


        :return: The path of this TermSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this TermSummary.
        Absolute path of the term.


        :param path: The path of this TermSummary.
        :type: str
        """
        self._path = path

    @property
    def time_created(self):
        """
        Gets the time_created of this TermSummary.
        The date and time the term was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TermSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TermSummary.
        The date and time the term was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TermSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this TermSummary.
        Status of the approval process workflow for this business term in the glossary.


        :return: The workflow_status of this TermSummary.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this TermSummary.
        Status of the approval process workflow for this business term in the glossary.


        :param workflow_status: The workflow_status of this TermSummary.
        :type: str
        """
        self._workflow_status = workflow_status

    @property
    def associated_object_count(self):
        """
        Gets the associated_object_count of this TermSummary.
        The number of objects tagged with this term.


        :return: The associated_object_count of this TermSummary.
        :rtype: int
        """
        return self._associated_object_count

    @associated_object_count.setter
    def associated_object_count(self, associated_object_count):
        """
        Sets the associated_object_count of this TermSummary.
        The number of objects tagged with this term.


        :param associated_object_count: The associated_object_count of this TermSummary.
        :type: int
        """
        self._associated_object_count = associated_object_count

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TermSummary.
        State of the term.


        :return: The lifecycle_state of this TermSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TermSummary.
        State of the term.


        :param lifecycle_state: The lifecycle_state of this TermSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
