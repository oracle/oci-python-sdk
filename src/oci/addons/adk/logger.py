# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import logging
import os
from typing import Any, Optional, Union

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.traceback import install as install_rich_traceback


class ADKLogger:
    """
    A customized logger for the Agent Development Kit
    that uses RichHandler for console output
    and FileHandler for file output.
    Maintains rich formatting for console output while
    providing configurable logging levels and file output.
    """

    def __init__(
        self,
        name: str = "adk",
        level: Union[int, str] = logging.INFO,
        file_path: Optional[str] = None,
        file_level: Union[int, str] = logging.DEBUG,
        console: Optional[Console] = None,
    ):
        """
        Initialize the ADK logger.

        Args:
            name: Logger name
            level: Console logging level
                (can be string like 'INFO' or int like logging.INFO)
            file_path: Path to log file, if None, file logging is disabled
            file_level: File logging level
            console: Optional Rich console instance
        """
        # Convert string level to int if necessary
        if isinstance(level, str):
            level = getattr(logging, level.upper(), logging.INFO)

        if isinstance(file_level, str):
            file_level = getattr(logging, file_level.upper(), logging.DEBUG)

        # Initialize Rich console or use the provided one
        self.console = console or Console(log_time=False, log_path=False)

        # Install rich traceback handler for better exception display
        install_rich_traceback()

        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(min(level, file_level))  # Set to lowest of the two levels
        self.logger.propagate = False  # Prevent double logging

        # Clear existing handlers if there are any
        if self.logger.handlers:
            self.logger.handlers.clear()

        # Configure Rich handler for console output
        self.shell_handler = RichHandler(
            console=self.console,
            rich_tracebacks=True,
            markup=True,
            show_time=True,
            show_level=True,
            show_path=False,
            log_time_format="[%x %X] ",
        )
        self.shell_handler.setLevel(level)
        self.logger.addHandler(self.shell_handler)

        # Configure file handler if requested
        self.file_handler = None
        if file_path:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            self.file_handler = logging.FileHandler(file_path)
            self.file_handler.setLevel(file_level)
            file_formatter = logging.Formatter(
                "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d] %(message)s"  # noqa: E501
            )
            self.file_handler.setFormatter(file_formatter)
            self.logger.addHandler(self.file_handler)

    # Forward standard logging methods to the underlying logger
    def __getattr__(self, name: str) -> Any:
        """
        Forward any undefined attributes to the underlying logger.
        This allows direct access to all standard logging methods like
        debug(), info(), warning(), error(), etc.
        """
        return getattr(self.logger, name)

    def print(
        self,
        message: Any,
        title: Optional[str] = None,
        border_style: str = "blue",
        expand: bool = False,
    ) -> None:
        """
        Print a message in a panel with rich formatting,
        mirroring console.print(Panel()).

        Args:
            message: The message to print
            title: Optional title for the panel
            border_style: Style for the panel border
            expand: Whether to expand the panel to fill the terminal width
        """
        panel = Panel(message, title=title, border_style=border_style, expand=expand)
        self.console.print(panel)
        # Also log to file if file handler is configured, but without rich formatting
        if self.file_handler:
            plain_message = f"[{title}] {str(message)}" if title else str(message)
            self.logger.info(plain_message)

    def print_exception(self, show_locals: bool = False) -> None:
        """
        Print an exception with rich formatting, mirroring console.print_exception().

        Args:
            show_locals: Whether to show local variables
        """
        self.console.print_exception(show_locals=show_locals)
        self.logger.exception("Exception occurred")


# Create a default logger instance
default_logger = ADKLogger(
    name="adk",
    level=os.environ.get("ADK_LOG_LEVEL", "INFO"),
    file_path=os.environ.get("ADK_LOG_FILE", None),
)


# Get a configured logger
def get_logger(
    name: str = "adk",
    level: Union[int, str] = logging.INFO,
    file_path: Optional[str] = None,
) -> ADKLogger:
    """
    Create and return a configured ADKLogger instance.

    Args:
        name: Logger name
        level: Logging level for console output
        file_path: Path to log file, if None uses the default path

    Returns:
        ADKLogger instance
    """
    return ADKLogger(
        name=name,
        level=level,
        file_path=file_path or os.environ.get("ADK_LOG_FILE", None),
    )
