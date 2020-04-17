# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TsigKey(object):
    """
    A TSIG key.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a TsigKey.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TsigKey.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new TsigKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this TsigKey.
        :type algorithm: str

        :param name:
            The value to assign to the name property of this TsigKey.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TsigKey.
        :type compartment_id: str

        :param secret:
            The value to assign to the secret property of this TsigKey.
        :type secret: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TsigKey.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TsigKey.
        :type defined_tags: dict(str, dict(str, object))

        :param id:
            The value to assign to the id property of this TsigKey.
        :type id: str

        :param _self:
            The value to assign to the _self property of this TsigKey.
        :type _self: str

        :param time_created:
            The value to assign to the time_created property of this TsigKey.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TsigKey.
            Allowed values for this property are: "ACTIVE", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_updated:
            The value to assign to the time_updated property of this TsigKey.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'algorithm': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'secret': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'id': 'str',
            '_self': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'secret': 'secret',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'id': 'id',
            '_self': 'self',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'time_updated': 'timeUpdated'
        }

        self._algorithm = None
        self._name = None
        self._compartment_id = None
        self._secret = None
        self._freeform_tags = None
        self._defined_tags = None
        self._id = None
        self.__self = None
        self._time_created = None
        self._lifecycle_state = None
        self._time_updated = None

    @property
    def algorithm(self):
        """
        Gets the algorithm of this TsigKey.
        TSIG key algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute.
        Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
        hmac-sha512. For more information on these algorithms, see `RFC 4635`__.

        __ https://tools.ietf.org/html/rfc4635#section-2


        :return: The algorithm of this TsigKey.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this TsigKey.
        TSIG key algorithms are encoded as domain names, but most consist of only one
        non-empty label, which is not required to be explicitly absolute.
        Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256,
        hmac-sha512. For more information on these algorithms, see `RFC 4635`__.

        __ https://tools.ietf.org/html/rfc4635#section-2


        :param algorithm: The algorithm of this TsigKey.
        :type: str
        """
        self._algorithm = algorithm

    @property
    def name(self):
        """
        Gets the name of this TsigKey.
        A globally unique domain name identifying the key for a given pair of hosts.


        :return: The name of this TsigKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TsigKey.
        A globally unique domain name identifying the key for a given pair of hosts.


        :param name: The name of this TsigKey.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TsigKey.
        The OCID of the compartment containing the TSIG key.


        :return: The compartment_id of this TsigKey.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TsigKey.
        The OCID of the compartment containing the TSIG key.


        :param compartment_id: The compartment_id of this TsigKey.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def secret(self):
        """
        Gets the secret of this TsigKey.
        A base64 string encoding the binary shared secret.


        :return: The secret of this TsigKey.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this TsigKey.
        A base64 string encoding the binary shared secret.


        :param secret: The secret of this TsigKey.
        :type: str
        """
        self._secret = secret

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TsigKey.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TsigKey.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TsigKey.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TsigKey.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TsigKey.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TsigKey.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TsigKey.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TsigKey.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def id(self):
        """
        Gets the id of this TsigKey.
        The OCID of the resource.


        :return: The id of this TsigKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TsigKey.
        The OCID of the resource.


        :param id: The id of this TsigKey.
        :type: str
        """
        self._id = id

    @property
    def _self(self):
        """
        Gets the _self of this TsigKey.
        The canonical absolute URL of the resource.


        :return: The _self of this TsigKey.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this TsigKey.
        The canonical absolute URL of the resource.


        :param _self: The _self of this TsigKey.
        :type: str
        """
        self.__self = _self

    @property
    def time_created(self):
        """
        Gets the time_created of this TsigKey.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this TsigKey.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TsigKey.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this TsigKey.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TsigKey.
        The current state of the resource.

        Allowed values for this property are: "ACTIVE", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TsigKey.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TsigKey.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this TsigKey.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TsigKey.
        The date and time the resource was last updated, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_updated of this TsigKey.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TsigKey.
        The date and time the resource was last updated, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_updated: The time_updated of this TsigKey.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
