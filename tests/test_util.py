# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import pytest
from tests.util import enum_to_snake


# Parametrized test to cover multiple test cases
@pytest.mark.parametrize("input_str, expected_output", [
    ("HelloWorld", "hello_world"),
    ("Hello-World", "hello_world"),
    ("Hello:World", "hello_world"),
    ("Hello.World", "hello_world"),
    ("Hello:World-Test", "hello_world_test"),
    ("Hello:One:World", "hello_one_world"),
    ("", ""),
    ("A", "a"),
    ("hello", "hello"),
    ("HELLO", "hello")
])
def test_enum_to_snake_parametrized(input_str, expected_output):
    assert enum_to_snake(input_str) == expected_output
