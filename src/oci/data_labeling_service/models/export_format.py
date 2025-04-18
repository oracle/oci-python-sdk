# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportFormat(object):
    """
    Specifies the export format to be used for exporting snapshot.
    """

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "JSONL"
    NAME_JSONL = "JSONL"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "JSONL_CONSOLIDATED"
    NAME_JSONL_CONSOLIDATED = "JSONL_CONSOLIDATED"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "CONLL"
    NAME_CONLL = "CONLL"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "SPACY"
    NAME_SPACY = "SPACY"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "COCO"
    NAME_COCO = "COCO"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "YOLO"
    NAME_YOLO = "YOLO"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "PASCAL_VOC"
    NAME_PASCAL_VOC = "PASCAL_VOC"

    #: A constant which can be used with the name property of a ExportFormat.
    #: This constant has a value of "JSONL_COMPACT_PLUS_CONTENT"
    NAME_JSONL_COMPACT_PLUS_CONTENT = "JSONL_COMPACT_PLUS_CONTENT"

    #: A constant which can be used with the version property of a ExportFormat.
    #: This constant has a value of "V2003"
    VERSION_V2003 = "V2003"

    #: A constant which can be used with the version property of a ExportFormat.
    #: This constant has a value of "V5"
    VERSION_V5 = "V5"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportFormat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExportFormat.
            Allowed values for this property are: "JSONL", "JSONL_CONSOLIDATED", "CONLL", "SPACY", "COCO", "YOLO", "PASCAL_VOC", "JSONL_COMPACT_PLUS_CONTENT"
        :type name: str

        :param version:
            The value to assign to the version property of this ExportFormat.
            Allowed values for this property are: "V2003", "V5"
        :type version: str

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'version': 'version'
        }
        self._name = None
        self._version = None

    @property
    def name(self):
        """
        Gets the name of this ExportFormat.
        Name of export format.

        Allowed values for this property are: "JSONL", "JSONL_CONSOLIDATED", "CONLL", "SPACY", "COCO", "YOLO", "PASCAL_VOC", "JSONL_COMPACT_PLUS_CONTENT"


        :return: The name of this ExportFormat.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExportFormat.
        Name of export format.


        :param name: The name of this ExportFormat.
        :type: str
        """
        allowed_values = ["JSONL", "JSONL_CONSOLIDATED", "CONLL", "SPACY", "COCO", "YOLO", "PASCAL_VOC", "JSONL_COMPACT_PLUS_CONTENT"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            raise ValueError(
                f"Invalid value for `name`, must be None or one of {allowed_values}"
            )
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this ExportFormat.
        Version of export format.

        Allowed values for this property are: "V2003", "V5"


        :return: The version of this ExportFormat.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ExportFormat.
        Version of export format.


        :param version: The version of this ExportFormat.
        :type: str
        """
        allowed_values = ["V2003", "V5"]
        if not value_allowed_none_or_none_sentinel(version, allowed_values):
            raise ValueError(
                f"Invalid value for `version`, must be None or one of {allowed_values}"
            )
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
