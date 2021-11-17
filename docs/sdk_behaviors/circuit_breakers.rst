.. _circuit_breakers:

Circuit Breakers
~~~~~~~~~~~~~~~~
In case of an outage, retries can overwhelm the service.
To mitigate the issue, we have introduced the concept of circuit breakers in the SDK which can help reduce these ramifications
when configured. The SDK is utilizing the `CircuitBreaker library <https://pypi.org/project/circuitbreaker/>`__ to enable
this functionality. More information on this library can be found on `CircuitBreaker Github page <https://github.com/fabfuel/circuitbreaker>`__

Introduction
------------
The basic idea behind the circuit breaker is very simple.
A protected function call (a REST call in this case) is wrapped in a circuit breaker object, which monitors for failures.
Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker
return with an error, without the protected call being made at all.
This saves the service from being overwhelmed with network calls in case of an outage.

Circuit Breaker States
----------------------
The circuit breaker has a concept similar to the circuit breaker in Electronics. When we reach a overload state,
the circuit breaker trips to mitigates the further damage automatically. This behavior is mimicked by the three states of
the circuit breaker in the SDK.

Closed
^^^^^^
This is the initial state of the circuit breaker. In this state, the circuit breaker allows all requests to pass through
and hit the service. If the requests return success, then the circuit stays in the closed state, if there are any failures
the circuit breaker increments the failure count and any subsequent success resets the failure count. When the failure count
reaches the failure threshold, the circuit breaker trips and moves to the Open state.

Open
^^^^
In this state, none of the network calls are allowed to hit the service for reset timeout duration.
After the reset timeout, the circuit transitions into the half open state.

Half Open
^^^^^^^^^
In this state, the circuit is ready to make a real call as trial to see if the problem is fixed.
If the call results in success, the circuit transitions into the closed state, otherwise, the reset timeout is restarted
and the circuit is put back into the open state.

Circuit Breaker Strategy
------------------------
The :py:class:`~oci.circuit_breaker.CircuitBreakerStrategy`  is a helper class that users can utilize to configure custom
circuit breaker strategy that suits their needs.

Creating a custom CircuitBreakerStrategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An example on how to create a custom circuit breaker strategy using this helper class is as follows:-

.. code-block:: python

    import oci
    from oci.circuit_breaker import CircuitBreakerStrategy

    # Create a custom Circuit Breaker Strategy.
    custom_circuit_breaker_strategy = CircuitBreakerStrategy(
        failure_threshold=5,
        recovery_timeout=40,
        failure_statuses_and_codes={
            409: ["IncorrectState", "Conflict"],
            429: [],
        }
    )

DefaultCircuitBreakerStrategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SDK vends a convenient :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` for users to use to enable
circuit breakers with ease. The default circuit breaker strategy has the following configuration:-

- failure_threshold: 10
- recovery_timeout: 30 seconds
- failure_statuses_and_codes:

  - HTTP 409/IncorrectState
  - HTTP 429
  - HTTP 500
  - HTTP 502
  - HTTP 503
  - HTTP 504

.. important::
    The ``DEFAULT_CIRCUIT_BREAKER_STRATEGY`` should not be modified. Users can use use the ``GLOBAL_CIRCUIT_BREAKER_STRATEGY``
    instead to modify the circuit breaker behavior at the global level.

Configuring Circuit Breaker
---------------------------
By default, clients exposed in the SDK do not have circuit breakers, but circuit breakers can be enabled/disabled in the
SDK at a per client level or for all clients at the global level.

Client level
^^^^^^^^^^^^
Each client object accepts a ``circuit_breaker_strategy`` keyword argument which can be used to set the circuit breaker
strategy for all operations for that client. This circuit breaker strategy could be:

* The default circuit breaker strategy vended by the SDK as :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY`
* The :py:class:`~oci.circuit_breaker.NoCircuitBreakerStrategy`. This will result in no circuit breakers for the client.
* A custom circuit breaker strategy which is an object of the :py:class:`~oci.circuit_breaker.CircuitBreakerStrategy`

Global level
^^^^^^^^^^^^
Users can define a global level circuit breaker strategy programmatically by using :py:data:`oci.circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY`
variable. This strategy will be used by all clients unless overridden by individual clients by using their
``circuit_breaker_strategy`` keyword argument. This circuit breaker strategy can take the following values:

* The default circuit breaker strategy vended by the SDK as :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY`
* The :py:class:`~oci.circuit_breaker.NoCircuitBreakerStrategy()`. This will result in no circuit breakers for the clients.
* A custom circuit breaker strategy which is an object of the :py:class:`~oci.circuit_breaker.CircuitBreakerStrategy`

The SDK also provides a handy alternative to enable/disable Circuit Breakers with Default Circuit Breaker Strategy at
global level by setting the environment variable ``OCI_SDK_DEFAULT_CIRCUITBREAKER_ENABLED`` to True/False.

.. Note::
    Please note that this environment variable is read only once during SDK initialization.

Circuit Breaker Precedence
^^^^^^^^^^^^^^^^^^^^^^^^^^
The Circuit Breaker Precedence in Python SDK (Highest to lowest) is defined as below:-

* Client level Circuit Breaker strategy
* Global level Circuit Breaker strategy set using :py:data:`oci.circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY`
* Environment level override to use default Circuit Breaker strategy at global level via the
  ``OCI_SDK_DEFAULT_CIRCUITBREAKER_ENABLED`` environment variable.

.. important::
    Once a client has been configured with a circuit breaker strategy it can not be modified or removed!

.. Note::
    Some services have enabled circuit breakers for clients by default which would follow the ``oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY``.
    This can be overridden using any alternatives mentioned above. To know which service clients have circuit breakers enabled, look at the service client's 
    description in the SDK - it will say either that it has circuit breakers enabled by default, or that it does not have circuit breakers enabled by default

Examples
--------
A sample on using circuit breakers, including the default strategy and a custom strategy, can be found on
`GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/circuit_breaker_example.py>`__

Configuring Circuit Breaker CallBack Function
---------------------------------------------
Users using the circuit breakers may be interested in performing some custom actions (like logging, metrics, etc)
whenever an API call gets blocked by the circuit breakers. This can be achieved by using the ``circuit_breaker_callback``
functionality.

To use this feature you will need to pass a function as an argument to the ``circuit_breaker_callback``
parameter while creating a service client. This function takes in one argument of type ``CircuitBreakerError`` to get the
exception raised by the configured circuit breaker back from the SDK.
The definition for ``CircuitBreakerError`` can be found `here. <https://github.com/fabfuel/circuitbreaker/blob/develop/circuitbreaker.py>`__

An sample code is as follows:-

.. code-block:: python

    import oci
    import logging

    # Simple callback function
    def callback_function(circuit_breaker_exception):
        logger = logging.getLogger(__name__)
        logger.debug(circuit_breaker_exception)


    #  Setting configuration
    #  Default path for configuration file is "~/.oci/config"
    config = oci.config.from_file()

    identity_client = oci.identity.IdentityClient(config,
                                                  circuit_breaker_strategy=oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY,
                                                  circuit_breaker_callback=callback_function)
    user = identity_client.get_user(user_id=config['user']).data
    print('User data:{}'.format(user))

