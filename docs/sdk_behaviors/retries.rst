.. _sdk-retries:

Retries
~~~~~~~~
By default, operations exposed in the SDK do not retry, but retries can be set in the SDK on a per-operation basis. Each operation accepts a
``retry_strategy`` keyword argument which can be used to set the retry strategy for that operation. This retry stategy could be:

* The default strategy vended by the SDK as :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
* The :py:class:`~oci.retry.NoneRetryStrategy`. This will result in no retries being performed for the operation
* A custom strategy produced via the :py:class:`~oci.retry.RetryStrategyBuilder`

A sample on using retries, including the default strategy and a custom strategy, can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/retries.py>`__

Exponential Backoff
-------------------
The client application must implement retries responsibly. If there are N clients retrying for the same resource the work done by service increases proportionally to N^2 as N clients retry in first round, N-1 in second and so on. This quadratic increase in workload can overwhelm the system and can cause further degradation of a service which might already be under stress. A common strategy to avoid this is to use exponential backoff. This strategy essentially makes the client wait progressively longer after each consecutive retry which is exponential in nature.

The wait interval with exponential backoff would be as below:-
::
    exponential_backoff_sleep_base = min(base_time * (exponent ** attempt_number), max_wait_time)

Introducing Jitter
------------------
Exponential backoff solves the problem of overwhelming the service by spreading the retries over a longer interval of time; however, the N clients still retry in lockstep, albeit with retries spaced exponentially farther apart. To remove this synchronous behavior of the retrying clients we can add jitter, which adds randomness, to the wait interval helping these clients to avoid collision.

There are different strategies to implement these timed backoff delays as mentioned below.

Full Jitter
^^^^^^^^^^^^
Instead of using a constant time we can instead use a random value between 0 and the exponential backoff time.

Exponential backoff with full jitter is used for other scenarios where we need to retry because of a failure (e.g. timeouts, HTTP 5xx). The sleep time in this circumstance is calculated as:
::
    exponential_backoff_sleep_base = min(base_time * (exponent ** attempt_number), max_wait_time)
    sleep_time = random(0, exponential_backoff_sleep_base)

Equal Jitter
^^^^^^^^^^^^^
In this strategy we keep some amount of the original backoff and jitter on smaller amount. The intuition behind this it to avoid short sleep scenarios which can again lead to overwhelming the service.

Exponential backoff with equal jitter is used for throttles as this guarantees some sleep time between attempts. The sleep time in this circumstance is calculated as:
::
    exponential_backoff_sleep_base = min(base_time * (exponent ** attempt_number), max_wait_time)
    sleep_time = (exponential_backoff_sleep_base / 2.0) + random(0, exponential_backoff_sleep_base / 2.0)


Default Retry Strategy
------------------------
The default retry strategy vended by the SDK has the following attributes:

* 5 total attempts
* Total allowed elapsed time for all requests of 300 seconds (5 minutes)
* Exponential backoff with jitter, using:

    * The base time to use in retry calculations will be 1 second
    * An exponent of 2. When calculating the next retry time we will raise this to the power of the number of attempts
    * A maximum wait time between calls of 30 seconds

* Retries on the following exception types:

    * Timeouts and connection errors
    * HTTP 409 (IncorrectState)
    * HTTP 429s (throttles)
    * HTTP 5xx (server errors), except 501
