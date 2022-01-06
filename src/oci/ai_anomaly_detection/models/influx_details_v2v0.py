# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .influx_details import InfluxDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InfluxDetailsV2v0(InfluxDetails):
    """
    Influx details for V_2_0.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InfluxDetailsV2v0 object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.InfluxDetailsV2v0.influx_version` attribute
        of this class is ``V_2_0`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param influx_version:
            The value to assign to the influx_version property of this InfluxDetailsV2v0.
            Allowed values for this property are: "V_1_8", "V_2_0"
        :type influx_version: str

        :param bucket_name:
            The value to assign to the bucket_name property of this InfluxDetailsV2v0.
        :type bucket_name: str

        :param organization_name:
            The value to assign to the organization_name property of this InfluxDetailsV2v0.
        :type organization_name: str

        """
        self.swagger_types = {
            'influx_version': 'str',
            'bucket_name': 'str',
            'organization_name': 'str'
        }

        self.attribute_map = {
            'influx_version': 'influxVersion',
            'bucket_name': 'bucketName',
            'organization_name': 'organizationName'
        }

        self._influx_version = None
        self._bucket_name = None
        self._organization_name = None
        self._influx_version = 'V_2_0'

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this InfluxDetailsV2v0.
        Bucket Name for influx connection


        :return: The bucket_name of this InfluxDetailsV2v0.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this InfluxDetailsV2v0.
        Bucket Name for influx connection


        :param bucket_name: The bucket_name of this InfluxDetailsV2v0.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def organization_name(self):
        """
        **[Required]** Gets the organization_name of this InfluxDetailsV2v0.
        Org name for the influx db


        :return: The organization_name of this InfluxDetailsV2v0.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this InfluxDetailsV2v0.
        Org name for the influx db


        :param organization_name: The organization_name of this InfluxDetailsV2v0.
        :type: str
        """
        self._organization_name = organization_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
