# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerRepositorySummary(object):
    """
    Container repository summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerRepositorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerRepositorySummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerRepositorySummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ContainerRepositorySummary.
        :type id: str

        :param image_count:
            The value to assign to the image_count property of this ContainerRepositorySummary.
        :type image_count: int

        :param is_public:
            The value to assign to the is_public property of this ContainerRepositorySummary.
        :type is_public: bool

        :param layer_count:
            The value to assign to the layer_count property of this ContainerRepositorySummary.
        :type layer_count: int

        :param layers_size_in_bytes:
            The value to assign to the layers_size_in_bytes property of this ContainerRepositorySummary.
        :type layers_size_in_bytes: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerRepositorySummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ContainerRepositorySummary.
        :type time_created: datetime

        :param billable_size_in_gbs:
            The value to assign to the billable_size_in_gbs property of this ContainerRepositorySummary.
        :type billable_size_in_gbs: int

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'image_count': 'int',
            'is_public': 'bool',
            'layer_count': 'int',
            'layers_size_in_bytes': 'int',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'billable_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'image_count': 'imageCount',
            'is_public': 'isPublic',
            'layer_count': 'layerCount',
            'layers_size_in_bytes': 'layersSizeInBytes',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'billable_size_in_gbs': 'billableSizeInGBs'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._image_count = None
        self._is_public = None
        self._layer_count = None
        self._layers_size_in_bytes = None
        self._lifecycle_state = None
        self._time_created = None
        self._billable_size_in_gbs = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerRepositorySummary.
        The OCID of the compartment in which the container repository exists.


        :return: The compartment_id of this ContainerRepositorySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerRepositorySummary.
        The OCID of the compartment in which the container repository exists.


        :param compartment_id: The compartment_id of this ContainerRepositorySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerRepositorySummary.
        The container repository name.


        :return: The display_name of this ContainerRepositorySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerRepositorySummary.
        The container repository name.


        :param display_name: The display_name of this ContainerRepositorySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerRepositorySummary.
        The `OCID`__ of the container repository.

        Example: `ocid1.containerrepo.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ContainerRepositorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerRepositorySummary.
        The `OCID`__ of the container repository.

        Example: `ocid1.containerrepo.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ContainerRepositorySummary.
        :type: str
        """
        self._id = id

    @property
    def image_count(self):
        """
        **[Required]** Gets the image_count of this ContainerRepositorySummary.
        Total number of images.


        :return: The image_count of this ContainerRepositorySummary.
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        """
        Sets the image_count of this ContainerRepositorySummary.
        Total number of images.


        :param image_count: The image_count of this ContainerRepositorySummary.
        :type: int
        """
        self._image_count = image_count

    @property
    def is_public(self):
        """
        **[Required]** Gets the is_public of this ContainerRepositorySummary.
        Whether the repository is public. A public repository allows unauthenticated access.


        :return: The is_public of this ContainerRepositorySummary.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this ContainerRepositorySummary.
        Whether the repository is public. A public repository allows unauthenticated access.


        :param is_public: The is_public of this ContainerRepositorySummary.
        :type: bool
        """
        self._is_public = is_public

    @property
    def layer_count(self):
        """
        **[Required]** Gets the layer_count of this ContainerRepositorySummary.
        Total number of layers.


        :return: The layer_count of this ContainerRepositorySummary.
        :rtype: int
        """
        return self._layer_count

    @layer_count.setter
    def layer_count(self, layer_count):
        """
        Sets the layer_count of this ContainerRepositorySummary.
        Total number of layers.


        :param layer_count: The layer_count of this ContainerRepositorySummary.
        :type: int
        """
        self._layer_count = layer_count

    @property
    def layers_size_in_bytes(self):
        """
        **[Required]** Gets the layers_size_in_bytes of this ContainerRepositorySummary.
        Total storage in bytes consumed by layers.


        :return: The layers_size_in_bytes of this ContainerRepositorySummary.
        :rtype: int
        """
        return self._layers_size_in_bytes

    @layers_size_in_bytes.setter
    def layers_size_in_bytes(self, layers_size_in_bytes):
        """
        Sets the layers_size_in_bytes of this ContainerRepositorySummary.
        Total storage in bytes consumed by layers.


        :param layers_size_in_bytes: The layers_size_in_bytes of this ContainerRepositorySummary.
        :type: int
        """
        self._layers_size_in_bytes = layers_size_in_bytes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerRepositorySummary.
        The current state of the container repository.


        :return: The lifecycle_state of this ContainerRepositorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerRepositorySummary.
        The current state of the container repository.


        :param lifecycle_state: The lifecycle_state of this ContainerRepositorySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerRepositorySummary.
        An RFC 3339 timestamp indicating when the repository was created.


        :return: The time_created of this ContainerRepositorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerRepositorySummary.
        An RFC 3339 timestamp indicating when the repository was created.


        :param time_created: The time_created of this ContainerRepositorySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def billable_size_in_gbs(self):
        """
        **[Required]** Gets the billable_size_in_gbs of this ContainerRepositorySummary.
        Total storage size in GBs that will be charged.


        :return: The billable_size_in_gbs of this ContainerRepositorySummary.
        :rtype: int
        """
        return self._billable_size_in_gbs

    @billable_size_in_gbs.setter
    def billable_size_in_gbs(self, billable_size_in_gbs):
        """
        Sets the billable_size_in_gbs of this ContainerRepositorySummary.
        Total storage size in GBs that will be charged.


        :param billable_size_in_gbs: The billable_size_in_gbs of this ContainerRepositorySummary.
        :type: int
        """
        self._billable_size_in_gbs = billable_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
