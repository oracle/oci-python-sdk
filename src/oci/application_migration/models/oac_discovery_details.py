# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .discovery_details import DiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OacDiscoveryDetails(DiscoveryDetails):
    """
    Details about the Oracle Analytics Cloud - Classic application in the source environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OacDiscoveryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.OacDiscoveryDetails.type` attribute
        of this class is ``OAC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OacDiscoveryDetails.
            Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"
        :type type: str

        :param service_instance_user:
            The value to assign to the service_instance_user property of this OacDiscoveryDetails.
        :type service_instance_user: str

        :param service_instance_password:
            The value to assign to the service_instance_password property of this OacDiscoveryDetails.
        :type service_instance_password: str

        """
        self.swagger_types = {
            'type': 'str',
            'service_instance_user': 'str',
            'service_instance_password': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'service_instance_user': 'serviceInstanceUser',
            'service_instance_password': 'serviceInstancePassword'
        }

        self._type = None
        self._service_instance_user = None
        self._service_instance_password = None
        self._type = 'OAC'

    @property
    def service_instance_user(self):
        """
        **[Required]** Gets the service_instance_user of this OacDiscoveryDetails.
        This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.


        :return: The service_instance_user of this OacDiscoveryDetails.
        :rtype: str
        """
        return self._service_instance_user

    @service_instance_user.setter
    def service_instance_user(self, service_instance_user):
        """
        Sets the service_instance_user of this OacDiscoveryDetails.
        This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.


        :param service_instance_user: The service_instance_user of this OacDiscoveryDetails.
        :type: str
        """
        self._service_instance_user = service_instance_user

    @property
    def service_instance_password(self):
        """
        **[Required]** Gets the service_instance_password of this OacDiscoveryDetails.
        This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.


        :return: The service_instance_password of this OacDiscoveryDetails.
        :rtype: str
        """
        return self._service_instance_password

    @service_instance_password.setter
    def service_instance_password(self, service_instance_password):
        """
        Sets the service_instance_password of this OacDiscoveryDetails.
        This field is currently not supported. You must enter a value, such as <code>unused</code>. However, the value that you enter is ignored.


        :param service_instance_password: The service_instance_password of this OacDiscoveryDetails.
        :type: str
        """
        self._service_instance_password = service_instance_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
