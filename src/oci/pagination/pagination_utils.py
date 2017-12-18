# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .internal import retry
from ..response import Response

BASIC_RETRY_STRATEGY = retry.RetryStrategyBuilder() \
                            .add_max_attempts() \
                            .add_service_error_check() \
                            .get_retry_strategy()


def list_call_get_up_to_limit(list_func_ref, record_limit, page_size, *list_func_args, **list_func_kwargs):
    if not record_limit and not page_size:
        raise ValueError('You must provide one, or both, of a record_limit and page_size')

    # If no limit was provided, make a single call
    if record_limit is None:
        list_func_kwargs['limit'] = page_size
        return BASIC_RETRY_STRATEGY.make_retrying_call(list_func_ref, *list_func_args, **list_func_kwargs)

    # If we have a limit, make calls until we get that amount of data
    keep_paginating = True
    remaining_items_to_fetch = record_limit
    call_result = None
    aggregated_results = []
    while keep_paginating and remaining_items_to_fetch > 0:
        list_func_kwargs['limit'] = min(page_size, remaining_items_to_fetch)

        call_result = BASIC_RETRY_STRATEGY.make_retrying_call(list_func_ref, *list_func_args, **list_func_kwargs)
        aggregated_results.extend(call_result.data)
        remaining_items_to_fetch -= len(call_result.data)

        if call_result.next_page is not None:
            list_func_kwargs['page'] = call_result.next_page

        keep_paginating = call_result.has_next_page

    final_response = Response(call_result.status, call_result.headers, aggregated_results, call_result.request)
    return final_response


def list_call_get_all_results(list_func_ref, *list_func_args, **list_func_kwargs):
    keep_paginating = True
    call_result = None
    aggregated_results = []

    while keep_paginating:
        call_result = BASIC_RETRY_STRATEGY.make_retrying_call(list_func_ref, *list_func_args, **list_func_kwargs)
        aggregated_results.extend(call_result.data)

        if call_result.next_page is not None:
            list_func_kwargs['page'] = call_result.next_page

        keep_paginating = call_result.has_next_page

    final_response = Response(call_result.status, call_result.headers, aggregated_results, call_result.request)
    return final_response
