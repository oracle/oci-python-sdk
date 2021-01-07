# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Certificate(object):
    """
    A certificate contains information to be installed on a gateway to secure the traffic going
    through it.
    For more information, see
    `API Gateway Concepts`__.

    __ https://docs.cloud.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Certificate.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Certificate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Certificate.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Certificate.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Certificate.
        :type compartment_id: str

        :param subject_names:
            The value to assign to the subject_names property of this Certificate.
        :type subject_names: list[str]

        :param time_not_valid_after:
            The value to assign to the time_not_valid_after property of this Certificate.
        :type time_not_valid_after: datetime

        :param certificate:
            The value to assign to the certificate property of this Certificate.
        :type certificate: str

        :param intermediate_certificates:
            The value to assign to the intermediate_certificates property of this Certificate.
        :type intermediate_certificates: str

        :param time_created:
            The value to assign to the time_created property of this Certificate.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Certificate.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Certificate.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Certificate.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Certificate.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Certificate.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'subject_names': 'list[str]',
            'time_not_valid_after': 'datetime',
            'certificate': 'str',
            'intermediate_certificates': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'subject_names': 'subjectNames',
            'time_not_valid_after': 'timeNotValidAfter',
            'certificate': 'certificate',
            'intermediate_certificates': 'intermediateCertificates',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._subject_names = None
        self._time_not_valid_after = None
        self._certificate = None
        self._intermediate_certificates = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Certificate.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Certificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Certificate.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Certificate.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Certificate.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this Certificate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Certificate.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this Certificate.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Certificate.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Certificate.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Certificate.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Certificate.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subject_names(self):
        """
        **[Required]** Gets the subject_names of this Certificate.
        The entity to be secured by the certificate and additional host names.


        :return: The subject_names of this Certificate.
        :rtype: list[str]
        """
        return self._subject_names

    @subject_names.setter
    def subject_names(self, subject_names):
        """
        Sets the subject_names of this Certificate.
        The entity to be secured by the certificate and additional host names.


        :param subject_names: The subject_names of this Certificate.
        :type: list[str]
        """
        self._subject_names = subject_names

    @property
    def time_not_valid_after(self):
        """
        **[Required]** Gets the time_not_valid_after of this Certificate.
        The date and time the certificate will expire.


        :return: The time_not_valid_after of this Certificate.
        :rtype: datetime
        """
        return self._time_not_valid_after

    @time_not_valid_after.setter
    def time_not_valid_after(self, time_not_valid_after):
        """
        Sets the time_not_valid_after of this Certificate.
        The date and time the certificate will expire.


        :param time_not_valid_after: The time_not_valid_after of this Certificate.
        :type: datetime
        """
        self._time_not_valid_after = time_not_valid_after

    @property
    def certificate(self):
        """
        **[Required]** Gets the certificate of this Certificate.
        The data of the leaf certificate in pem format.


        :return: The certificate of this Certificate.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this Certificate.
        The data of the leaf certificate in pem format.


        :param certificate: The certificate of this Certificate.
        :type: str
        """
        self._certificate = certificate

    @property
    def intermediate_certificates(self):
        """
        Gets the intermediate_certificates of this Certificate.
        The intermediate certificate data associated with the certificate in pem format.


        :return: The intermediate_certificates of this Certificate.
        :rtype: str
        """
        return self._intermediate_certificates

    @intermediate_certificates.setter
    def intermediate_certificates(self, intermediate_certificates):
        """
        Sets the intermediate_certificates of this Certificate.
        The intermediate certificate data associated with the certificate in pem format.


        :param intermediate_certificates: The intermediate_certificates of this Certificate.
        :type: str
        """
        self._intermediate_certificates = intermediate_certificates

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Certificate.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Certificate.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Certificate.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Certificate.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Certificate.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Certificate.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Certificate.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Certificate.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Certificate.
        The current state of the certificate.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Certificate.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Certificate.
        The current state of the certificate.


        :param lifecycle_state: The lifecycle_state of this Certificate.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Certificate.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :return: The lifecycle_details of this Certificate.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Certificate.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Certificate.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Certificate.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Certificate.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Certificate.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Certificate.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Certificate.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Certificate.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Certificate.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Certificate.
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
