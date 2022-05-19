# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .bulk_upload_cell_info import BulkUploadCellInfo
from .bulk_upload_failed_record_info import BulkUploadFailedRecordInfo
from .bulk_upload_license_records_details import BulkUploadLicenseRecordsDetails
from .bulk_upload_response import BulkUploadResponse
from .bulk_upload_template import BulkUploadTemplate
from .bulk_upload_validation_error_info import BulkUploadValidationErrorInfo
from .configuration import Configuration
from .create_license_record_details import CreateLicenseRecordDetails
from .create_product_license_details import CreateProductLicenseDetails
from .image_details import ImageDetails
from .image_response import ImageResponse
from .license_metric import LicenseMetric
from .license_record import LicenseRecord
from .license_record_collection import LicenseRecordCollection
from .license_record_summary import LicenseRecordSummary
from .product import Product
from .product_license import ProductLicense
from .product_license_collection import ProductLicenseCollection
from .product_license_consumer_collection import ProductLicenseConsumerCollection
from .product_license_consumer_summary import ProductLicenseConsumerSummary
from .product_license_summary import ProductLicenseSummary
from .top_utilized_product_license_collection import TopUtilizedProductLicenseCollection
from .top_utilized_product_license_summary import TopUtilizedProductLicenseSummary
from .top_utilized_resource_collection import TopUtilizedResourceCollection
from .top_utilized_resource_summary import TopUtilizedResourceSummary
from .update_configuration_details import UpdateConfigurationDetails
from .update_license_record_details import UpdateLicenseRecordDetails
from .update_product_license_details import UpdateProductLicenseDetails

# Maps type names to classes for license_manager services.
license_manager_type_mapping = {
    "BulkUploadCellInfo": BulkUploadCellInfo,
    "BulkUploadFailedRecordInfo": BulkUploadFailedRecordInfo,
    "BulkUploadLicenseRecordsDetails": BulkUploadLicenseRecordsDetails,
    "BulkUploadResponse": BulkUploadResponse,
    "BulkUploadTemplate": BulkUploadTemplate,
    "BulkUploadValidationErrorInfo": BulkUploadValidationErrorInfo,
    "Configuration": Configuration,
    "CreateLicenseRecordDetails": CreateLicenseRecordDetails,
    "CreateProductLicenseDetails": CreateProductLicenseDetails,
    "ImageDetails": ImageDetails,
    "ImageResponse": ImageResponse,
    "LicenseMetric": LicenseMetric,
    "LicenseRecord": LicenseRecord,
    "LicenseRecordCollection": LicenseRecordCollection,
    "LicenseRecordSummary": LicenseRecordSummary,
    "Product": Product,
    "ProductLicense": ProductLicense,
    "ProductLicenseCollection": ProductLicenseCollection,
    "ProductLicenseConsumerCollection": ProductLicenseConsumerCollection,
    "ProductLicenseConsumerSummary": ProductLicenseConsumerSummary,
    "ProductLicenseSummary": ProductLicenseSummary,
    "TopUtilizedProductLicenseCollection": TopUtilizedProductLicenseCollection,
    "TopUtilizedProductLicenseSummary": TopUtilizedProductLicenseSummary,
    "TopUtilizedResourceCollection": TopUtilizedResourceCollection,
    "TopUtilizedResourceSummary": TopUtilizedResourceSummary,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateLicenseRecordDetails": UpdateLicenseRecordDetails,
    "UpdateProductLicenseDetails": UpdateProductLicenseDetails
}
