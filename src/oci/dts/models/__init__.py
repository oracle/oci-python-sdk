# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .attach_devices_details import AttachDevicesDetails
from .change_transfer_job_compartment_details import ChangeTransferJobCompartmentDetails
from .create_transfer_appliance_details import CreateTransferApplianceDetails
from .create_transfer_appliance_entitlement_details import CreateTransferApplianceEntitlementDetails
from .create_transfer_device_details import CreateTransferDeviceDetails
from .create_transfer_job_details import CreateTransferJobDetails
from .create_transfer_package_details import CreateTransferPackageDetails
from .detach_devices_details import DetachDevicesDetails
from .multiple_transfer_appliances import MultipleTransferAppliances
from .multiple_transfer_devices import MultipleTransferDevices
from .multiple_transfer_packages import MultipleTransferPackages
from .new_transfer_device import NewTransferDevice
from .shipping_address import ShippingAddress
from .shipping_vendors import ShippingVendors
from .transfer_appliance import TransferAppliance
from .transfer_appliance_certificate import TransferApplianceCertificate
from .transfer_appliance_encryption_passphrase import TransferApplianceEncryptionPassphrase
from .transfer_appliance_entitlement import TransferApplianceEntitlement
from .transfer_appliance_entitlement_summary import TransferApplianceEntitlementSummary
from .transfer_appliance_public_key import TransferAppliancePublicKey
from .transfer_appliance_summary import TransferApplianceSummary
from .transfer_device import TransferDevice
from .transfer_device_summary import TransferDeviceSummary
from .transfer_job import TransferJob
from .transfer_job_summary import TransferJobSummary
from .transfer_package import TransferPackage
from .transfer_package_summary import TransferPackageSummary
from .update_transfer_appliance_details import UpdateTransferApplianceDetails
from .update_transfer_device_details import UpdateTransferDeviceDetails
from .update_transfer_job_details import UpdateTransferJobDetails
from .update_transfer_package_details import UpdateTransferPackageDetails

# Maps type names to classes for dts services.
dts_type_mapping = {
    "AttachDevicesDetails": AttachDevicesDetails,
    "ChangeTransferJobCompartmentDetails": ChangeTransferJobCompartmentDetails,
    "CreateTransferApplianceDetails": CreateTransferApplianceDetails,
    "CreateTransferApplianceEntitlementDetails": CreateTransferApplianceEntitlementDetails,
    "CreateTransferDeviceDetails": CreateTransferDeviceDetails,
    "CreateTransferJobDetails": CreateTransferJobDetails,
    "CreateTransferPackageDetails": CreateTransferPackageDetails,
    "DetachDevicesDetails": DetachDevicesDetails,
    "MultipleTransferAppliances": MultipleTransferAppliances,
    "MultipleTransferDevices": MultipleTransferDevices,
    "MultipleTransferPackages": MultipleTransferPackages,
    "NewTransferDevice": NewTransferDevice,
    "ShippingAddress": ShippingAddress,
    "ShippingVendors": ShippingVendors,
    "TransferAppliance": TransferAppliance,
    "TransferApplianceCertificate": TransferApplianceCertificate,
    "TransferApplianceEncryptionPassphrase": TransferApplianceEncryptionPassphrase,
    "TransferApplianceEntitlement": TransferApplianceEntitlement,
    "TransferApplianceEntitlementSummary": TransferApplianceEntitlementSummary,
    "TransferAppliancePublicKey": TransferAppliancePublicKey,
    "TransferApplianceSummary": TransferApplianceSummary,
    "TransferDevice": TransferDevice,
    "TransferDeviceSummary": TransferDeviceSummary,
    "TransferJob": TransferJob,
    "TransferJobSummary": TransferJobSummary,
    "TransferPackage": TransferPackage,
    "TransferPackageSummary": TransferPackageSummary,
    "UpdateTransferApplianceDetails": UpdateTransferApplianceDetails,
    "UpdateTransferDeviceDetails": UpdateTransferDeviceDetails,
    "UpdateTransferJobDetails": UpdateTransferJobDetails,
    "UpdateTransferPackageDetails": UpdateTransferPackageDetails
}
