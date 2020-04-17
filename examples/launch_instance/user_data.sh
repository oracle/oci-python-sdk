# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#!/bin/bash

# This file will be Base64-ed and provided as user_data when launching an instance.
# See: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/LaunchInstanceDetails
# for more information

mkdir /tmp/mydir
touch /tmp/mydir/mytxt.txt