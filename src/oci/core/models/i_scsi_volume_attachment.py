# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_attachment import VolumeAttachment
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IScsiVolumeAttachment(VolumeAttachment):
    """
    An ISCSI volume attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IScsiVolumeAttachment object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.IScsiVolumeAttachment.attachment_type` attribute
        of this class is ``iscsi`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachment_type:
            The value to assign to the attachment_type property of this IScsiVolumeAttachment.
        :type attachment_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this IScsiVolumeAttachment.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IScsiVolumeAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this IScsiVolumeAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this IScsiVolumeAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this IScsiVolumeAttachment.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this IScsiVolumeAttachment.
        :type is_read_only: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IScsiVolumeAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this IScsiVolumeAttachment.
        :type time_created: datetime

        :param volume_id:
            The value to assign to the volume_id property of this IScsiVolumeAttachment.
        :type volume_id: str

        :param chap_secret:
            The value to assign to the chap_secret property of this IScsiVolumeAttachment.
        :type chap_secret: str

        :param chap_username:
            The value to assign to the chap_username property of this IScsiVolumeAttachment.
        :type chap_username: str

        :param ipv4:
            The value to assign to the ipv4 property of this IScsiVolumeAttachment.
        :type ipv4: str

        :param iqn:
            The value to assign to the iqn property of this IScsiVolumeAttachment.
        :type iqn: str

        :param port:
            The value to assign to the port property of this IScsiVolumeAttachment.
        :type port: int

        """
        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
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
            'is_read_only': 'isReadOnly',
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
        self._is_read_only = None
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
        **[Required]** Gets the ipv4 of this IScsiVolumeAttachment.
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
        **[Required]** Gets the iqn of this IScsiVolumeAttachment.
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
        **[Required]** Gets the port of this IScsiVolumeAttachment.
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
