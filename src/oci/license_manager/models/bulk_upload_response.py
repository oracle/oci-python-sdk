# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUploadResponse(object):
    """
    The bulk upload response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUploadResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_supported_records:
            The value to assign to the total_supported_records property of this BulkUploadResponse.
        :type total_supported_records: int

        :param total_supported_records_saved:
            The value to assign to the total_supported_records_saved property of this BulkUploadResponse.
        :type total_supported_records_saved: int

        :param total_supported_duplicate_records:
            The value to assign to the total_supported_duplicate_records property of this BulkUploadResponse.
        :type total_supported_duplicate_records: int

        :param total_supported_failed_license_records:
            The value to assign to the total_supported_failed_license_records property of this BulkUploadResponse.
        :type total_supported_failed_license_records: int

        :param total_supported_invalid_records:
            The value to assign to the total_supported_invalid_records property of this BulkUploadResponse.
        :type total_supported_invalid_records: int

        :param validation_error_info:
            The value to assign to the validation_error_info property of this BulkUploadResponse.
        :type validation_error_info: list[oci.license_manager.models.BulkUploadValidationErrorInfo]

        :param failed_license_record_info:
            The value to assign to the failed_license_record_info property of this BulkUploadResponse.
        :type failed_license_record_info: list[oci.license_manager.models.BulkUploadFailedRecordInfo]

        :param message:
            The value to assign to the message property of this BulkUploadResponse.
        :type message: str

        """
        self.swagger_types = {
            'total_supported_records': 'int',
            'total_supported_records_saved': 'int',
            'total_supported_duplicate_records': 'int',
            'total_supported_failed_license_records': 'int',
            'total_supported_invalid_records': 'int',
            'validation_error_info': 'list[BulkUploadValidationErrorInfo]',
            'failed_license_record_info': 'list[BulkUploadFailedRecordInfo]',
            'message': 'str'
        }

        self.attribute_map = {
            'total_supported_records': 'totalSupportedRecords',
            'total_supported_records_saved': 'totalSupportedRecordsSaved',
            'total_supported_duplicate_records': 'totalSupportedDuplicateRecords',
            'total_supported_failed_license_records': 'totalSupportedFailedLicenseRecords',
            'total_supported_invalid_records': 'totalSupportedInvalidRecords',
            'validation_error_info': 'validationErrorInfo',
            'failed_license_record_info': 'failedLicenseRecordInfo',
            'message': 'message'
        }

        self._total_supported_records = None
        self._total_supported_records_saved = None
        self._total_supported_duplicate_records = None
        self._total_supported_failed_license_records = None
        self._total_supported_invalid_records = None
        self._validation_error_info = None
        self._failed_license_record_info = None
        self._message = None

    @property
    def total_supported_records(self):
        """
        **[Required]** Gets the total_supported_records of this BulkUploadResponse.
        The number of license records which were supported.


        :return: The total_supported_records of this BulkUploadResponse.
        :rtype: int
        """
        return self._total_supported_records

    @total_supported_records.setter
    def total_supported_records(self, total_supported_records):
        """
        Sets the total_supported_records of this BulkUploadResponse.
        The number of license records which were supported.


        :param total_supported_records: The total_supported_records of this BulkUploadResponse.
        :type: int
        """
        self._total_supported_records = total_supported_records

    @property
    def total_supported_records_saved(self):
        """
        **[Required]** Gets the total_supported_records_saved of this BulkUploadResponse.
        The number of supported license records that were uploaded successfully.


        :return: The total_supported_records_saved of this BulkUploadResponse.
        :rtype: int
        """
        return self._total_supported_records_saved

    @total_supported_records_saved.setter
    def total_supported_records_saved(self, total_supported_records_saved):
        """
        Sets the total_supported_records_saved of this BulkUploadResponse.
        The number of supported license records that were uploaded successfully.


        :param total_supported_records_saved: The total_supported_records_saved of this BulkUploadResponse.
        :type: int
        """
        self._total_supported_records_saved = total_supported_records_saved

    @property
    def total_supported_duplicate_records(self):
        """
        **[Required]** Gets the total_supported_duplicate_records of this BulkUploadResponse.
        The number of supported license records that were valid but not uploaded since they were duplicates.


        :return: The total_supported_duplicate_records of this BulkUploadResponse.
        :rtype: int
        """
        return self._total_supported_duplicate_records

    @total_supported_duplicate_records.setter
    def total_supported_duplicate_records(self, total_supported_duplicate_records):
        """
        Sets the total_supported_duplicate_records of this BulkUploadResponse.
        The number of supported license records that were valid but not uploaded since they were duplicates.


        :param total_supported_duplicate_records: The total_supported_duplicate_records of this BulkUploadResponse.
        :type: int
        """
        self._total_supported_duplicate_records = total_supported_duplicate_records

    @property
    def total_supported_failed_license_records(self):
        """
        **[Required]** Gets the total_supported_failed_license_records of this BulkUploadResponse.
        The number of supported license records that were valid but failed with errors during upload.


        :return: The total_supported_failed_license_records of this BulkUploadResponse.
        :rtype: int
        """
        return self._total_supported_failed_license_records

    @total_supported_failed_license_records.setter
    def total_supported_failed_license_records(self, total_supported_failed_license_records):
        """
        Sets the total_supported_failed_license_records of this BulkUploadResponse.
        The number of supported license records that were valid but failed with errors during upload.


        :param total_supported_failed_license_records: The total_supported_failed_license_records of this BulkUploadResponse.
        :type: int
        """
        self._total_supported_failed_license_records = total_supported_failed_license_records

    @property
    def total_supported_invalid_records(self):
        """
        **[Required]** Gets the total_supported_invalid_records of this BulkUploadResponse.
        The number of supported license records that could not be uploaded since they were invalid.


        :return: The total_supported_invalid_records of this BulkUploadResponse.
        :rtype: int
        """
        return self._total_supported_invalid_records

    @total_supported_invalid_records.setter
    def total_supported_invalid_records(self, total_supported_invalid_records):
        """
        Sets the total_supported_invalid_records of this BulkUploadResponse.
        The number of supported license records that could not be uploaded since they were invalid.


        :param total_supported_invalid_records: The total_supported_invalid_records of this BulkUploadResponse.
        :type: int
        """
        self._total_supported_invalid_records = total_supported_invalid_records

    @property
    def validation_error_info(self):
        """
        **[Required]** Gets the validation_error_info of this BulkUploadResponse.
        Detailed error information corresponding to each supported but invalid row for the uploaded file.


        :return: The validation_error_info of this BulkUploadResponse.
        :rtype: list[oci.license_manager.models.BulkUploadValidationErrorInfo]
        """
        return self._validation_error_info

    @validation_error_info.setter
    def validation_error_info(self, validation_error_info):
        """
        Sets the validation_error_info of this BulkUploadResponse.
        Detailed error information corresponding to each supported but invalid row for the uploaded file.


        :param validation_error_info: The validation_error_info of this BulkUploadResponse.
        :type: list[oci.license_manager.models.BulkUploadValidationErrorInfo]
        """
        self._validation_error_info = validation_error_info

    @property
    def failed_license_record_info(self):
        """
        **[Required]** Gets the failed_license_record_info of this BulkUploadResponse.
        Error information corresponding to the supported records which are valid but could not be created.


        :return: The failed_license_record_info of this BulkUploadResponse.
        :rtype: list[oci.license_manager.models.BulkUploadFailedRecordInfo]
        """
        return self._failed_license_record_info

    @failed_license_record_info.setter
    def failed_license_record_info(self, failed_license_record_info):
        """
        Sets the failed_license_record_info of this BulkUploadResponse.
        Error information corresponding to the supported records which are valid but could not be created.


        :param failed_license_record_info: The failed_license_record_info of this BulkUploadResponse.
        :type: list[oci.license_manager.models.BulkUploadFailedRecordInfo]
        """
        self._failed_license_record_info = failed_license_record_info

    @property
    def message(self):
        """
        **[Required]** Gets the message of this BulkUploadResponse.
        Response message for bulk upload.


        :return: The message of this BulkUploadResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BulkUploadResponse.
        Response message for bulk upload.


        :param message: The message of this BulkUploadResponse.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
