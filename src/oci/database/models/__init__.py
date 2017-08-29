# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .create_database_details import CreateDatabaseDetails
from .create_db_home_details import CreateDbHomeDetails
from .create_db_home_with_db_system_id_details import CreateDbHomeWithDbSystemIdDetails
from .database import Database
from .database_summary import DatabaseSummary
from .db_home import DbHome
from .db_home_summary import DbHomeSummary
from .db_node import DbNode
from .db_node_summary import DbNodeSummary
from .db_system import DbSystem
from .db_system_shape_summary import DbSystemShapeSummary
from .db_system_summary import DbSystemSummary
from .db_version_summary import DbVersionSummary
from .launch_db_system_details import LaunchDbSystemDetails
from .update_db_system_details import UpdateDbSystemDetails

# Maps type names to classes for database services.
database_type_mapping = {
    "CreateDatabaseDetails": CreateDatabaseDetails,
    "CreateDbHomeDetails": CreateDbHomeDetails,
    "CreateDbHomeWithDbSystemIdDetails": CreateDbHomeWithDbSystemIdDetails,
    "Database": Database,
    "DatabaseSummary": DatabaseSummary,
    "DbHome": DbHome,
    "DbHomeSummary": DbHomeSummary,
    "DbNode": DbNode,
    "DbNodeSummary": DbNodeSummary,
    "DbSystem": DbSystem,
    "DbSystemShapeSummary": DbSystemShapeSummary,
    "DbSystemSummary": DbSystemSummary,
    "DbVersionSummary": DbVersionSummary,
    "LaunchDbSystemDetails": LaunchDbSystemDetails,
    "UpdateDbSystemDetails": UpdateDbSystemDetails
}
