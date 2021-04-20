.. _sdk-retries:

Retries
~~~~~~~~
By default, operations exposed in the SDK do not retry, but retries can be set in the SDK on a per-operation basis. Each operation accepts a
``retry_strategy`` keyword argument which can be used to set the retry strategy for that operation. This retry stategy could be:

* The default strategy vended by the SDK as :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
* The :py:class:`~oci.retry.NoneRetryStrategy`. This will result in no retries being performed for the operation
* A custom strategy produced via the :py:class:`~oci.retry.RetryStrategyBuilder`

A sample on using retries, including the default strategy and a custom strategy, can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/retries.py>`__

Default Retry Strategy
------------------------
The default retry strategy vended by the SDK has the following attributes:

* 5 total attempts
* Total allowed elapsed time for all requests of 300 seconds (5 minutes)
* Exponential backoff with jitter, using:

    * The base time to use in retry calculations will be 1 second
    * An exponent of 2. When calculating the next retry time we will raise this to the power of the number of attempts
    * A maximum wait time between calls of 30 seconds

* Exponential backoff with equal jitter is used for throttles as this guarantees some sleep time between attempts. The sleep time in this circumstance is calculated as:

.. code-block:: none

    exponential_backoff_sleep_base = min(base_time * (exponent ** attempt_number), max_wait_time)
    sleep_time = (exponential_backoff_sleep_base / 2.0) + random(0, exponential_backoff_sleep_base / 2.0)

* Exponential backoff with full jitter is used for other scenarios where we need to retry (e.g. timeouts, HTTP 5xx). The sleep time in this circumstance is calculated as:

.. code-block:: none

    exponential_backoff_sleep_base = min(base_time * (exponent ** attempt_number), max_wait_time)
    sleep_time = random(0, exponential_backoff_sleep_base)

* Retries on the following exception types:

    * Timeouts and connection errors
    * HTTP 409 (IncorrectState)
    * HTTP 429s (throttles)
    * HTTP 5xx (server errors), except 501
