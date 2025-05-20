# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.response import Response


class AgentException(Exception):
    """Base exception class for OCI Generative AI ADK errors"""

    def __init__(self, message: str = "", response: Response | None = None):
        self.message = message
        self.response = response

        if response is not None:
            self.status_code = response.status
            self.data = response.data
            self.headers = response.headers
        else:
            self.status_code = None
            self.data = None
            self.headers = None

    def __str__(self):
        if self.response is not None:
            return f"{self.message}. Status code: {self.status_code}. Response data: {self.data}. Response headers: {self.headers}"  # noqa: E501
        else:
            return f"{self.message}"


class AgentError(AgentException):
    """Exception for OCI Agent service errors"""


class UserError(AgentException):
    """Exception for user errors"""
