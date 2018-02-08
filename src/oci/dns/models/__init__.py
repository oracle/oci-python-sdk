# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .create_zone_details import CreateZoneDetails
from .external_master import ExternalMaster
from .patch_domain_records_details import PatchDomainRecordsDetails
from .patch_rr_set_details import PatchRRSetDetails
from .patch_zone_records_details import PatchZoneRecordsDetails
from .rr_set import RRSet
from .record import Record
from .record_collection import RecordCollection
from .record_details import RecordDetails
from .record_operation import RecordOperation
from .tsig import TSIG
from .update_domain_records_details import UpdateDomainRecordsDetails
from .update_rr_set_details import UpdateRRSetDetails
from .update_zone_details import UpdateZoneDetails
from .update_zone_records_details import UpdateZoneRecordsDetails
from .zone import Zone
from .zone_summary import ZoneSummary

# Maps type names to classes for dns services.
dns_type_mapping = {
    "CreateZoneDetails": CreateZoneDetails,
    "ExternalMaster": ExternalMaster,
    "PatchDomainRecordsDetails": PatchDomainRecordsDetails,
    "PatchRRSetDetails": PatchRRSetDetails,
    "PatchZoneRecordsDetails": PatchZoneRecordsDetails,
    "RRSet": RRSet,
    "Record": Record,
    "RecordCollection": RecordCollection,
    "RecordDetails": RecordDetails,
    "RecordOperation": RecordOperation,
    "TSIG": TSIG,
    "UpdateDomainRecordsDetails": UpdateDomainRecordsDetails,
    "UpdateRRSetDetails": UpdateRRSetDetails,
    "UpdateZoneDetails": UpdateZoneDetails,
    "UpdateZoneRecordsDetails": UpdateZoneRecordsDetails,
    "Zone": Zone,
    "ZoneSummary": ZoneSummary
}
