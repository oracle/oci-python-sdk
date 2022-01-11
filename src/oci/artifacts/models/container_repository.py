# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerRepository(object):
    """
    Container repository metadata.
    """

    #: A constant which can be used with the lifecycle_state property of a ContainerRepository.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ContainerRepository.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ContainerRepository.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerRepository object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerRepository.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this ContainerRepository.
        :type created_by: str

        :param display_name:
            The value to assign to the display_name property of this ContainerRepository.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ContainerRepository.
        :type id: str

        :param image_count:
            The value to assign to the image_count property of this ContainerRepository.
        :type image_count: int

        :param is_immutable:
            The value to assign to the is_immutable property of this ContainerRepository.
        :type is_immutable: bool

        :param is_public:
            The value to assign to the is_public property of this ContainerRepository.
        :type is_public: bool

        :param layer_count:
            The value to assign to the layer_count property of this ContainerRepository.
        :type layer_count: int

        :param layers_size_in_bytes:
            The value to assign to the layers_size_in_bytes property of this ContainerRepository.
        :type layers_size_in_bytes: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerRepository.
            Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param readme:
            The value to assign to the readme property of this ContainerRepository.
        :type readme: oci.artifacts.models.ContainerRepositoryReadme

        :param time_created:
            The value to assign to the time_created property of this ContainerRepository.
        :type time_created: datetime

        :param time_last_pushed:
            The value to assign to the time_last_pushed property of this ContainerRepository.
        :type time_last_pushed: datetime

        :param billable_size_in_gbs:
            The value to assign to the billable_size_in_gbs property of this ContainerRepository.
        :type billable_size_in_gbs: int

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'created_by': 'str',
            'display_name': 'str',
            'id': 'str',
            'image_count': 'int',
            'is_immutable': 'bool',
            'is_public': 'bool',
            'layer_count': 'int',
            'layers_size_in_bytes': 'int',
            'lifecycle_state': 'str',
            'readme': 'ContainerRepositoryReadme',
            'time_created': 'datetime',
            'time_last_pushed': 'datetime',
            'billable_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'display_name': 'displayName',
            'id': 'id',
            'image_count': 'imageCount',
            'is_immutable': 'isImmutable',
            'is_public': 'isPublic',
            'layer_count': 'layerCount',
            'layers_size_in_bytes': 'layersSizeInBytes',
            'lifecycle_state': 'lifecycleState',
            'readme': 'readme',
            'time_created': 'timeCreated',
            'time_last_pushed': 'timeLastPushed',
            'billable_size_in_gbs': 'billableSizeInGBs'
        }

        self._compartment_id = None
        self._created_by = None
        self._display_name = None
        self._id = None
        self._image_count = None
        self._is_immutable = None
        self._is_public = None
        self._layer_count = None
        self._layers_size_in_bytes = None
        self._lifecycle_state = None
        self._readme = None
        self._time_created = None
        self._time_last_pushed = None
        self._billable_size_in_gbs = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerRepository.
        The OCID of the compartment in which the container repository exists.


        :return: The compartment_id of this ContainerRepository.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerRepository.
        The OCID of the compartment in which the container repository exists.


        :param compartment_id: The compartment_id of this ContainerRepository.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ContainerRepository.
        The id of the user or principal that created the resource.


        :return: The created_by of this ContainerRepository.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ContainerRepository.
        The id of the user or principal that created the resource.


        :param created_by: The created_by of this ContainerRepository.
        :type: str
        """
        self._created_by = created_by

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerRepository.
        The container repository name.


        :return: The display_name of this ContainerRepository.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerRepository.
        The container repository name.


        :param display_name: The display_name of this ContainerRepository.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerRepository.
        The `OCID`__ of the container repository.

        Example: `ocid1.containerrepo.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ContainerRepository.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerRepository.
        The `OCID`__ of the container repository.

        Example: `ocid1.containerrepo.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ContainerRepository.
        :type: str
        """
        self._id = id

    @property
    def image_count(self):
        """
        **[Required]** Gets the image_count of this ContainerRepository.
        Total number of images.


        :return: The image_count of this ContainerRepository.
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        """
        Sets the image_count of this ContainerRepository.
        Total number of images.


        :param image_count: The image_count of this ContainerRepository.
        :type: int
        """
        self._image_count = image_count

    @property
    def is_immutable(self):
        """
        **[Required]** Gets the is_immutable of this ContainerRepository.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :return: The is_immutable of this ContainerRepository.
        :rtype: bool
        """
        return self._is_immutable

    @is_immutable.setter
    def is_immutable(self, is_immutable):
        """
        Sets the is_immutable of this ContainerRepository.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :param is_immutable: The is_immutable of this ContainerRepository.
        :type: bool
        """
        self._is_immutable = is_immutable

    @property
    def is_public(self):
        """
        **[Required]** Gets the is_public of this ContainerRepository.
        Whether the repository is public. A public repository allows unauthenticated access.


        :return: The is_public of this ContainerRepository.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this ContainerRepository.
        Whether the repository is public. A public repository allows unauthenticated access.


        :param is_public: The is_public of this ContainerRepository.
        :type: bool
        """
        self._is_public = is_public

    @property
    def layer_count(self):
        """
        **[Required]** Gets the layer_count of this ContainerRepository.
        Total number of layers.


        :return: The layer_count of this ContainerRepository.
        :rtype: int
        """
        return self._layer_count

    @layer_count.setter
    def layer_count(self, layer_count):
        """
        Sets the layer_count of this ContainerRepository.
        Total number of layers.


        :param layer_count: The layer_count of this ContainerRepository.
        :type: int
        """
        self._layer_count = layer_count

    @property
    def layers_size_in_bytes(self):
        """
        **[Required]** Gets the layers_size_in_bytes of this ContainerRepository.
        Total storage in bytes consumed by layers.


        :return: The layers_size_in_bytes of this ContainerRepository.
        :rtype: int
        """
        return self._layers_size_in_bytes

    @layers_size_in_bytes.setter
    def layers_size_in_bytes(self, layers_size_in_bytes):
        """
        Sets the layers_size_in_bytes of this ContainerRepository.
        Total storage in bytes consumed by layers.


        :param layers_size_in_bytes: The layers_size_in_bytes of this ContainerRepository.
        :type: int
        """
        self._layers_size_in_bytes = layers_size_in_bytes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerRepository.
        The current state of the container repository.

        Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ContainerRepository.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerRepository.
        The current state of the container repository.


        :param lifecycle_state: The lifecycle_state of this ContainerRepository.
        :type: str
        """
        allowed_values = ["AVAILABLE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def readme(self):
        """
        Gets the readme of this ContainerRepository.

        :return: The readme of this ContainerRepository.
        :rtype: oci.artifacts.models.ContainerRepositoryReadme
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """
        Sets the readme of this ContainerRepository.

        :param readme: The readme of this ContainerRepository.
        :type: oci.artifacts.models.ContainerRepositoryReadme
        """
        self._readme = readme

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerRepository.
        An RFC 3339 timestamp indicating when the repository was created.


        :return: The time_created of this ContainerRepository.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerRepository.
        An RFC 3339 timestamp indicating when the repository was created.


        :param time_created: The time_created of this ContainerRepository.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_pushed(self):
        """
        Gets the time_last_pushed of this ContainerRepository.
        An RFC 3339 timestamp indicating when an image was last pushed to the repository.


        :return: The time_last_pushed of this ContainerRepository.
        :rtype: datetime
        """
        return self._time_last_pushed

    @time_last_pushed.setter
    def time_last_pushed(self, time_last_pushed):
        """
        Sets the time_last_pushed of this ContainerRepository.
        An RFC 3339 timestamp indicating when an image was last pushed to the repository.


        :param time_last_pushed: The time_last_pushed of this ContainerRepository.
        :type: datetime
        """
        self._time_last_pushed = time_last_pushed

    @property
    def billable_size_in_gbs(self):
        """
        **[Required]** Gets the billable_size_in_gbs of this ContainerRepository.
        Total storage size in GBs that will be charged.


        :return: The billable_size_in_gbs of this ContainerRepository.
        :rtype: int
        """
        return self._billable_size_in_gbs

    @billable_size_in_gbs.setter
    def billable_size_in_gbs(self, billable_size_in_gbs):
        """
        Sets the billable_size_in_gbs of this ContainerRepository.
        Total storage size in GBs that will be charged.


        :param billable_size_in_gbs: The billable_size_in_gbs of this ContainerRepository.
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
