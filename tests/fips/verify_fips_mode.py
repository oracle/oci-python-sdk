# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

# This program launches oci and checks to see if it is in FIPs mode
# There must be an environment variable set to get oci to automatically
# enter FIPS mode and this program expects to the environment to
# be set correctly.  See /src/oci/fips for list of environment
# variables which can be used to start FIPS mode.

import logging
logging.basicConfig(level=logging.INFO)

import oci  # NOQA: E402
print(oci.version.__version__)

assert oci.fips.is_fips_mode(), "Expected FIPS mode to be True"
