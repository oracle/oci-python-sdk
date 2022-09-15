# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAssetDetails(object):
    """
    The information of asset to be updated.
    """

    #: A constant which can be used with the asset_type property of a UpdateAssetDetails.
    #: This constant has a value of "VMWARE_VM"
    ASSET_TYPE_VMWARE_VM = "VMWARE_VM"

    #: A constant which can be used with the asset_type property of a UpdateAssetDetails.
    #: This constant has a value of "VM"
    ASSET_TYPE_VM = "VM"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAssetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_bridge.models.UpdateVmAssetDetails`
        * :class:`~oci.cloud_bridge.models.UpdateVmwareVmAssetDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAssetDetails.
        :type display_name: str

        :param asset_type:
            The value to assign to the asset_type property of this UpdateAssetDetails.
            Allowed values for this property are: "VMWARE_VM", "VM"
        :type asset_type: str

        :param asset_source_ids:
            The value to assign to the asset_source_ids property of this UpdateAssetDetails.
        :type asset_source_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'asset_type': 'str',
            'asset_source_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'asset_type': 'assetType',
            'asset_source_ids': 'assetSourceIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._asset_type = None
        self._asset_source_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['assetType']

        if type == 'VM':
            return 'UpdateVmAssetDetails'

        if type == 'VMWARE_VM':
            return 'UpdateVmwareVmAssetDetails'
        else:
            return 'UpdateAssetDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAssetDetails.
        Asset display name.


        :return: The display_name of this UpdateAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAssetDetails.
        Asset display name.


        :param display_name: The display_name of this UpdateAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def asset_type(self):
        """
        **[Required]** Gets the asset_type of this UpdateAssetDetails.
        Asset type

        Allowed values for this property are: "VMWARE_VM", "VM"


        :return: The asset_type of this UpdateAssetDetails.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """
        Sets the asset_type of this UpdateAssetDetails.
        Asset type


        :param asset_type: The asset_type of this UpdateAssetDetails.
        :type: str
        """
        allowed_values = ["VMWARE_VM", "VM"]
        if not value_allowed_none_or_none_sentinel(asset_type, allowed_values):
            raise ValueError(
                "Invalid value for `asset_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._asset_type = asset_type

    @property
    def asset_source_ids(self):
        """
        Gets the asset_source_ids of this UpdateAssetDetails.
        List of asset source OCID.


        :return: The asset_source_ids of this UpdateAssetDetails.
        :rtype: list[str]
        """
        return self._asset_source_ids

    @asset_source_ids.setter
    def asset_source_ids(self, asset_source_ids):
        """
        Sets the asset_source_ids of this UpdateAssetDetails.
        List of asset source OCID.


        :param asset_source_ids: The asset_source_ids of this UpdateAssetDetails.
        :type: list[str]
        """
        self._asset_source_ids = asset_source_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAssetDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAssetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAssetDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAssetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAssetDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAssetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAssetDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAssetDetails.
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
