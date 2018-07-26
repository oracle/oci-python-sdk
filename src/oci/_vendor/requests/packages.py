# coding: utf-8
# Modified Work: Copyright (c) 2018, 2018, Oracle and/or its affiliates. All rights reserved.
# Copyright 2018 Kenneth Reitz

import sys

# This code exists for backwards compatibility reasons.
# I don't like it either. Just look the other way. :)

for package in ('urllib3', 'idna', 'chardet'):
    vendored_package = "oci._vendor." + package
    locals()[package] = __import__(vendored_package)
    # This traversal is apparently necessary such that the identities are
    # preserved (requests.packages.urllib3.* is urllib3.*)
    for mod in list(sys.modules):
        if mod == vendored_package or mod.startswith(vendored_package + '.'):
            unprefixed_mod = mod[len("oci._vendor."):]
            sys.modules['oci._vendor.requests.packages.' + unprefixed_mod] = sys.modules[mod]

# Kinda cool, though, right?
