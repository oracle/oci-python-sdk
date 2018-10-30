# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci

invalid_conversions = ['size_in_g_bs',
                       'size_in_m_bs',
                       'size_in_t_bs',
                       'size_in_k_bs',
                       'size_in_p_bs']


def test_bad_conversions_in_attibute_names():
    # Programmitically get all the models by inspecting all of the modules
    # in oci.
    for x in dir(oci):
        # oci.version is a module and we want to find all the other modules
        instance_x = eval("oci.{}".format(x))
        if isinstance(instance_x, type(oci.version)) and hasattr(instance_x, 'models'):
            for model_name in dir((instance_x).models):
                for attribute in dir(eval("{}.models.{}".format(instance_x.__name__, model_name))):
                    for invalid in invalid_conversions:
                        assert(invalid not in attribute)
