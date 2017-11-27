# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityProvider(object):

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityProvider object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.identity.models.Saml2IdentityProvider`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IdentityProvider.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IdentityProvider.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this IdentityProvider.
        :type name: str

        :param description:
            The value to assign to the description property of this IdentityProvider.
        :type description: str

        :param product_type:
            The value to assign to the product_type property of this IdentityProvider.
        :type product_type: str

        :param time_created:
            The value to assign to the time_created property of this IdentityProvider.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IdentityProvider.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this IdentityProvider.
        :type inactive_status: int

        :param protocol:
            The value to assign to the protocol property of this IdentityProvider.
        :type protocol: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'product_type': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'product_type': 'productType',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'protocol': 'protocol'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._product_type = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._protocol = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['protocol']

        if type == 'SAML2':
            return 'Saml2IdentityProvider'
        else:
            return 'IdentityProvider'

    @property
    def id(self):
        """
        Gets the id of this IdentityProvider.
        The OCID of the `IdentityProvider`.


        :return: The id of this IdentityProvider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdentityProvider.
        The OCID of the `IdentityProvider`.


        :param id: The id of this IdentityProvider.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IdentityProvider.
        The OCID of the tenancy containing the `IdentityProvider`.


        :return: The compartment_id of this IdentityProvider.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IdentityProvider.
        The OCID of the tenancy containing the `IdentityProvider`.


        :param compartment_id: The compartment_id of this IdentityProvider.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this IdentityProvider.
        The name you assign to the `IdentityProvider` during creation. The name
        must be unique across all `IdentityProvider` objects in the tenancy and
        cannot be changed. This is the name federated users see when choosing
        which identity provider to use when signing in to the Oracle Cloud Infrastructure
        Console.


        :return: The name of this IdentityProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IdentityProvider.
        The name you assign to the `IdentityProvider` during creation. The name
        must be unique across all `IdentityProvider` objects in the tenancy and
        cannot be changed. This is the name federated users see when choosing
        which identity provider to use when signing in to the Oracle Cloud Infrastructure
        Console.


        :param name: The name of this IdentityProvider.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this IdentityProvider.
        The description you assign to the `IdentityProvider` during creation. Does
        not have to be unique, and it's changeable.


        :return: The description of this IdentityProvider.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IdentityProvider.
        The description you assign to the `IdentityProvider` during creation. Does
        not have to be unique, and it's changeable.


        :param description: The description of this IdentityProvider.
        :type: str
        """
        self._description = description

    @property
    def product_type(self):
        """
        Gets the product_type of this IdentityProvider.
        The identity provider service or product.
        Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
        Active Directory Federation Services (ADFS).

        Allowed values are:
        - `ADFS`
        - `IDCS`

        Example: `IDCS`


        :return: The product_type of this IdentityProvider.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this IdentityProvider.
        The identity provider service or product.
        Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
        Active Directory Federation Services (ADFS).

        Allowed values are:
        - `ADFS`
        - `IDCS`

        Example: `IDCS`


        :param product_type: The product_type of this IdentityProvider.
        :type: str
        """
        self._product_type = product_type

    @property
    def time_created(self):
        """
        Gets the time_created of this IdentityProvider.
        Date and time the `IdentityProvider` was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IdentityProvider.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IdentityProvider.
        Date and time the `IdentityProvider` was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IdentityProvider.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IdentityProvider.
        The current state. After creating an `IdentityProvider`, make sure its
        `lifecycleState` changes from CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IdentityProvider.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IdentityProvider.
        The current state. After creating an `IdentityProvider`, make sure its
        `lifecycleState` changes from CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this IdentityProvider.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this IdentityProvider.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this IdentityProvider.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this IdentityProvider.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this IdentityProvider.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def protocol(self):
        """
        Gets the protocol of this IdentityProvider.
        The protocol used for federation. Allowed value: `SAML2`.

        Example: `SAML2`


        :return: The protocol of this IdentityProvider.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this IdentityProvider.
        The protocol used for federation. Allowed value: `SAML2`.

        Example: `SAML2`


        :param protocol: The protocol of this IdentityProvider.
        :type: str
        """
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
