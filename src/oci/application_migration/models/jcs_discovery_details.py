# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .discovery_details import DiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JcsDiscoveryDetails(DiscoveryDetails):
    """
    Credentials to access the Oracle Java Cloud Service application in the source environment. When you create and update a migration,
    Application Migration connects to the application in the source environment with the supplied credentials and exports the domain
    configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JcsDiscoveryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.JcsDiscoveryDetails.type` attribute
        of this class is ``JCS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this JcsDiscoveryDetails.
            Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"
        :type type: str

        :param weblogic_user:
            The value to assign to the weblogic_user property of this JcsDiscoveryDetails.
        :type weblogic_user: str

        :param weblogic_password:
            The value to assign to the weblogic_password property of this JcsDiscoveryDetails.
        :type weblogic_password: str

        """
        self.swagger_types = {
            'type': 'str',
            'weblogic_user': 'str',
            'weblogic_password': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'weblogic_user': 'weblogicUser',
            'weblogic_password': 'weblogicPassword'
        }

        self._type = None
        self._weblogic_user = None
        self._weblogic_password = None
        self._type = 'JCS'

    @property
    def weblogic_user(self):
        """
        **[Required]** Gets the weblogic_user of this JcsDiscoveryDetails.
        WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.


        :return: The weblogic_user of this JcsDiscoveryDetails.
        :rtype: str
        """
        return self._weblogic_user

    @weblogic_user.setter
    def weblogic_user(self, weblogic_user):
        """
        Sets the weblogic_user of this JcsDiscoveryDetails.
        WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.


        :param weblogic_user: The weblogic_user of this JcsDiscoveryDetails.
        :type: str
        """
        self._weblogic_user = weblogic_user

    @property
    def weblogic_password(self):
        """
        **[Required]** Gets the weblogic_password of this JcsDiscoveryDetails.
        The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.


        :return: The weblogic_password of this JcsDiscoveryDetails.
        :rtype: str
        """
        return self._weblogic_password

    @weblogic_password.setter
    def weblogic_password(self, weblogic_password):
        """
        Sets the weblogic_password of this JcsDiscoveryDetails.
        The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.


        :param weblogic_password: The weblogic_password of this JcsDiscoveryDetails.
        :type: str
        """
        self._weblogic_password = weblogic_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
