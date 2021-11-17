.. _sdk-retries:

Retries
~~~~~~~~
By default, operations exposed in the SDK do not retry, but retries can be set in the SDK on a per-operation basis. Each operation accepts a
``retry_strategy`` keyword argument which can be used to set the retry strategy for that operation. This retry strategy could be:

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

De-correlated Jitter
^^^^^^^^^^^^^^^^^^^^
In this strategy we keep some amount of De-correlated Jitter (default 1 second) to reduce the number of collisions between the subsequent retrying calls.
::
    exponential_backoff_sleep_base = base_time * (exponent ** (attempt_number - 1))
    sleep_time = min(exponential_backoff_sleep_base + random.uniform(0, decorrelated_jitter), max_wait_between_calls_seconds)

Default Retry Strategy
-----------------------
The default retry strategy vended by the SDK has the following attributes:

* 8 total attempts
* Total allowed elapsed time for all requests of 600 seconds (10 minutes)
* Exponential backoff with de-correlated jitter of 1000 ms, using:

    * The base time to use in retry calculations will be 1 second
    * An exponent of 2. When calculating the next retry time we will raise this to the power of the number of attempts
    * A maximum wait time between calls of 30 seconds

* Retries on the following exception types:

    * Timeouts and connection errors
    * HTTP 409 (IncorrectState)
    * HTTP 429s (throttles)
    * HTTP 5xx (server errors), except 501

Customizing Retry Strategy
--------------------------
As mentioned above, users can create there own custom retry strategy using :py:class:`~oci.retry.RetryStrategyBuilder` class.

An example for this is below:-
::
    custom_retry_strategy = oci.retry.RetryStrategyBuilder(
        # Make up to 10 service calls
        max_attempts_check=True,
        max_attempts=10,

        # Don't exceed a total of 600 seconds for all service calls
        total_elapsed_time_check=True,
        total_elapsed_time_seconds=600,

        # Wait 45 seconds between attempts
        retry_max_wait_between_calls_seconds=45,

        # Use 2 seconds as the base number for doing sleep time calculations
        retry_base_sleep_time_seconds=2,

        # Retry on certain service errors:
        #
        #   - 5xx code received for the request
        #   - Any 429 (this is signified by the empty array in the retry config)
        #   - 400s where the code is QuotaExceeded or LimitExceeded
        service_error_check=True,
        service_error_retry_on_any_5xx=True,
        service_error_retry_config={
            400: ['QuotaExceeded', 'LimitExceeded'],
            429: []
        },

        # Use exponential backoff and retry with full jitter, but on throttles use
        # exponential backoff and retry with equal jitter
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE
    ).get_retry_strategy()

Overriding the Retry behavior at Operation Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To use a custom retry strategy for an operation, a custom retry strategy can be passed through the ``retry_strategy``
keyword argument.

An Example would be:-
::
    # Default config file and profile
    config = oci.config.from_file()
    compartment_id = config["tenancy"]

    # Service client
    identity_client = oci.identity.IdentityClient(config)

    # Operation Retry Strategy override
    response = identity_client.list_region_subscriptions(compartment_id, retry_strategy=custom_retry_strategy)

    # For convenience the Default Retry Strategy vended by the SDK can also be used here
    response = identity_client.list_region_subscriptions(compartment_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

To disable retries at Operation level you can use:-
::
    response = identity.list_region_subscriptions(compartment_id, retry_strategy=oci.retry.NoneRetryStrategy())

Overriding the Retry behavior at Client Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To use a custom retry strategy for all operations for client, a custom retry strategy can be passed through
the ``retry_strategy`` keyword argument while initializing the client

An Example would be:-
::
    # Default config file and profile
    config = oci.config.from_file()
    compartment_id = config["tenancy"]

    # Service client that uses custom retry strategy for all operations
    identity_client = oci.identity.IdentityClient(config, retry_strategy=custom_retry_strategy)

    # For convenience the Default Retry Strategy vended by the SDK can also be used here
    identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

To disable retries at the client level:-
::
    identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.NoneRetryStrategy())

Overriding the Retry behavior at Global/SDK Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To override the SDK level global retries for service client operations programmatically, a retry strategy can be passed
to the variable :py:data:`~oci.retry.GLOBAL_RETRY_STRATEGY`. This retry strategy can be:

* The default strategy vended by the SDK as :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
* The :py:class:`~oci.retry.NoneRetryStrategy`. This will result in no retries being performed for the operation
* A custom strategy produced via the :py:class:`~oci.retry.RetryStrategyBuilder`

The python SDK also provides a handy way of enabling/disabling retries at global level using environment variables.
::
    # Set the following environment variable to False
    OCI_SDK_DEFAULT_RETRY_ENABLED=False

    # Setting the environment variable to True will enable retries with DEFAULT_RETRY_STRATEGY
    OCI_SDK_DEFAULT_RETRY_ENABLED=True

Retry Behavior Precedence
^^^^^^^^^^^^^^^^^^^^^^^^^
The Retry behavior Precedence in Python SDK (Highest to lowest) is defined as below:-

* Operation level retry strategy
* Client level retry strategy
* Global level retry strategy set using ``oci.retry.GLOBAL_RETRY_STRATEGY``
* Environment level override via the ``OCI_SDK_DEFAULT_RETRY_ENABLED`` environment variable

.. Note::
    Some services can enable retries for operations by default which would follow the ``oci.retry.DEFAULT_RETRY_STRATEGY``.
    This can be overridden using any alternatives mentioned above. To know which service operations have retries enabled by default, 
    look at the operation's description in the SDK - it will say either that it has retries enabled by default, or that it does not have retries enabled by default. 