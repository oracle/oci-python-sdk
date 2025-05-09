# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PiiEntityMasking(object):
    """
    Mask recognized PII entities with different modes.
    """

    #: A constant which can be used with the mode property of a PiiEntityMasking.
    #: This constant has a value of "REPLACE"
    MODE_REPLACE = "REPLACE"

    #: A constant which can be used with the mode property of a PiiEntityMasking.
    #: This constant has a value of "MASK"
    MODE_MASK = "MASK"

    #: A constant which can be used with the mode property of a PiiEntityMasking.
    #: This constant has a value of "REMOVE"
    MODE_REMOVE = "REMOVE"

    def __init__(self, **kwargs):
        """
        Initializes a new PiiEntityMasking object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_language.models.PiiEntityReplace`
        * :class:`~oci.ai_language.models.PiiEntityRemove`
        * :class:`~oci.ai_language.models.PiiEntityMask`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mode:
            The value to assign to the mode property of this PiiEntityMasking.
            Allowed values for this property are: "REPLACE", "MASK", "REMOVE"
        :type mode: str

        :param exclude:
            The value to assign to the exclude property of this PiiEntityMasking.
        :type exclude: list[str]

        :param should_detect:
            The value to assign to the should_detect property of this PiiEntityMasking.
        :type should_detect: bool

        """
        self.swagger_types = {
            'mode': 'str',
            'exclude': 'list[str]',
            'should_detect': 'bool'
        }
        self.attribute_map = {
            'mode': 'mode',
            'exclude': 'exclude',
            'should_detect': 'shouldDetect'
        }
        self._mode = None
        self._exclude = None
        self._should_detect = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['mode']

        if type == 'REPLACE':
            return 'PiiEntityReplace'

        if type == 'REMOVE':
            return 'PiiEntityRemove'

        if type == 'MASK':
            return 'PiiEntityMask'
        else:
            return 'PiiEntityMasking'

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this PiiEntityMasking.
        The type of masking mode.

        Allowed values for this property are: "REPLACE", "MASK", "REMOVE"


        :return: The mode of this PiiEntityMasking.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this PiiEntityMasking.
        The type of masking mode.


        :param mode: The mode of this PiiEntityMasking.
        :type: str
        """
        allowed_values = ["REPLACE", "MASK", "REMOVE"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            raise ValueError(
                f"Invalid value for `mode`, must be None or one of {allowed_values}"
            )
        self._mode = mode

    @property
    def exclude(self):
        """
        Gets the exclude of this PiiEntityMasking.
        List of offsets/entities to be removed from anonymization.


        :return: The exclude of this PiiEntityMasking.
        :rtype: list[str]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """
        Sets the exclude of this PiiEntityMasking.
        List of offsets/entities to be removed from anonymization.


        :param exclude: The exclude of this PiiEntityMasking.
        :type: list[str]
        """
        self._exclude = exclude

    @property
    def should_detect(self):
        """
        Gets the should_detect of this PiiEntityMasking.
        To include excluded entities from masking in detected entities or not.


        :return: The should_detect of this PiiEntityMasking.
        :rtype: bool
        """
        return self._should_detect

    @should_detect.setter
    def should_detect(self, should_detect):
        """
        Sets the should_detect of this PiiEntityMasking.
        To include excluded entities from masking in detected entities or not.


        :param should_detect: The should_detect of this PiiEntityMasking.
        :type: bool
        """
        self._should_detect = should_detect

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
