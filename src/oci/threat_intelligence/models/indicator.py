# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Indicator(object):
    """
    A data signature observed on a network or host that indicates a potential security threat. Indicators can be plain text or computed (hashed) values.
    """

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "DOMAIN_NAME"
    TYPE_DOMAIN_NAME = "DOMAIN_NAME"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "FILE_NAME"
    TYPE_FILE_NAME = "FILE_NAME"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "MD5_HASH"
    TYPE_MD5_HASH = "MD5_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "SHA1_HASH"
    TYPE_SHA1_HASH = "SHA1_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "SHA256_HASH"
    TYPE_SHA256_HASH = "SHA256_HASH"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "IP_ADDRESS"
    TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the type property of a Indicator.
    #: This constant has a value of "URL"
    TYPE_URL = "URL"

    #: A constant which can be used with the lifecycle_state property of a Indicator.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Indicator.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Indicator object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Indicator.
        :type id: str

        :param type:
            The value to assign to the type property of this Indicator.
            Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this Indicator.
        :type value: str

        :param confidence:
            The value to assign to the confidence property of this Indicator.
        :type confidence: int

        :param compartment_id:
            The value to assign to the compartment_id property of this Indicator.
        :type compartment_id: str

        :param threat_types:
            The value to assign to the threat_types property of this Indicator.
        :type threat_types: list[oci.threat_intelligence.models.ThreatType]

        :param attributes:
            The value to assign to the attributes property of this Indicator.
        :type attributes: list[oci.threat_intelligence.models.IndicatorAttribute]

        :param relationships:
            The value to assign to the relationships property of this Indicator.
        :type relationships: list[oci.threat_intelligence.models.IndicatorRelationship]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Indicator.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Indicator.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Indicator.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'value': 'str',
            'confidence': 'int',
            'compartment_id': 'str',
            'threat_types': 'list[ThreatType]',
            'attributes': 'list[IndicatorAttribute]',
            'relationships': 'list[IndicatorRelationship]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'value': 'value',
            'confidence': 'confidence',
            'compartment_id': 'compartmentId',
            'threat_types': 'threatTypes',
            'attributes': 'attributes',
            'relationships': 'relationships',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._type = None
        self._value = None
        self._confidence = None
        self._compartment_id = None
        self._threat_types = None
        self._attributes = None
        self._relationships = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Indicator.
        The OCID of the indicator.


        :return: The id of this Indicator.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Indicator.
        The OCID of the indicator.


        :param id: The id of this Indicator.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Indicator.
        Type of indicator

        Allowed values for this property are: "DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Indicator.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Indicator.
        Type of indicator


        :param type: The type of this Indicator.
        :type: str
        """
        allowed_values = ["DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Indicator.
        The value for this indicator.
        Format is dependent upon `type`, e.g. DOMAIN_NAME \"evil.example.com\", MD5_HASH \"44d88612fea8a8f36de82e1278abb02f\", IP_ADDRESS \"2001:db8::1\".


        :return: The value of this Indicator.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Indicator.
        The value for this indicator.
        Format is dependent upon `type`, e.g. DOMAIN_NAME \"evil.example.com\", MD5_HASH \"44d88612fea8a8f36de82e1278abb02f\", IP_ADDRESS \"2001:db8::1\".


        :param value: The value of this Indicator.
        :type: str
        """
        self._value = value

    @property
    def confidence(self):
        """
        Gets the confidence of this Indicator.
        Confidence is an integer from 0 to 100 that provides a measure of our certainty in the maliciousness of the indicator.  This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.


        :return: The confidence of this Indicator.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Indicator.
        Confidence is an integer from 0 to 100 that provides a measure of our certainty in the maliciousness of the indicator.  This confidence value is aggregated from the confidence in the threat types, attributes, and relationships to create an overall value for the indicator.


        :param confidence: The confidence of this Indicator.
        :type: int
        """
        self._confidence = confidence

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Indicator.
        Compartment Identifier


        :return: The compartment_id of this Indicator.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Indicator.
        Compartment Identifier


        :param compartment_id: The compartment_id of this Indicator.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def threat_types(self):
        """
        **[Required]** Gets the threat_types of this Indicator.
        Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.


        :return: The threat_types of this Indicator.
        :rtype: list[oci.threat_intelligence.models.ThreatType]
        """
        return self._threat_types

    @threat_types.setter
    def threat_types(self, threat_types):
        """
        Sets the threat_types of this Indicator.
        Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.


        :param threat_types: The threat_types of this Indicator.
        :type: list[oci.threat_intelligence.models.ThreatType]
        """
        self._threat_types = threat_types

    @property
    def attributes(self):
        """
        **[Required]** Gets the attributes of this Indicator.
        A map of attribute name (string) to IndicatorAttribute (values and supporting data).
        This provides generic storage for additional data about an indicator.


        :return: The attributes of this Indicator.
        :rtype: list[oci.threat_intelligence.models.IndicatorAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this Indicator.
        A map of attribute name (string) to IndicatorAttribute (values and supporting data).
        This provides generic storage for additional data about an indicator.


        :param attributes: The attributes of this Indicator.
        :type: list[oci.threat_intelligence.models.IndicatorAttribute]
        """
        self._attributes = attributes

    @property
    def relationships(self):
        """
        **[Required]** Gets the relationships of this Indicator.
        A map of relationship name (string) to IndicatorRelationship (related entities and supporting data).
        This provides generic storage for relationships between indicators or other entities.


        :return: The relationships of this Indicator.
        :rtype: list[oci.threat_intelligence.models.IndicatorRelationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Indicator.
        A map of relationship name (string) to IndicatorRelationship (related entities and supporting data).
        This provides generic storage for relationships between indicators or other entities.


        :param relationships: The relationships of this Indicator.
        :type: list[oci.threat_intelligence.models.IndicatorRelationship]
        """
        self._relationships = relationships

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Indicator.
        The state of the indicator.  It will always be ACTIVE.  This field is added for consistency.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Indicator.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Indicator.
        The state of the indicator.  It will always be ACTIVE.  This field is added for consistency.


        :param lifecycle_state: The lifecycle_state of this Indicator.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Indicator.
        The time the data was first seen for this indicator. An RFC3339 formatted datetime string


        :return: The time_created of this Indicator.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Indicator.
        The time the data was first seen for this indicator. An RFC3339 formatted datetime string


        :param time_created: The time_created of this Indicator.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Indicator.
        The last time this indicator was updated. It starts with the same value as timeCreated and is never empty. An RFC3339 formatted datetime string


        :return: The time_updated of this Indicator.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Indicator.
        The last time this indicator was updated. It starts with the same value as timeCreated and is never empty. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this Indicator.
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
