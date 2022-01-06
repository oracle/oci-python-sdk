# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BucketSummary(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BucketSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this BucketSummary.
        :type namespace: str

        :param name:
            The value to assign to the name property of this BucketSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BucketSummary.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this BucketSummary.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this BucketSummary.
        :type time_created: datetime

        :param etag:
            The value to assign to the etag property of this BucketSummary.
        :type etag: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BucketSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BucketSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'namespace': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'created_by': 'str',
            'time_created': 'datetime',
            'etag': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'etag': 'etag',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._namespace = None
        self._name = None
        self._compartment_id = None
        self._created_by = None
        self._time_created = None
        self._etag = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this BucketSummary.
        The Object Storage namespace in which the bucket lives.


        :return: The namespace of this BucketSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this BucketSummary.
        The Object Storage namespace in which the bucket lives.


        :param namespace: The namespace of this BucketSummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BucketSummary.
        The name of the bucket. Avoid entering confidential information.
        Example: my-new-bucket1


        :return: The name of this BucketSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BucketSummary.
        The name of the bucket. Avoid entering confidential information.
        Example: my-new-bucket1


        :param name: The name of this BucketSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BucketSummary.
        The compartment ID in which the bucket is authorized.


        :return: The compartment_id of this BucketSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BucketSummary.
        The compartment ID in which the bucket is authorized.


        :param compartment_id: The compartment_id of this BucketSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this BucketSummary.
        The `OCID`__ of the user who created the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The created_by of this BucketSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this BucketSummary.
        The `OCID`__ of the user who created the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this BucketSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BucketSummary.
        The date and time the bucket was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_created of this BucketSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BucketSummary.
        The date and time the bucket was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_created: The time_created of this BucketSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this BucketSummary.
        The entity tag (ETag) for the bucket.


        :return: The etag of this BucketSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this BucketSummary.
        The entity tag (ETag) for the bucket.


        :param etag: The etag of this BucketSummary.
        :type: str
        """
        self._etag = etag

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BucketSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BucketSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BucketSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BucketSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BucketSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BucketSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BucketSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BucketSummary.
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
