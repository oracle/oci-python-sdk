# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TermRelationship(object):
    """
    Full term relationship definition. Business term relationship between two terms in a business glossary.
    """

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a TermRelationship.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new TermRelationship object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TermRelationship.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this TermRelationship.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TermRelationship.
        :type description: str

        :param related_term_key:
            The value to assign to the related_term_key property of this TermRelationship.
        :type related_term_key: str

        :param related_term_display_name:
            The value to assign to the related_term_display_name property of this TermRelationship.
        :type related_term_display_name: str

        :param related_term_description:
            The value to assign to the related_term_description property of this TermRelationship.
        :type related_term_description: str

        :param related_term_path:
            The value to assign to the related_term_path property of this TermRelationship.
        :type related_term_path: str

        :param related_term_glossary_key:
            The value to assign to the related_term_glossary_key property of this TermRelationship.
        :type related_term_glossary_key: str

        :param uri:
            The value to assign to the uri property of this TermRelationship.
        :type uri: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this TermRelationship.
        :type parent_term_key: str

        :param parent_term_display_name:
            The value to assign to the parent_term_display_name property of this TermRelationship.
        :type parent_term_display_name: str

        :param parent_term_description:
            The value to assign to the parent_term_description property of this TermRelationship.
        :type parent_term_description: str

        :param parent_term_path:
            The value to assign to the parent_term_path property of this TermRelationship.
        :type parent_term_path: str

        :param parent_term_glossary_key:
            The value to assign to the parent_term_glossary_key property of this TermRelationship.
        :type parent_term_glossary_key: str

        :param time_created:
            The value to assign to the time_created property of this TermRelationship.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TermRelationship.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'related_term_key': 'str',
            'related_term_display_name': 'str',
            'related_term_description': 'str',
            'related_term_path': 'str',
            'related_term_glossary_key': 'str',
            'uri': 'str',
            'parent_term_key': 'str',
            'parent_term_display_name': 'str',
            'parent_term_description': 'str',
            'parent_term_path': 'str',
            'parent_term_glossary_key': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'related_term_key': 'relatedTermKey',
            'related_term_display_name': 'relatedTermDisplayName',
            'related_term_description': 'relatedTermDescription',
            'related_term_path': 'relatedTermPath',
            'related_term_glossary_key': 'relatedTermGlossaryKey',
            'uri': 'uri',
            'parent_term_key': 'parentTermKey',
            'parent_term_display_name': 'parentTermDisplayName',
            'parent_term_description': 'parentTermDescription',
            'parent_term_path': 'parentTermPath',
            'parent_term_glossary_key': 'parentTermGlossaryKey',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._related_term_key = None
        self._related_term_display_name = None
        self._related_term_description = None
        self._related_term_path = None
        self._related_term_glossary_key = None
        self._uri = None
        self._parent_term_key = None
        self._parent_term_display_name = None
        self._parent_term_description = None
        self._parent_term_path = None
        self._parent_term_glossary_key = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TermRelationship.
        Unique term relationship key that is immutable.


        :return: The key of this TermRelationship.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TermRelationship.
        Unique term relationship key that is immutable.


        :param key: The key of this TermRelationship.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this TermRelationship.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.This is the same as relationshipType for termRelationship


        :return: The display_name of this TermRelationship.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TermRelationship.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.This is the same as relationshipType for termRelationship


        :param display_name: The display_name of this TermRelationship.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TermRelationship.
        Detailed description of the term relationship usually defined at the time of creation.


        :return: The description of this TermRelationship.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TermRelationship.
        Detailed description of the term relationship usually defined at the time of creation.


        :param description: The description of this TermRelationship.
        :type: str
        """
        self._description = description

    @property
    def related_term_key(self):
        """
        Gets the related_term_key of this TermRelationship.
        Unique id of the related term.


        :return: The related_term_key of this TermRelationship.
        :rtype: str
        """
        return self._related_term_key

    @related_term_key.setter
    def related_term_key(self, related_term_key):
        """
        Sets the related_term_key of this TermRelationship.
        Unique id of the related term.


        :param related_term_key: The related_term_key of this TermRelationship.
        :type: str
        """
        self._related_term_key = related_term_key

    @property
    def related_term_display_name(self):
        """
        Gets the related_term_display_name of this TermRelationship.
        Name of the related term.


        :return: The related_term_display_name of this TermRelationship.
        :rtype: str
        """
        return self._related_term_display_name

    @related_term_display_name.setter
    def related_term_display_name(self, related_term_display_name):
        """
        Sets the related_term_display_name of this TermRelationship.
        Name of the related term.


        :param related_term_display_name: The related_term_display_name of this TermRelationship.
        :type: str
        """
        self._related_term_display_name = related_term_display_name

    @property
    def related_term_description(self):
        """
        Gets the related_term_description of this TermRelationship.
        Description of the related term.


        :return: The related_term_description of this TermRelationship.
        :rtype: str
        """
        return self._related_term_description

    @related_term_description.setter
    def related_term_description(self, related_term_description):
        """
        Sets the related_term_description of this TermRelationship.
        Description of the related term.


        :param related_term_description: The related_term_description of this TermRelationship.
        :type: str
        """
        self._related_term_description = related_term_description

    @property
    def related_term_path(self):
        """
        Gets the related_term_path of this TermRelationship.
        Full path of the related term.


        :return: The related_term_path of this TermRelationship.
        :rtype: str
        """
        return self._related_term_path

    @related_term_path.setter
    def related_term_path(self, related_term_path):
        """
        Sets the related_term_path of this TermRelationship.
        Full path of the related term.


        :param related_term_path: The related_term_path of this TermRelationship.
        :type: str
        """
        self._related_term_path = related_term_path

    @property
    def related_term_glossary_key(self):
        """
        Gets the related_term_glossary_key of this TermRelationship.
        Glossary key of the related term.


        :return: The related_term_glossary_key of this TermRelationship.
        :rtype: str
        """
        return self._related_term_glossary_key

    @related_term_glossary_key.setter
    def related_term_glossary_key(self, related_term_glossary_key):
        """
        Sets the related_term_glossary_key of this TermRelationship.
        Glossary key of the related term.


        :param related_term_glossary_key: The related_term_glossary_key of this TermRelationship.
        :type: str
        """
        self._related_term_glossary_key = related_term_glossary_key

    @property
    def uri(self):
        """
        Gets the uri of this TermRelationship.
        URI to the term relationship instance in the API.


        :return: The uri of this TermRelationship.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TermRelationship.
        URI to the term relationship instance in the API.


        :param uri: The uri of this TermRelationship.
        :type: str
        """
        self._uri = uri

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this TermRelationship.
        This relationships parent term key.


        :return: The parent_term_key of this TermRelationship.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this TermRelationship.
        This relationships parent term key.


        :param parent_term_key: The parent_term_key of this TermRelationship.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def parent_term_display_name(self):
        """
        Gets the parent_term_display_name of this TermRelationship.
        Name of the parent term.


        :return: The parent_term_display_name of this TermRelationship.
        :rtype: str
        """
        return self._parent_term_display_name

    @parent_term_display_name.setter
    def parent_term_display_name(self, parent_term_display_name):
        """
        Sets the parent_term_display_name of this TermRelationship.
        Name of the parent term.


        :param parent_term_display_name: The parent_term_display_name of this TermRelationship.
        :type: str
        """
        self._parent_term_display_name = parent_term_display_name

    @property
    def parent_term_description(self):
        """
        Gets the parent_term_description of this TermRelationship.
        Description of the parent term.


        :return: The parent_term_description of this TermRelationship.
        :rtype: str
        """
        return self._parent_term_description

    @parent_term_description.setter
    def parent_term_description(self, parent_term_description):
        """
        Sets the parent_term_description of this TermRelationship.
        Description of the parent term.


        :param parent_term_description: The parent_term_description of this TermRelationship.
        :type: str
        """
        self._parent_term_description = parent_term_description

    @property
    def parent_term_path(self):
        """
        Gets the parent_term_path of this TermRelationship.
        Full path of the parent term.


        :return: The parent_term_path of this TermRelationship.
        :rtype: str
        """
        return self._parent_term_path

    @parent_term_path.setter
    def parent_term_path(self, parent_term_path):
        """
        Sets the parent_term_path of this TermRelationship.
        Full path of the parent term.


        :param parent_term_path: The parent_term_path of this TermRelationship.
        :type: str
        """
        self._parent_term_path = parent_term_path

    @property
    def parent_term_glossary_key(self):
        """
        Gets the parent_term_glossary_key of this TermRelationship.
        Glossary key of the parent term.


        :return: The parent_term_glossary_key of this TermRelationship.
        :rtype: str
        """
        return self._parent_term_glossary_key

    @parent_term_glossary_key.setter
    def parent_term_glossary_key(self, parent_term_glossary_key):
        """
        Sets the parent_term_glossary_key of this TermRelationship.
        Glossary key of the parent term.


        :param parent_term_glossary_key: The parent_term_glossary_key of this TermRelationship.
        :type: str
        """
        self._parent_term_glossary_key = parent_term_glossary_key

    @property
    def time_created(self):
        """
        Gets the time_created of this TermRelationship.
        The date and time the term relationship was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TermRelationship.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TermRelationship.
        The date and time the term relationship was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TermRelationship.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TermRelationship.
        State of the term relationship.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TermRelationship.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TermRelationship.
        State of the term relationship.


        :param lifecycle_state: The lifecycle_state of this TermRelationship.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
