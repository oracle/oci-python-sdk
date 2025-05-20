# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
A prebuilt toolkit for performing calculations
"""

from oci.addons.adk.tool import Toolkit, tool


class CalculatorToolkit(Toolkit):
    """A toolkit for performing calculations"""

    def __init__(self):
        super().__init__()

    @tool
    def add(self, left: float, right: float) -> float:
        """Add two floats

        Args:
            left(float): The left operand
            right(float): The right operand

        Returns:
            The sum of the two operands
        """
        return left + right

    @tool
    def subtract(self, left: float, right: float) -> float:
        """Subtract two floats

        Args:
            left(float): The left operand
            right(float): The right operand

        Returns:
            The difference of the two operands
        """
        return left - right

    @tool
    def multiply(self, left: float, right: float) -> float:
        """Multiply two floats

        Args:
            left(float): The left operand
            right(float): The right operand

        Returns:
            The product of the two operands
        """
        return left * right

    @tool
    def divide(self, left: float, right: float) -> float:
        """Divide two floats

        Args:
            left(float): The left operand
            right(float): The right operand

        Returns:
            The quotient of the two operands
        """
        return left / right

    @tool
    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent

        Args:
            base(float): The base
            exponent(float): The exponent

        Returns:
            The result of raising the base to the power of the exponent
        """
        return base**exponent

    @tool
    def sqrt(self, number: float) -> float:
        """Square root of a number

        Args:
            number(float): The number to square root

        Returns:
            The square root of the number
        """
        return number**0.5

    def evaluate(self, expression: str) -> float:
        """A method that will not be registered as a tool

        Args:
            expression: The expression to evaluate

        Returns:
            The result of the expression
        """
        raise NotImplementedError("This is not implemented")
