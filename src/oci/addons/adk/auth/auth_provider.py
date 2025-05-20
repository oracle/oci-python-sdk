# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from abc import ABC, abstractmethod
from typing import Any, Dict


class AuthProvider(ABC):
    """Base class for authentication providers."""

    @abstractmethod
    def get_config(self) -> Dict[str, Any]:
        """Get service-specific configuration.

        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        pass

    @abstractmethod
    def get_auth_credentials(self) -> Any:
        """Get authentication credentials.

        Returns:
            Any: Authentication credentials (e.g., API key, signer)
        """
        pass
