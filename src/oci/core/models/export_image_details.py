# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportImageDetails(object):
    """
    The destination details for the image export.

    Set `destinationType` to `objectStorageTuple`
    and use :func:`export_image_via_object_storage_tuple_details`
    when specifying the namespace, bucket name, and object name.

    Set `destinationType` to `objectStorageUri` and
    use :func:`export_image_via_object_storage_uri_details`
    when specifying the Object Storage URL.
    """

    #: A constant which can be used with the export_format property of a ExportImageDetails.
    #: This constant has a value of "QCOW2"
    EXPORT_FORMAT_QCOW2 = "QCOW2"

    #: A constant which can be used with the export_format property of a ExportImageDetails.
    #: This constant has a value of "VMDK"
    EXPORT_FORMAT_VMDK = "VMDK"

    #: A constant which can be used with the export_format property of a ExportImageDetails.
    #: This constant has a value of "OCI"
    EXPORT_FORMAT_OCI = "OCI"

    #: A constant which can be used with the export_format property of a ExportImageDetails.
    #: This constant has a value of "VHD"
    EXPORT_FORMAT_VHD = "VHD"

    #: A constant which can be used with the export_format property of a ExportImageDetails.
    #: This constant has a value of "VDI"
    EXPORT_FORMAT_VDI = "VDI"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportImageDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ExportImageViaObjectStorageUriDetails`
        * :class:`~oci.core.models.ExportImageViaObjectStorageTupleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_type:
            The value to assign to the destination_type property of this ExportImageDetails.
        :type destination_type: str

        :param export_format:
            The value to assign to the export_format property of this ExportImageDetails.
            Allowed values for this property are: "QCOW2", "VMDK", "OCI", "VHD", "VDI"
        :type export_format: str

        """
        self.swagger_types = {
            'destination_type': 'str',
            'export_format': 'str'
        }
        self.attribute_map = {
            'destination_type': 'destinationType',
            'export_format': 'exportFormat'
        }
        self._destination_type = None
        self._export_format = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['destinationType']

        if type == 'objectStorageUri':
            return 'ExportImageViaObjectStorageUriDetails'

        if type == 'objectStorageTuple':
            return 'ExportImageViaObjectStorageTupleDetails'
        else:
            return 'ExportImageDetails'

    @property
    def destination_type(self):
        """
        **[Required]** Gets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage URL.


        :return: The destination_type of this ExportImageDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage URL.


        :param destination_type: The destination_type of this ExportImageDetails.
        :type: str
        """
        self._destination_type = destination_type

    @property
    def export_format(self):
        """
        Gets the export_format of this ExportImageDetails.
        The format to export the image to. The default value is `OCI`.

        The following image formats are available:

        - `OCI` - Oracle Cloud Infrastructure file with a QCOW2 image and Oracle Cloud Infrastructure metadata (.oci).
        Use this format to export a custom image that you want to import into other tenancies or regions.
        - `QCOW2` - QEMU Copy On Write (.qcow2)
        - `VDI` - Virtual Disk Image (.vdi) for Oracle VM VirtualBox
        - `VHD` - Virtual Hard Disk (.vhd) for Hyper-V
        - `VMDK` - Virtual Machine Disk (.vmdk)

        Allowed values for this property are: "QCOW2", "VMDK", "OCI", "VHD", "VDI"


        :return: The export_format of this ExportImageDetails.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        """
        Sets the export_format of this ExportImageDetails.
        The format to export the image to. The default value is `OCI`.

        The following image formats are available:

        - `OCI` - Oracle Cloud Infrastructure file with a QCOW2 image and Oracle Cloud Infrastructure metadata (.oci).
        Use this format to export a custom image that you want to import into other tenancies or regions.
        - `QCOW2` - QEMU Copy On Write (.qcow2)
        - `VDI` - Virtual Disk Image (.vdi) for Oracle VM VirtualBox
        - `VHD` - Virtual Hard Disk (.vhd) for Hyper-V
        - `VMDK` - Virtual Machine Disk (.vmdk)


        :param export_format: The export_format of this ExportImageDetails.
        :type: str
        """
        allowed_values = ["QCOW2", "VMDK", "OCI", "VHD", "VDI"]
        if not value_allowed_none_or_none_sentinel(export_format, allowed_values):
            raise ValueError(
                f"Invalid value for `export_format`, must be None or one of {allowed_values}"
            )
        self._export_format = export_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
