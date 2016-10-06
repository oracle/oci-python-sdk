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


from ..util import formatted_flat_dict


class Instance(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'image_id': 'str',
            'lifecycle_state': 'str',
            'metadata': 'dict(str, str)',
            'region': 'str',
            'shape': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'image_id': 'imageId',
            'lifecycle_state': 'lifecycleState',
            'metadata': 'metadata',
            'region': 'region',
            'shape': 'shape',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._image_id = None
        self._lifecycle_state = None
        self._metadata = None
        self._region = None
        self._shape = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Instance.
        The Availability Domain the instance is running in.
        Example: `Uocm:PHX-AD-1`

        :return: The availability_domain of this Instance.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Instance.
        The Availability Domain the instance is running in.
        Example: `Uocm:PHX-AD-1`

        :param availability_domain: The availability_domain of this Instance.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Instance.
        The OCID of the compartment that contains the instance.

        :return: The compartment_id of this Instance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Instance.
        The OCID of the compartment that contains the instance.

        :param compartment_id: The compartment_id of this Instance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Instance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Example: `My bare metal instance`

        :return: The display_name of this Instance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Instance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Example: `My bare metal instance`

        :param display_name: The display_name of this Instance.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Instance.
        The OCID that uniquely identifies the instance.

        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Instance.
        The OCID that uniquely identifies the instance.

        :param id: The id of this Instance.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """
        Gets the image_id of this Instance.
        The image used to boot the instance. You can enumerate all available images by calling
        ListImages.

        :return: The image_id of this Instance.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this Instance.
        The image used to boot the instance. You can enumerate all available images by calling
        ListImages.

        :param image_id: The image_id of this Instance.
        :type: str
        """
        self._image_id = image_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Instance.
        The current state of the instance.

        :return: The lifecycle_state of this Instance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Instance.
        The current state of the instance.

        :param lifecycle_state: The lifecycle_state of this Instance.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def metadata(self):
        """
        Gets the metadata of this Instance.
        Custom metadata that you provide.

        :return: The metadata of this Instance.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Instance.
        Custom metadata that you provide.

        :param metadata: The metadata of this Instance.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def region(self):
        """
        Gets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.
        Example: `phx`

        :return: The region of this Instance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.
        Example: `phx`

        :param region: The region of this Instance.
        :type: str
        """
        self._region = region

    @property
    def shape(self):
        """
        Gets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. You can enumerate all available shapes by calling
        ListShapes.

        :return: The shape of this Instance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. You can enumerate all available shapes by calling
        ListShapes.

        :param shape: The shape of this Instance.
        :type: str
        """
        self._shape = shape

    @property
    def time_created(self):
        """
        Gets the time_created of this Instance.
        The date and time the instance was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`

        :return: The time_created of this Instance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Instance.
        The date and time the instance was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`

        :param time_created: The time_created of this Instance.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
