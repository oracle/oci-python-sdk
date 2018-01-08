# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BucketSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new BucketSummary object with values from values from keyword arguments.
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

        """
        self.swagger_types = {
            'namespace': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'created_by': 'str',
            'time_created': 'datetime',
            'etag': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'etag': 'etag'
        }

        self._namespace = None
        self._name = None
        self._compartment_id = None
        self._created_by = None
        self._time_created = None
        self._etag = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this BucketSummary.
        The namespace in which the bucket lives.


        :return: The namespace of this BucketSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this BucketSummary.
        The namespace in which the bucket lives.


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
        The OCID of the user who created the bucket.


        :return: The created_by of this BucketSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this BucketSummary.
        The OCID of the user who created the bucket.


        :param created_by: The created_by of this BucketSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BucketSummary.
        The date and time the bucket was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :return: The time_created of this BucketSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BucketSummary.
        The date and time the bucket was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :param time_created: The time_created of this BucketSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this BucketSummary.
        The entity tag for the bucket.


        :return: The etag of this BucketSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this BucketSummary.
        The entity tag for the bucket.


        :param etag: The etag of this BucketSummary.
        :type: str
        """
        self._etag = etag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
