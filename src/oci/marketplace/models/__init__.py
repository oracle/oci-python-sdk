# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .accepted_agreement import AcceptedAgreement
from .accepted_agreement_summary import AcceptedAgreementSummary
from .agreement import Agreement
from .agreement_summary import AgreementSummary
from .category_summary import CategorySummary
from .change_publication_compartment_details import ChangePublicationCompartmentDetails
from .create_accepted_agreement_details import CreateAcceptedAgreementDetails
from .create_image_publication_package import CreateImagePublicationPackage
from .create_publication_details import CreatePublicationDetails
from .create_publication_package import CreatePublicationPackage
from .documentation_link import DocumentationLink
from .error_entity import ErrorEntity
from .eula import Eula
from .free_text_search_details import FreeTextSearchDetails
from .image_listing_package import ImageListingPackage
from .image_publication_package import ImagePublicationPackage
from .international_market_price import InternationalMarketPrice
from .item import Item
from .launch_eligibility import LaunchEligibility
from .link import Link
from .listing import Listing
from .listing_package import ListingPackage
from .listing_package_summary import ListingPackageSummary
from .listing_summary import ListingSummary
from .named_link import NamedLink
from .operating_system import OperatingSystem
from .orchestration_listing_package import OrchestrationListingPackage
from .orchestration_publication_package import OrchestrationPublicationPackage
from .orchestration_variable import OrchestrationVariable
from .pricing_model import PricingModel
from .publication import Publication
from .publication_package import PublicationPackage
from .publication_package_summary import PublicationPackageSummary
from .publication_summary import PublicationSummary
from .publisher import Publisher
from .publisher_summary import PublisherSummary
from .region import Region
from .report_collection import ReportCollection
from .report_summary import ReportSummary
from .report_type_collection import ReportTypeCollection
from .report_type_summary import ReportTypeSummary
from .screenshot import Screenshot
from .search_listings_details import SearchListingsDetails
from .structured_search_details import StructuredSearchDetails
from .support_contact import SupportContact
from .tax_summary import TaxSummary
from .text_based_eula import TextBasedEula
from .third_party_paid_listing_eligibility import ThirdPartyPaidListingEligibility
from .update_accepted_agreement_details import UpdateAcceptedAgreementDetails
from .update_publication_details import UpdatePublicationDetails
from .upload_data import UploadData

# Maps type names to classes for marketplace services.
marketplace_type_mapping = {
    "AcceptedAgreement": AcceptedAgreement,
    "AcceptedAgreementSummary": AcceptedAgreementSummary,
    "Agreement": Agreement,
    "AgreementSummary": AgreementSummary,
    "CategorySummary": CategorySummary,
    "ChangePublicationCompartmentDetails": ChangePublicationCompartmentDetails,
    "CreateAcceptedAgreementDetails": CreateAcceptedAgreementDetails,
    "CreateImagePublicationPackage": CreateImagePublicationPackage,
    "CreatePublicationDetails": CreatePublicationDetails,
    "CreatePublicationPackage": CreatePublicationPackage,
    "DocumentationLink": DocumentationLink,
    "ErrorEntity": ErrorEntity,
    "Eula": Eula,
    "FreeTextSearchDetails": FreeTextSearchDetails,
    "ImageListingPackage": ImageListingPackage,
    "ImagePublicationPackage": ImagePublicationPackage,
    "InternationalMarketPrice": InternationalMarketPrice,
    "Item": Item,
    "LaunchEligibility": LaunchEligibility,
    "Link": Link,
    "Listing": Listing,
    "ListingPackage": ListingPackage,
    "ListingPackageSummary": ListingPackageSummary,
    "ListingSummary": ListingSummary,
    "NamedLink": NamedLink,
    "OperatingSystem": OperatingSystem,
    "OrchestrationListingPackage": OrchestrationListingPackage,
    "OrchestrationPublicationPackage": OrchestrationPublicationPackage,
    "OrchestrationVariable": OrchestrationVariable,
    "PricingModel": PricingModel,
    "Publication": Publication,
    "PublicationPackage": PublicationPackage,
    "PublicationPackageSummary": PublicationPackageSummary,
    "PublicationSummary": PublicationSummary,
    "Publisher": Publisher,
    "PublisherSummary": PublisherSummary,
    "Region": Region,
    "ReportCollection": ReportCollection,
    "ReportSummary": ReportSummary,
    "ReportTypeCollection": ReportTypeCollection,
    "ReportTypeSummary": ReportTypeSummary,
    "Screenshot": Screenshot,
    "SearchListingsDetails": SearchListingsDetails,
    "StructuredSearchDetails": StructuredSearchDetails,
    "SupportContact": SupportContact,
    "TaxSummary": TaxSummary,
    "TextBasedEula": TextBasedEula,
    "ThirdPartyPaidListingEligibility": ThirdPartyPaidListingEligibility,
    "UpdateAcceptedAgreementDetails": UpdateAcceptedAgreementDetails,
    "UpdatePublicationDetails": UpdatePublicationDetails,
    "UploadData": UploadData
}
