# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateApplication(object):
    """
    Full details of an application or a solution, which lives inside the tenancy and may be included into service catalogs.
    """

    #: A constant which can be used with the lifecycle_state property of a PrivateApplication.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateApplication.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateApplication.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PrivateApplication.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a PrivateApplication.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the package_type property of a PrivateApplication.
    #: This constant has a value of "STACK"
    PACKAGE_TYPE_STACK = "STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateApplication object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PrivateApplication.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateApplication.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this PrivateApplication.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this PrivateApplication.
        :type display_name: str

        :param short_description:
            The value to assign to the short_description property of this PrivateApplication.
        :type short_description: str

        :param long_description:
            The value to assign to the long_description property of this PrivateApplication.
        :type long_description: str

        :param logo:
            The value to assign to the logo property of this PrivateApplication.
        :type logo: oci.service_catalog.models.UploadData

        :param package_type:
            The value to assign to the package_type property of this PrivateApplication.
            Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param time_created:
            The value to assign to the time_created property of this PrivateApplication.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PrivateApplication.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this PrivateApplication.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PrivateApplication.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'display_name': 'str',
            'short_description': 'str',
            'long_description': 'str',
            'logo': 'UploadData',
            'package_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'display_name': 'displayName',
            'short_description': 'shortDescription',
            'long_description': 'longDescription',
            'logo': 'logo',
            'package_type': 'packageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._lifecycle_state = None
        self._compartment_id = None
        self._id = None
        self._display_name = None
        self._short_description = None
        self._long_description = None
        self._logo = None
        self._package_type = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PrivateApplication.
        The lifecycle state of the private application.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PrivateApplication.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PrivateApplication.
        The lifecycle state of the private application.


        :param lifecycle_state: The lifecycle_state of this PrivateApplication.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PrivateApplication.
        The `OCID`__ of the compartment where the private application resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PrivateApplication.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateApplication.
        The `OCID`__ of the compartment where the private application resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PrivateApplication.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PrivateApplication.
        The unique identifier for the private application in Marketplace.


        :return: The id of this PrivateApplication.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateApplication.
        The unique identifier for the private application in Marketplace.


        :param id: The id of this PrivateApplication.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PrivateApplication.
        The name of the private application.


        :return: The display_name of this PrivateApplication.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateApplication.
        The name of the private application.


        :param display_name: The display_name of this PrivateApplication.
        :type: str
        """
        self._display_name = display_name

    @property
    def short_description(self):
        """
        Gets the short_description of this PrivateApplication.
        A short description of the private application.


        :return: The short_description of this PrivateApplication.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this PrivateApplication.
        A short description of the private application.


        :param short_description: The short_description of this PrivateApplication.
        :type: str
        """
        self._short_description = short_description

    @property
    def long_description(self):
        """
        Gets the long_description of this PrivateApplication.
        A long description of the private application.


        :return: The long_description of this PrivateApplication.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this PrivateApplication.
        A long description of the private application.


        :param long_description: The long_description of this PrivateApplication.
        :type: str
        """
        self._long_description = long_description

    @property
    def logo(self):
        """
        Gets the logo of this PrivateApplication.

        :return: The logo of this PrivateApplication.
        :rtype: oci.service_catalog.models.UploadData
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this PrivateApplication.

        :param logo: The logo of this PrivateApplication.
        :type: oci.service_catalog.models.UploadData
        """
        self._logo = logo

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PrivateApplication.
        Type of packages within this private application.

        Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PrivateApplication.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PrivateApplication.
        Type of packages within this private application.


        :param package_type: The package_type of this PrivateApplication.
        :type: str
        """
        allowed_values = ["STACK"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PrivateApplication.
        The date and time the private application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-26T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PrivateApplication.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateApplication.
        The date and time the private application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-26T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PrivateApplication.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this PrivateApplication.
        The date and time the private application was last modified, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-12-10T05:10:29.721Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this PrivateApplication.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PrivateApplication.
        The date and time the private application was last modified, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-12-10T05:10:29.721Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this PrivateApplication.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PrivateApplication.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PrivateApplication.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PrivateApplication.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PrivateApplication.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PrivateApplication.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PrivateApplication.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PrivateApplication.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PrivateApplication.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
