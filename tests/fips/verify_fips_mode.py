# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
