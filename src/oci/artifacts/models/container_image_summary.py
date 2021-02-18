# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerImageSummary(object):
    """
    Container image summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerImageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerImageSummary.
        :type compartment_id: str

        :param digest:
            The value to assign to the digest property of this ContainerImageSummary.
        :type digest: str

        :param display_name:
            The value to assign to the display_name property of this ContainerImageSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ContainerImageSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerImageSummary.
        :type lifecycle_state: str

        :param repository_id:
            The value to assign to the repository_id property of this ContainerImageSummary.
        :type repository_id: str

        :param repository_name:
            The value to assign to the repository_name property of this ContainerImageSummary.
        :type repository_name: str

        :param time_created:
            The value to assign to the time_created property of this ContainerImageSummary.
        :type time_created: datetime

        :param version:
            The value to assign to the version property of this ContainerImageSummary.
        :type version: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'digest': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'repository_id': 'str',
            'repository_name': 'str',
            'time_created': 'datetime',
            'version': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'digest': 'digest',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'repository_id': 'repositoryId',
            'repository_name': 'repositoryName',
            'time_created': 'timeCreated',
            'version': 'version'
        }

        self._compartment_id = None
        self._digest = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._repository_id = None
        self._repository_name = None
        self._time_created = None
        self._version = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerImageSummary.
        The compartment OCID to which the container image belongs. Inferred from the container repository.


        :return: The compartment_id of this ContainerImageSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerImageSummary.
        The compartment OCID to which the container image belongs. Inferred from the container repository.


        :param compartment_id: The compartment_id of this ContainerImageSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def digest(self):
        """
        **[Required]** Gets the digest of this ContainerImageSummary.
        The container image digest.


        :return: The digest of this ContainerImageSummary.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this ContainerImageSummary.
        The container image digest.


        :param digest: The digest of this ContainerImageSummary.
        :type: str
        """
        self._digest = digest

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerImageSummary.
        The repository name and the most recent version associated with the image.
        If there are no versions associated with the image, then last known version and digest are used instead.
        If the last known version is unavailable, then 'unknown' is used instead of the version.

        Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`


        :return: The display_name of this ContainerImageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerImageSummary.
        The repository name and the most recent version associated with the image.
        If there are no versions associated with the image, then last known version and digest are used instead.
        If the last known version is unavailable, then 'unknown' is used instead of the version.

        Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`


        :param display_name: The display_name of this ContainerImageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerImageSummary.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ContainerImageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerImageSummary.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ContainerImageSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerImageSummary.
        The current state of the container image.


        :return: The lifecycle_state of this ContainerImageSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerImageSummary.
        The current state of the container image.


        :param lifecycle_state: The lifecycle_state of this ContainerImageSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this ContainerImageSummary.
        The OCID of the container repository.


        :return: The repository_id of this ContainerImageSummary.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this ContainerImageSummary.
        The OCID of the container repository.


        :param repository_id: The repository_id of this ContainerImageSummary.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        """
        **[Required]** Gets the repository_name of this ContainerImageSummary.
        The container repository name.


        :return: The repository_name of this ContainerImageSummary.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """
        Sets the repository_name of this ContainerImageSummary.
        The container repository name.


        :param repository_name: The repository_name of this ContainerImageSummary.
        :type: str
        """
        self._repository_name = repository_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerImageSummary.
        An RFC 3339 timestamp indicating when the image was created.


        :return: The time_created of this ContainerImageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerImageSummary.
        An RFC 3339 timestamp indicating when the image was created.


        :param time_created: The time_created of this ContainerImageSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        Gets the version of this ContainerImageSummary.
        The most recent version associated with this image.


        :return: The version of this ContainerImageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ContainerImageSummary.
        The most recent version associated with this image.


        :param version: The version of this ContainerImageSummary.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
