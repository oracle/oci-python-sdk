# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.addons.adk import Toolkit, tool
from typing import Dict, Any


class BillingToolkit(Toolkit):

    @tool
    def get_orders(self, customer_id: str) -> Dict[str, Any]:
        """Get information about an order

        Args:
            user_id (str): The user ID to get information about

        Returns:
            Dict[str, Any]: A dictionary containing the order information
        """
        return [
            {
                "order_id": "order_111111",
                "amount": 100,
                "status": "pending",
                "customer_id": customer_id,
                "order_date": "2024-08-09",
            },
            {
                "order_id": "order_222222",
                "amount": 200,
                "status": "pending",
                "customer_id": customer_id,
                "order_date": "2025-01-02",
            },
        ]

    @tool
    def refund_order(self, order_id: str) -> Dict[str, Any]:
        """Refund an order

        Args:
            order_id (str): The order ID to refund

        Returns:
            Dict[str, Any]: A dictionary containing the refund information
        """
        return {
            "refund_id": "refund_222222",
            "status": "refunded",
            "order_id": order_id,
            "refund_date": "2025-01-01",
            "refund_reason": "customer_requested",
        }
