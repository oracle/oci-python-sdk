# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociationSummary(object):
    """
    The details of the association.
    """

    #: A constant which can be used with the lifecycle_state property of a AssociationSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AssociationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssociationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssociationSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AssociationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the association_type property of a AssociationSummary.
    #: This constant has a value of "CERTIFICATE"
    ASSOCIATION_TYPE_CERTIFICATE = "CERTIFICATE"

    #: A constant which can be used with the association_type property of a AssociationSummary.
    #: This constant has a value of "CERTIFICATE_AUTHORITY"
    ASSOCIATION_TYPE_CERTIFICATE_AUTHORITY = "CERTIFICATE_AUTHORITY"

    #: A constant which can be used with the association_type property of a AssociationSummary.
    #: This constant has a value of "CA_BUNDLE"
    ASSOCIATION_TYPE_CA_BUNDLE = "CA_BUNDLE"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociationSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this AssociationSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this AssociationSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssociationSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param certificates_resource_id:
            The value to assign to the certificates_resource_id property of this AssociationSummary.
        :type certificates_resource_id: str

        :param associated_resource_id:
            The value to assign to the associated_resource_id property of this AssociationSummary.
        :type associated_resource_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssociationSummary.
        :type compartment_id: str

        :param association_type:
            The value to assign to the association_type property of this AssociationSummary.
            Allowed values for this property are: "CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type association_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'certificates_resource_id': 'str',
            'associated_resource_id': 'str',
            'compartment_id': 'str',
            'association_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'certificates_resource_id': 'certificatesResourceId',
            'associated_resource_id': 'associatedResourceId',
            'compartment_id': 'compartmentId',
            'association_type': 'associationType'
        }

        self._id = None
        self._name = None
        self._time_created = None
        self._lifecycle_state = None
        self._certificates_resource_id = None
        self._associated_resource_id = None
        self._compartment_id = None
        self._association_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssociationSummary.
        The OCID of the association.


        :return: The id of this AssociationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociationSummary.
        The OCID of the association.


        :param id: The id of this AssociationSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AssociationSummary.
        A user-friendly name generated by the service for the association. Name format follows the pattern [certificatesResourceEntityType]-[associatedResourceEntityType]-UUID.


        :return: The name of this AssociationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssociationSummary.
        A user-friendly name generated by the service for the association. Name format follows the pattern [certificatesResourceEntityType]-[associatedResourceEntityType]-UUID.


        :param name: The name of this AssociationSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AssociationSummary.
        A property indicating when the association was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AssociationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AssociationSummary.
        A property indicating when the association was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AssociationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AssociationSummary.
        The current lifecycle state of the association.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AssociationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssociationSummary.
        The current lifecycle state of the association.


        :param lifecycle_state: The lifecycle_state of this AssociationSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def certificates_resource_id(self):
        """
        **[Required]** Gets the certificates_resource_id of this AssociationSummary.
        The OCID of the certificate-related resource associated with another Oracle Cloud Infrastructure resource.


        :return: The certificates_resource_id of this AssociationSummary.
        :rtype: str
        """
        return self._certificates_resource_id

    @certificates_resource_id.setter
    def certificates_resource_id(self, certificates_resource_id):
        """
        Sets the certificates_resource_id of this AssociationSummary.
        The OCID of the certificate-related resource associated with another Oracle Cloud Infrastructure resource.


        :param certificates_resource_id: The certificates_resource_id of this AssociationSummary.
        :type: str
        """
        self._certificates_resource_id = certificates_resource_id

    @property
    def associated_resource_id(self):
        """
        **[Required]** Gets the associated_resource_id of this AssociationSummary.
        The OCID of the associated resource.


        :return: The associated_resource_id of this AssociationSummary.
        :rtype: str
        """
        return self._associated_resource_id

    @associated_resource_id.setter
    def associated_resource_id(self, associated_resource_id):
        """
        Sets the associated_resource_id of this AssociationSummary.
        The OCID of the associated resource.


        :param associated_resource_id: The associated_resource_id of this AssociationSummary.
        :type: str
        """
        self._associated_resource_id = associated_resource_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AssociationSummary.
        The compartment OCID of the association. This is strongly tied to the compartment OCID of the certificate-related resource.


        :return: The compartment_id of this AssociationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssociationSummary.
        The compartment OCID of the association. This is strongly tied to the compartment OCID of the certificate-related resource.


        :param compartment_id: The compartment_id of this AssociationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def association_type(self):
        """
        **[Required]** Gets the association_type of this AssociationSummary.
        Type of the association.

        Allowed values for this property are: "CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The association_type of this AssociationSummary.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this AssociationSummary.
        Type of the association.


        :param association_type: The association_type of this AssociationSummary.
        :type: str
        """
        allowed_values = ["CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE"]
        if not value_allowed_none_or_none_sentinel(association_type, allowed_values):
            association_type = 'UNKNOWN_ENUM_VALUE'
        self._association_type = association_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
