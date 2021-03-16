# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from io import SEEK_SET
import logging

logger = logging.getLogger(__name__)


def should_record_body_position_for_retry(func_ref, **func_kwargs):
    func_name = func_ref.__name__
    # TODO: remove Python 2 requirements, use qualname
    if func_name == 'call_api':
        body = func_kwargs.get('body')
        # A file-like object body should be treated differently for retry
        if body and hasattr(body, 'read'):
            return True
        return False
    return False


def record_body_position_for_retry(body):
    is_body_retryable = True
    if getattr(body, 'tell', None) is not None:
        try:
            # Attempt to record current body position
            body_position = body.tell()
        except (IOError, OSError):
            # If we cannot record the current body position for a file-like body, then we should not retry
            is_body_retryable = False
            body_position = None
            logger.warning("Unable to record body position for retrying. This request will not be retried")
    else:
        # If the body does not support tell, then don't retry
        is_body_retryable = False
        body_position = None
        logger.warning("Unable to record body position for retrying. This request will not be retried")
    return is_body_retryable, body_position


def rewind_body_for_retry(body, body_position):
    if getattr(body, 'seek', None) is not None:
        try:
            body.seek(body_position, SEEK_SET)
        except (IOError, OSError):
            # If we're unable to reset the body position, then we should not retry
            logger.warning("Unable to reset body position for retrying. This request will not be retried")
            return False
        return True
    # if the body does not support seek, then we should not retry
    logger.warning("Unable to reset body position for retrying. This request will not be retried")
    return False
