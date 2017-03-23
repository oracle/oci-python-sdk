# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .volume_attachment import VolumeAttachment
from ...util import formatted_flat_dict


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
        The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name.
        (Also called the \"CHAP password\".)

        Example: `d6866c0d-298b-48ba-95af-309b4faux45e`


        :return: The chap_secret of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """
        Sets the chap_secret of this IScsiVolumeAttachment.
        The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name.
        (Also called the \"CHAP password\".)

        Example: `d6866c0d-298b-48ba-95af-309b4faux45e`


        :param chap_secret: The chap_secret of this IScsiVolumeAttachment.
        :type: str
        """
        self._chap_secret = chap_secret

    @property
    def chap_username(self):
        """
        Gets the chap_username of this IScsiVolumeAttachment.
        The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.

        Example: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`


        :return: The chap_username of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._chap_username

    @chap_username.setter
    def chap_username(self, chap_username):
        """
        Sets the chap_username of this IScsiVolumeAttachment.
        The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.

        Example: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`


        :param chap_username: The chap_username of this IScsiVolumeAttachment.
        :type: str
        """
        self._chap_username = chap_username

    @property
    def ipv4(self):
        """
        Gets the ipv4 of this IScsiVolumeAttachment.
        The volume's iSCSI IP address.

        Example: `169.254.0.2`


        :return: The ipv4 of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """
        Sets the ipv4 of this IScsiVolumeAttachment.
        The volume's iSCSI IP address.

        Example: `169.254.0.2`


        :param ipv4: The ipv4 of this IScsiVolumeAttachment.
        :type: str
        """
        self._ipv4 = ipv4

    @property
    def iqn(self):
        """
        Gets the iqn of this IScsiVolumeAttachment.
        The target volume's iSCSI Qualified Name in the format defined by RFC 3720.

        Example: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`


        :return: The iqn of this IScsiVolumeAttachment.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this IScsiVolumeAttachment.
        The target volume's iSCSI Qualified Name in the format defined by RFC 3720.

        Example: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`


        :param iqn: The iqn of this IScsiVolumeAttachment.
        :type: str
        """
        self._iqn = iqn

    @property
    def port(self):
        """
        Gets the port of this IScsiVolumeAttachment.
        The volume's iSCSI port.

        Example: `3260`


        :return: The port of this IScsiVolumeAttachment.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this IScsiVolumeAttachment.
        The volume's iSCSI port.

        Example: `3260`


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
