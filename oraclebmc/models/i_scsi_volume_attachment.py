# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen

from .volume_attachment import VolumeAttachment
from ..util import formatted_flat_dict


class IScsiVolumeAttachment(VolumeAttachment):

    def __init__(self):

        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'volume_id': 'str',
            'chap_secret': 'str',
            'chap_username': 'str',
            'ipv4': 'str',
            'iqn': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'attachment_type': 'attachmentType',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'volume_id': 'volumeId',
            'chap_secret': 'chapSecret',
            'chap_username': 'chapUsername',
            'ipv4': 'ipv4',
            'iqn': 'iqn',
            'port': 'port'
        }

        self._attachment_type = None
        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._volume_id = None
        self._chap_secret = None
        self._chap_username = None
        self._ipv4 = None
        self._iqn = None
        self._port = None

        self._attachment_type = 'iscsi'

    @property
    def chap_secret(self):
        """
        Gets the chap_secret of this IScsiVolumeAttachment.
        The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name.\n(Also called the \"CHAP password\".)\n\nExample: `d6866c0d-298b-48ba-95af-309b4faux45e`\n

        :return: The chap_secret of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """
        Sets the chap_secret of this IScsiVolumeAttachment.
        The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name.\n(Also called the \"CHAP password\".)\n\nExample: `d6866c0d-298b-48ba-95af-309b4faux45e`\n

        :param chap_secret: The chap_secret of this IScsiVolumeAttachment.
        :type: str
        """
        self._chap_secret = chap_secret

    @property
    def chap_username(self):
        """
        Gets the chap_username of this IScsiVolumeAttachment.
        The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.\n\nExample: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`\n

        :return: The chap_username of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._chap_username

    @chap_username.setter
    def chap_username(self, chap_username):
        """
        Sets the chap_username of this IScsiVolumeAttachment.
        The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.\n\nExample: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`\n

        :param chap_username: The chap_username of this IScsiVolumeAttachment.
        :type: str
        """
        self._chap_username = chap_username

    @property
    def ipv4(self):
        """
        Gets the ipv4 of this IScsiVolumeAttachment.
        The volume's iSCSI IP address.\n\nExample: `169.254.0.2`\n

        :return: The ipv4 of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """
        Sets the ipv4 of this IScsiVolumeAttachment.
        The volume's iSCSI IP address.\n\nExample: `169.254.0.2`\n

        :param ipv4: The ipv4 of this IScsiVolumeAttachment.
        :type: str
        """
        self._ipv4 = ipv4

    @property
    def iqn(self):
        """
        Gets the iqn of this IScsiVolumeAttachment.
        The target volume's iSCSI Qualified Name in the format defined by RFC 3720.\n\nExample: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`\n

        :return: The iqn of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this IScsiVolumeAttachment.
        The target volume's iSCSI Qualified Name in the format defined by RFC 3720.\n\nExample: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`\n

        :param iqn: The iqn of this IScsiVolumeAttachment.
        :type: str
        """
        self._iqn = iqn

    @property
    def port(self):
        """
        Gets the port of this IScsiVolumeAttachment.
        The volume's iSCSI port.\n\nExample: `3260`\n

        :return: The port of this IScsiVolumeAttachment.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this IScsiVolumeAttachment.
        The volume's iSCSI port.\n\nExample: `3260`\n

        :param port: The port of this IScsiVolumeAttachment.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

