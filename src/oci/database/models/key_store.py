# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyStore(object):
    """
    A key store to connect to an on-premise encryption key appliance like Oracle Key Vault.
    """

    #: A constant which can be used with the lifecycle_state property of a KeyStore.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a KeyStore.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new KeyStore object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this KeyStore.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this KeyStore.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this KeyStore.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this KeyStore.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KeyStore.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this KeyStore.
        :type lifecycle_details: str

        :param type_details:
            The value to assign to the type_details property of this KeyStore.
        :type type_details: oci.database.models.KeyStoreTypeDetails

        :param associated_databases:
            The value to assign to the associated_databases property of this KeyStore.
        :type associated_databases: list[oci.database.models.KeyStoreAssociatedDatabaseDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KeyStore.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this KeyStore.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'type_details': 'KeyStoreTypeDetails',
            'associated_databases': 'list[KeyStoreAssociatedDatabaseDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'type_details': 'typeDetails',
            'associated_databases': 'associatedDatabases',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._type_details = None
        self._associated_databases = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this KeyStore.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this KeyStore.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeyStore.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this KeyStore.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this KeyStore.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this KeyStore.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this KeyStore.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this KeyStore.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this KeyStore.
        The user-friendly name for the key store. The name does not need to be unique.


        :return: The display_name of this KeyStore.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this KeyStore.
        The user-friendly name for the key store. The name does not need to be unique.


        :param display_name: The display_name of this KeyStore.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this KeyStore.
        The date and time that the key store was created.


        :return: The time_created of this KeyStore.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this KeyStore.
        The date and time that the key store was created.


        :param time_created: The time_created of this KeyStore.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this KeyStore.
        The current state of the key store.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this KeyStore.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this KeyStore.
        The current state of the key store.


        :param lifecycle_state: The lifecycle_state of this KeyStore.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this KeyStore.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this KeyStore.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this KeyStore.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this KeyStore.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def type_details(self):
        """
        **[Required]** Gets the type_details of this KeyStore.

        :return: The type_details of this KeyStore.
        :rtype: oci.database.models.KeyStoreTypeDetails
        """
        return self._type_details

    @type_details.setter
    def type_details(self, type_details):
        """
        Sets the type_details of this KeyStore.

        :param type_details: The type_details of this KeyStore.
        :type: oci.database.models.KeyStoreTypeDetails
        """
        self._type_details = type_details

    @property
    def associated_databases(self):
        """
        Gets the associated_databases of this KeyStore.
        List of databases associated with the key store.


        :return: The associated_databases of this KeyStore.
        :rtype: list[oci.database.models.KeyStoreAssociatedDatabaseDetails]
        """
        return self._associated_databases

    @associated_databases.setter
    def associated_databases(self, associated_databases):
        """
        Sets the associated_databases of this KeyStore.
        List of databases associated with the key store.


        :param associated_databases: The associated_databases of this KeyStore.
        :type: list[oci.database.models.KeyStoreAssociatedDatabaseDetails]
        """
        self._associated_databases = associated_databases

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this KeyStore.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this KeyStore.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this KeyStore.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this KeyStore.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this KeyStore.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this KeyStore.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this KeyStore.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this KeyStore.
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
