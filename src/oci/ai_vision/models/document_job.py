# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentJob(object):
    """
    The job details for a batch document analysis.
    """

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "ENG"
    LANGUAGE_ENG = "ENG"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "CES"
    LANGUAGE_CES = "CES"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "DAN"
    LANGUAGE_DAN = "DAN"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "NLD"
    LANGUAGE_NLD = "NLD"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "FIN"
    LANGUAGE_FIN = "FIN"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "FRA"
    LANGUAGE_FRA = "FRA"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "DEU"
    LANGUAGE_DEU = "DEU"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "ELL"
    LANGUAGE_ELL = "ELL"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "HUN"
    LANGUAGE_HUN = "HUN"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "ITA"
    LANGUAGE_ITA = "ITA"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "NOR"
    LANGUAGE_NOR = "NOR"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "POL"
    LANGUAGE_POL = "POL"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "POR"
    LANGUAGE_POR = "POR"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "RON"
    LANGUAGE_RON = "RON"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "RUS"
    LANGUAGE_RUS = "RUS"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "SLK"
    LANGUAGE_SLK = "SLK"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "SPA"
    LANGUAGE_SPA = "SPA"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "SWE"
    LANGUAGE_SWE = "SWE"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "TUR"
    LANGUAGE_TUR = "TUR"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "ARA"
    LANGUAGE_ARA = "ARA"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "CHI_SIM"
    LANGUAGE_CHI_SIM = "CHI_SIM"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "HIN"
    LANGUAGE_HIN = "HIN"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "JPN"
    LANGUAGE_JPN = "JPN"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "KOR"
    LANGUAGE_KOR = "KOR"

    #: A constant which can be used with the language property of a DocumentJob.
    #: This constant has a value of "OTHERS"
    LANGUAGE_OTHERS = "OTHERS"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "INVOICE"
    DOCUMENT_TYPE_INVOICE = "INVOICE"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "RECEIPT"
    DOCUMENT_TYPE_RECEIPT = "RECEIPT"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "RESUME"
    DOCUMENT_TYPE_RESUME = "RESUME"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "TAX_FORM"
    DOCUMENT_TYPE_TAX_FORM = "TAX_FORM"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "DRIVER_LICENSE"
    DOCUMENT_TYPE_DRIVER_LICENSE = "DRIVER_LICENSE"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "PASSPORT"
    DOCUMENT_TYPE_PASSPORT = "PASSPORT"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "BANK_STATEMENT"
    DOCUMENT_TYPE_BANK_STATEMENT = "BANK_STATEMENT"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "CHECK"
    DOCUMENT_TYPE_CHECK = "CHECK"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "PAYSLIP"
    DOCUMENT_TYPE_PAYSLIP = "PAYSLIP"

    #: A constant which can be used with the document_type property of a DocumentJob.
    #: This constant has a value of "OTHERS"
    DOCUMENT_TYPE_OTHERS = "OTHERS"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DocumentJob.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_details property of a DocumentJob.
    #: This constant has a value of "PARTIALLY_SUCCEEDED"
    LIFECYCLE_DETAILS_PARTIALLY_SUCCEEDED = "PARTIALLY_SUCCEEDED"

    #: A constant which can be used with the lifecycle_details property of a DocumentJob.
    #: This constant has a value of "COMPLETELY_FAILED"
    LIFECYCLE_DETAILS_COMPLETELY_FAILED = "COMPLETELY_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DocumentJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DocumentJob.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DocumentJob.
        :type display_name: str

        :param features:
            The value to assign to the features property of this DocumentJob.
        :type features: list[oci.ai_vision.models.DocumentFeature]

        :param language:
            The value to assign to the language property of this DocumentJob.
            Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language: str

        :param document_type:
            The value to assign to the document_type property of this DocumentJob.
            Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type document_type: str

        :param input_location:
            The value to assign to the input_location property of this DocumentJob.
        :type input_location: oci.ai_vision.models.InputLocation

        :param time_accepted:
            The value to assign to the time_accepted property of this DocumentJob.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this DocumentJob.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this DocumentJob.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this DocumentJob.
        :type percent_complete: float

        :param output_location:
            The value to assign to the output_location property of this DocumentJob.
        :type output_location: oci.ai_vision.models.OutputLocation

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DocumentJob.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_zip_output_enabled:
            The value to assign to the is_zip_output_enabled property of this DocumentJob.
        :type is_zip_output_enabled: bool

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DocumentJob.
            Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'features': 'list[DocumentFeature]',
            'language': 'str',
            'document_type': 'str',
            'input_location': 'InputLocation',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'float',
            'output_location': 'OutputLocation',
            'lifecycle_state': 'str',
            'is_zip_output_enabled': 'bool',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'features': 'features',
            'language': 'language',
            'document_type': 'documentType',
            'input_location': 'inputLocation',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete',
            'output_location': 'outputLocation',
            'lifecycle_state': 'lifecycleState',
            'is_zip_output_enabled': 'isZipOutputEnabled',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._features = None
        self._language = None
        self._document_type = None
        self._input_location = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None
        self._output_location = None
        self._lifecycle_state = None
        self._is_zip_output_enabled = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DocumentJob.
        The job id.


        :return: The id of this DocumentJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DocumentJob.
        The job id.


        :param id: The id of this DocumentJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DocumentJob.
        The OCID of the compartment that starts the job.


        :return: The compartment_id of this DocumentJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DocumentJob.
        The OCID of the compartment that starts the job.


        :param compartment_id: The compartment_id of this DocumentJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DocumentJob.
        The document job display name.


        :return: The display_name of this DocumentJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DocumentJob.
        The document job display name.


        :param display_name: The display_name of this DocumentJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def features(self):
        """
        **[Required]** Gets the features of this DocumentJob.
        The list of requested document analysis types.


        :return: The features of this DocumentJob.
        :rtype: list[oci.ai_vision.models.DocumentFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this DocumentJob.
        The list of requested document analysis types.


        :param features: The features of this DocumentJob.
        :type: list[oci.ai_vision.models.DocumentFeature]
        """
        self._features = features

    @property
    def language(self):
        """
        Gets the language of this DocumentJob.
        The document language, abbreviated according to ISO 639-2.

        Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language of this DocumentJob.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this DocumentJob.
        The document language, abbreviated according to ISO 639-2.


        :param language: The language of this DocumentJob.
        :type: str
        """
        allowed_values = ["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            language = 'UNKNOWN_ENUM_VALUE'
        self._language = language

    @property
    def document_type(self):
        """
        Gets the document_type of this DocumentJob.
        The type of document.

        Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The document_type of this DocumentJob.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this DocumentJob.
        The type of document.


        :param document_type: The document_type of this DocumentJob.
        :type: str
        """
        allowed_values = ["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(document_type, allowed_values):
            document_type = 'UNKNOWN_ENUM_VALUE'
        self._document_type = document_type

    @property
    def input_location(self):
        """
        Gets the input_location of this DocumentJob.

        :return: The input_location of this DocumentJob.
        :rtype: oci.ai_vision.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this DocumentJob.

        :param input_location: The input_location of this DocumentJob.
        :type: oci.ai_vision.models.InputLocation
        """
        self._input_location = input_location

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this DocumentJob.
        The job acceptance time.


        :return: The time_accepted of this DocumentJob.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this DocumentJob.
        The job acceptance time.


        :param time_accepted: The time_accepted of this DocumentJob.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this DocumentJob.
        The job start time.


        :return: The time_started of this DocumentJob.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DocumentJob.
        The job start time.


        :param time_started: The time_started of this DocumentJob.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this DocumentJob.
        The job finish time.


        :return: The time_finished of this DocumentJob.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this DocumentJob.
        The job finish time.


        :param time_finished: The time_finished of this DocumentJob.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this DocumentJob.
        How much progress the operation has made, compared to the total amount of work to be performed.


        :return: The percent_complete of this DocumentJob.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this DocumentJob.
        How much progress the operation has made, compared to the total amount of work to be performed.


        :param percent_complete: The percent_complete of this DocumentJob.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this DocumentJob.

        :return: The output_location of this DocumentJob.
        :rtype: oci.ai_vision.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this DocumentJob.

        :param output_location: The output_location of this DocumentJob.
        :type: oci.ai_vision.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DocumentJob.
        The current state of the batch document job.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DocumentJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DocumentJob.
        The current state of the batch document job.


        :param lifecycle_state: The lifecycle_state of this DocumentJob.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_zip_output_enabled(self):
        """
        Gets the is_zip_output_enabled of this DocumentJob.
        Whether or not to generate a ZIP file containing the results.


        :return: The is_zip_output_enabled of this DocumentJob.
        :rtype: bool
        """
        return self._is_zip_output_enabled

    @is_zip_output_enabled.setter
    def is_zip_output_enabled(self, is_zip_output_enabled):
        """
        Sets the is_zip_output_enabled of this DocumentJob.
        Whether or not to generate a ZIP file containing the results.


        :param is_zip_output_enabled: The is_zip_output_enabled of this DocumentJob.
        :type: bool
        """
        self._is_zip_output_enabled = is_zip_output_enabled

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DocumentJob.
        The detailed status of FAILED state.

        Allowed values for this property are: "PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this DocumentJob.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DocumentJob.
        The detailed status of FAILED state.


        :param lifecycle_details: The lifecycle_details of this DocumentJob.
        :type: str
        """
        allowed_values = ["PARTIALLY_SUCCEEDED", "COMPLETELY_FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
