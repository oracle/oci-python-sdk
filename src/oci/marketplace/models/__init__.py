# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .accepted_agreement import AcceptedAgreement
from .accepted_agreement_summary import AcceptedAgreementSummary
from .agreement import Agreement
from .agreement_summary import AgreementSummary
from .category_summary import CategorySummary
from .create_accepted_agreement_details import CreateAcceptedAgreementDetails
from .documentation_link import DocumentationLink
from .error_entity import ErrorEntity
from .image_listing_package import ImageListingPackage
from .item import Item
from .link import Link
from .listing import Listing
from .listing_package import ListingPackage
from .listing_package_summary import ListingPackageSummary
from .listing_summary import ListingSummary
from .named_link import NamedLink
from .orchestration_listing_package import OrchestrationListingPackage
from .orchestration_variable import OrchestrationVariable
from .pricing_model import PricingModel
from .publisher import Publisher
from .publisher_summary import PublisherSummary
from .region import Region
from .report_collection import ReportCollection
from .report_summary import ReportSummary
from .report_type_collection import ReportTypeCollection
from .report_type_summary import ReportTypeSummary
from .screenshot import Screenshot
from .support_contact import SupportContact
from .tax_summary import TaxSummary
from .update_accepted_agreement_details import UpdateAcceptedAgreementDetails
from .upload_data import UploadData

# Maps type names to classes for marketplace services.
marketplace_type_mapping = {
    "AcceptedAgreement": AcceptedAgreement,
    "AcceptedAgreementSummary": AcceptedAgreementSummary,
    "Agreement": Agreement,
    "AgreementSummary": AgreementSummary,
    "CategorySummary": CategorySummary,
    "CreateAcceptedAgreementDetails": CreateAcceptedAgreementDetails,
    "DocumentationLink": DocumentationLink,
    "ErrorEntity": ErrorEntity,
    "ImageListingPackage": ImageListingPackage,
    "Item": Item,
    "Link": Link,
    "Listing": Listing,
    "ListingPackage": ListingPackage,
    "ListingPackageSummary": ListingPackageSummary,
    "ListingSummary": ListingSummary,
    "NamedLink": NamedLink,
    "OrchestrationListingPackage": OrchestrationListingPackage,
    "OrchestrationVariable": OrchestrationVariable,
    "PricingModel": PricingModel,
    "Publisher": Publisher,
    "PublisherSummary": PublisherSummary,
    "Region": Region,
    "ReportCollection": ReportCollection,
    "ReportSummary": ReportSummary,
    "ReportTypeCollection": ReportTypeCollection,
    "ReportTypeSummary": ReportTypeSummary,
    "Screenshot": Screenshot,
    "SupportContact": SupportContact,
    "TaxSummary": TaxSummary,
    "UpdateAcceptedAgreementDetails": UpdateAcceptedAgreementDetails,
    "UploadData": UploadData
}
