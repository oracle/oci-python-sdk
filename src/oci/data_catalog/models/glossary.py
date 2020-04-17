# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Glossary(object):
    """
    Full glossary details. A glossary of business terms, such as 'Customer', 'Account', 'Contact' , 'Address',
    or 'Product', with definitions, used to provide common meaning across disparate data assets. Business glossaries
    may be hierarchical where some terms may contain child terms to allow them to be used as 'taxonomies'.
    By linking data assets, data entities, and attributes to glossaries and glossary terms, the glossary can act as a
    way of organizing data catalog objects in a hierarchy to make a large number of objects more navigable and easier to
    consume. Objects in the data aatalog, such as data assets or data entities, may be linked to any level in the
    glossary, so that the glossary can be used to browse the available data according to the business model of the
    organization.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Glossary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Glossary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Glossary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Glossary.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this Glossary.
        :type catalog_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Glossary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Glossary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Glossary.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Glossary.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Glossary.
        :type updated_by_id: str

        :param owner:
            The value to assign to the owner property of this Glossary.
        :type owner: str

        :param workflow_status:
            The value to assign to the workflow_status property of this Glossary.
        :type workflow_status: str

        :param uri:
            The value to assign to the uri property of this Glossary.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'owner': 'str',
            'workflow_status': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'catalog_id': 'catalogId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'owner': 'owner',
            'workflow_status': 'workflowStatus',
            'uri': 'uri'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._catalog_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._owner = None
        self._workflow_status = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Glossary.
        Unique glossary key that is immutable.


        :return: The key of this Glossary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Glossary.
        Unique glossary key that is immutable.


        :param key: The key of this Glossary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Glossary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Glossary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Glossary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Glossary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Glossary.
        Detailed description of the glossary.


        :return: The description of this Glossary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Glossary.
        Detailed description of the glossary.


        :param description: The description of this Glossary.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this Glossary.
        The data catalog's OCID.


        :return: The catalog_id of this Glossary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this Glossary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this Glossary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Glossary.
        The current state of the glossary.


        :return: The lifecycle_state of this Glossary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Glossary.
        The current state of the glossary.


        :param lifecycle_state: The lifecycle_state of this Glossary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Glossary.
        The date and time the glossary was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Glossary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Glossary.
        The date and time the glossary was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Glossary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Glossary.
        The last time that any change was made to the glossary. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Glossary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Glossary.
        The last time that any change was made to the glossary. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Glossary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Glossary.
        OCID of the user who created this metadata element.


        :return: The created_by_id of this Glossary.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Glossary.
        OCID of the user who created this metadata element.


        :param created_by_id: The created_by_id of this Glossary.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Glossary.
        OCID of the user who updated this metadata element.


        :return: The updated_by_id of this Glossary.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Glossary.
        OCID of the user who updated this metadata element.


        :param updated_by_id: The updated_by_id of this Glossary.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def owner(self):
        """
        Gets the owner of this Glossary.
        OCID of the user who is the owner of the glossary.


        :return: The owner of this Glossary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Glossary.
        OCID of the user who is the owner of the glossary.


        :param owner: The owner of this Glossary.
        :type: str
        """
        self._owner = owner

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this Glossary.
        Status of the approval process workflow for this business glossary.


        :return: The workflow_status of this Glossary.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this Glossary.
        Status of the approval process workflow for this business glossary.


        :param workflow_status: The workflow_status of this Glossary.
        :type: str
        """
        self._workflow_status = workflow_status

    @property
    def uri(self):
        """
        Gets the uri of this Glossary.
        URI to the tag instance in the API.


        :return: The uri of this Glossary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Glossary.
        URI to the tag instance in the API.


        :param uri: The uri of this Glossary.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
