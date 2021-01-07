# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci

invalid_conversions = ['in_g_bs',
                       'in_m_bs',
                       'in_t_bs',
                       'in_k_bs',
                       'in_p_bs']

# Ignore some attributes for this test.
# We found this bug a little too late and these properties already exist in the public SDK
# Instead of re-gening with the correct name and have breaking changes, it is better to leave them unchanged
ignored_attributes = (("blockchain", "BlockchainPlatform", "storage_used_in_t_bs"),
                      ("core", "ShapeMemoryOptions", "min_in_g_bs"),
                      ("core", "ShapeMemoryOptions", "max_in_g_bs"),
                      ("core", "ShapeMemoryOptions", "default_per_ocpu_in_g_bs"),
                      ("database", "DbSystemShapeSummary", "min_memory_per_node_in_g_bs"),
                      ("database", "DbSystemShapeSummary", "available_db_node_storage_in_g_bs"),
                      ("database", "DbSystemShapeSummary", "min_db_node_storage_per_node_in_g_bs"),
                      ("database", "DbSystemShapeSummary", "available_data_storage_in_t_bs"),
                      ("database", "DbSystemShapeSummary", "min_data_storage_in_t_bs"),
                      ("database", "ExadataInfrastructure", "max_db_node_storage_in_g_bs"),
                      ("database", "ExadataInfrastructure", "max_data_storage_in_t_bs"),
                      ("database", "ExadataInfrastructureSummary", "max_db_node_storage_in_g_bs"),
                      ("database", "ExadataInfrastructureSummary", "max_data_storage_in_t_bs"),
                      ("nosql", "QueryDetails", "max_read_in_k_bs"),
                      ("nosql", "TableLimits", "max_storage_in_g_bs"),
                      ("nosql", "TableUsageSummary", "storage_in_g_bs"))


def test_bad_conversions_in_attibute_names():
    # Programmatically get all the models by inspecting all of the modules
    # in oci.
    for x in dir(oci):
        # oci.version is a module and we want to find all the other modules
        instance_x = eval("oci.{}".format(x))
        if isinstance(instance_x, type(oci.version)) and hasattr(instance_x, 'models'):
            for model_name in dir((instance_x).models):
                for attribute in dir(eval("{}.models.{}".format(instance_x.__name__, model_name))):
                    # Continue for attributes in ignore list
                    if (x, model_name, attribute) in ignored_attributes:
                        continue
                    for invalid in invalid_conversions:
                        assert(invalid not in attribute)
